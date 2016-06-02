#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from datetime import datetime, timedelta
from os.path import expanduser
from terminaltables import SingleTable
import os.path
import sys, re
import zipfile

import requests, json

import xml.etree.ElementTree as ET
import xml.dom.minidom as xmldom

from godockercli.auth import Auth
from godockercli.httputils import HttpUtils


class Utils:

    @staticmethod
    def get_userInfos(login):
        """ get user informations"""

        user = HttpUtils.http_get_request(
            "/api/1.0/user/"+login,
            Auth.server,
            {'Authorization':'Bearer '+Auth.token},
            Auth.noCert
        )

        return user.json()


    @staticmethod
    def get_config_infos():
        """ get the godocker server config """
      
        Auth.authenticate()

        config = HttpUtils.http_get_request("/api/1.0/config", Auth.server, {}, Auth.noCert)

        json_config=config.json()

        return json_config

    @staticmethod
    def get_docker_images():
        """ get the list if docker images infos"""

	return Utils.get_config_infos()['images']


    @staticmethod
    def get_docker_images_url():
        """ get the docker images url list """

        images = Utils.get_docker_images()

        tab_images=[]
        for image in images:
            tab_images.append(image['url'])

        return tab_images

    @staticmethod
    def get_docker_images_url_interactive():
        """ get the docker interactive images url list"""
        
        interactive_images = []
        
        for image in Utils.get_docker_images():
            if image['interactive']:
                interactive_images.append(image['url'])

        return interactive_images
        

    @staticmethod
    def get_contraint_labels():
        """ get the list of authorized lables """

        json_config=Utils.get_config_infos()

        constraints = []

        for constraint in json_config['constraints']:
            for value in constraint["value"]:
                constraints.append(constraint["name"]+"=="+value)

        return constraints

    @staticmethod
    def get_projects_for_user():
        """ return project array """

        Auth.authenticate()

        projects = HttpUtils.http_get_request(
            "/api/1.0/user/"+Auth.login+"/project",
            Auth.server, {'Authorization':'Bearer '+Auth.token},
            Auth.noCert
        )

        list_project = []

        for project in projects.json():
            list_project.append(project['id'])

        return list_project

    @staticmethod
    def get_volumes_infos():
        """ return volumes array """

        return Utils.get_config_infos()["volumes"]

    @staticmethod
    def get_executor_features():
        """ return executor features """
        
        return Utils.get_config_infos()["executor_features"]

    @staticmethod
    def get_volumes_name():
        """ return volumes name only """

        volumes = Utils.get_volumes_infos()
        volumes_list=[]
        for volume in volumes:
            volumes_list.append(volume['name'])

        return volumes_list

    @staticmethod
    def get_acl_for_volume(volume_name):
        """ return the volume acl """

        volumes = Utils.get_volumes_infos()
        for volume in volumes:
            if volume['name'] == volume_name:
                return volume['acl']


    @staticmethod
    def get_execution_status(exit_code):
        """ return the execution code for a job """

        if exit_code>0 and exit_code!=137:
            return 'error'
        elif exit_code == 137:
            return 'warning'
        else:
            return 'success'


    @staticmethod
    def is_finish(job_id):
        """ test if job is finish """
        Auth.authenticate()

        task = HttpUtils.http_get_request(
            "/api/1.0/task/"+str(job_id),
            Auth.server,
            {'Authorization':'Bearer '+Auth.token},
            Auth.noCert
        )

        job=task.json()

        # test if job has been launch and is finish
        if 'date_running' in job["status"] and job["status"]['date_over'] is not None:
            return True
        else:
            return False

    @staticmethod
    def get_user_details_xml(user, login):
        """ write user infos in a xml file  """
        user_infos = user.json()

        #general infos table
        myuser = ET.Element("user")
        ET.SubElement(myuser, "login").text = user_infos['id']
        ET.SubElement(myuser, "api_key").text = user_infos['credentials']['apikey']
        ET.SubElement(myuser, "email").text = user_infos['email']
        ET.SubElement(myuser, "admin").text = str(user_infos['admin'])
        ET.SubElement(myuser, "home_directory").text = user_infos['homeDirectory']
        ET.SubElement(myuser, "uid").text = str(user_infos['uid'])
        ET.SubElement(myuser, "gid").text =  str(user_infos['gid'])

        quota = ET.SubElement(myuser, "quota")
        if 'quota_ram' in user_infos['usage']:
            ET.SubElement(quota, "ram").text = str(user_infos['usage']['quota_ram'])
            ET.SubElement(quota, "cpu").text = str(user_infos['usage']['quota_cpu'])
            ET.SubElement(quota, "time").text = str(user_infos['usage']['quota_time'])
            ET.SubElement(quota, "priority").text = str(user_infos['usage']['prio'])

        projects = HttpUtils.http_get_request("/api/1.0/user/"+login+"/project", Auth.server, {'Authorization':'Bearer '+Auth.token}, Auth.noCert)
 
        myprojects = ET.SubElement(myuser, "projects")

        for project in projects.json():
            myproject = ET.SubElement(myprojects, "project")
            ET.SubElement(myproject, "id").text = str(project['id'])
            ET.SubElement(myproject, "priority").text = str(project['prio'])
            if project["id"] == "default":
                ET.SubElement(myproject, "description")
            else:
                ET.SubElement(myproject, "description").text = str(project['description'])  

        usage = HttpUtils.http_get_request("/api/1.0/user/"+login+"/usage", Auth.server, {'Authorization':'Bearer '+Auth.token}, Auth.noCert)

        myusage = ET.SubElement(myuser, "usage")
        for date in usage.json():
            mydate = ET.SubElement(myusage, "date")
            mydate.set("value", datetime.strptime(str(date['date']), "%Y_%m_%d").strftime('%d %b %Y'))
            ET.SubElement(mydate, "datetime").text = str(date['date'])
            ET.SubElement(mydate, "ram").text = str(date['ram'])
            ET.SubElement(mydate, "cpu").text = str(date['cpu'])
            ET.SubElement(mydate, "time").text = str(timedelta(seconds=date['time']))

        if user_infos['credentials']['public'] != "":
            ET.SubElement(myuser, "ssh_key").text = str(user_infos['credentials']['public'])
        else:
            ET.SubElement(myuser, "ssh_key")

        # write in a temp xml file
        tree = ET.ElementTree(myuser)
        tree.write("/tmp/.user_infos.xml")
        xml = xmldom.parse("/tmp/.user_infos.xml").toprettyxml()

        # write in a final xml (pretty)
        xmlfile = open("user_infos.xml", 'w')
        xmlfile.write(xml)
        xmlfile.close()

        print("Results are available in user_infos.xml file")


    @staticmethod
    def get_task_infos_xml(job, tags):
        """ write task infos in a xml file"""
        myjob = ET.Element("job")
        ET.SubElement(myjob, "id").text = str(job['id'])
        ET.SubElement(myjob, "name").text = str(job["meta"]["name"])
        ET.SubElement(myjob, "description").text = str(job['meta']["description"].encode('utf-8'))
        ET.SubElement(myjob, "tags").text = tags
        ET.SubElement(myjob, "root").text = str(job['container']['root'])
        ET.SubElement(myjob, "interactive").text = str(job['command']['interactive'])

        # tasks dependency
        if 'tasks' in job['requirements']:
            parents = ET.SubElement(myjob, "parents")
            if job['requirements']['tasks']:
                for task in job['requirements']['tasks']:
                    parent = ET.SubElement(parents, "parent")
                    ET.SubElement(parent, "id").text = str(task)

        #data_user
        user = ET.SubElement(myjob, "user")
        ET.SubElement(user, "login").text = str(job['user']['id'])
        ET.SubElement(user, "project").text = str(job['user']['project'])

        # container
        container = ET.SubElement(myjob, "container")
        ET.SubElement(container, "image").text = str(job['container']['image'])
        ET.SubElement(container, "cpu").text = str(job['requirements']['cpu'])
        ET.SubElement(container, "cpu").text = str(job['requirements']['ram'])

        # volumes
        volumes = ET.SubElement(myjob, "volumes")
        for volume in job['container']['volumes']:
            myvolume = ET.SubElement(volumes, "volume")
            ET.SubElement(myvolume, "name").text = str(volume['name'])
            ET.SubElement(myvolume, "path").text = str(volume['path'])
            ET.SubElement(myvolume, "mount").text = str(volume['mount'])
            ET.SubElement(myvolume, "acl").text = str(volume['acl'])
        if 'tmpstorage' in job['requirements'] and job['requirements']['tmpstorage'] is not None:
            myvolume = ET.SubElement(volumes, "volume")
            ET.SubElement(myvolume, "name").text = str(volume['name'])
            ET.SubElement(myvolume, "path").text = str(job['requirements']['tmpstorage']['size'])
            ET.SubElement(myvolume, "mount").text = '/tmp-data'
            ET.SubElement(myvolume, "acl").text = 'rw'

        #data_status
        status = ET.SubElement(myjob, "execution_status")
        ET.SubElement(status, "primary_status").text = str(job["status"]['primary'])
        ET.SubElement(status, "secondary_status").text = str(job["status"]['secondary'])

        # test if task is / has already running
        if 'date_running' in job["status"]:
            ET.SubElement(status, "date_running").text = str(datetime.fromtimestamp(job["status"]['date_running']))
            if job["status"]['date_over'] is not None:
                ET.SubElement(status, "date_over").text = str(datetime.fromtimestamp(job["status"]['date_over']))
            else:
                ET.SubElement(status, "date_over").text = ""
        else:
            ET.SubElement(status, "date_running").text = ""
            ET.SubElement(status, "date_over").text = ""

        #data interactive
        if job['command']['interactive'] and 'date_running' in job["status"] and job["status"]['primary'] == 'running':
            interactive = ET.SubElement(myjob, "interactive")
            ET.SubElement(interactive, "host").text = str(job['container']['meta']['Node']['Name'])
            ET.SubElement(interactive, "port").text = str(" ".join(job['container']['ports']))

        # write in a temp xml file
        tree = ET.ElementTree(myjob)
        tree.write("/tmp/.jobs_infos.xml")
        xml = xmldom.parse("/tmp/.jobs_infos.xml").toprettyxml()

        # write in a final xml (pretty)
        xmlfile = open("jobs_infos.xml", 'w')
        xmlfile.write(xml)
        xmlfile.close()

        print("Results are available in jobs_infos.xml file")

    @staticmethod
    def get_list_tasks_xml(tasks, regex=None):
        """ write a xml file """
        jobs = ET.Element("jobs")
        if regex is not None:
            for job in tasks:
                try:
                    # test for over jobs
                    exitCode = '-'
                    if job['container']['meta'] is not None and 'State' in job['container']['meta']:
                        exitCode = Utils.get_execution_status(job['container']['meta']['State']['ExitCode'])
                    
                    tags = ",".join(job['meta']['tags'])

                    # test regex
                    if re.search(regex, str(job['id'])) or \
                       re.search(regex, str(job['meta']['name'])) or \
                       re.search(regex, str(job['meta']['description'])) or \
                       re.search(regex, str(job['user']['id'])) or \
                       re.search(regex, str(job['container']['image'])) or \
                       re.search(regex, tags) or \
                       re.search(regex, exitCode):

                        single_job = ET.SubElement(jobs, "job")
                        ET.SubElement(single_job, "id").text = str(job['id'])
                        ET.SubElement(single_job, "name").text = job['meta']['name']
                        ET.SubElement(single_job, "description").text = job['meta']['description'][:15]
                        ET.SubElement(single_job, "user").text = job['user']['id']
                        ET.SubElement(single_job, "container").text = job['container']['image']
                        ET.SubElement(single_job, "event").text = str(job['status']['secondary'])
                        ET.SubElement(single_job, "status").text = exitCode
                        ET.SubElement(single_job, "ram").text = str(job['requirements']['ram'])
                        ET.SubElement(single_job, "cpu").text = str(job['requirements']['cpu'])
                        ET.SubElement(single_job, "root").text = str(job['container']['root'])
                        ET.SubElement(single_job, "interactive").text = str(job['command']['interactive'])
                except: 
                    print("Error parsing json for job :"+str(job['id']))  
        else:
            for job in tasks:
                try:
                    # test for over jobs
                    exitCode = '-'
                    if job['container']['meta'] is not None and 'State' in job['container']['meta']:
                        exitCode = Utils.get_execution_status(job['container']['meta']['State']['ExitCode'])

                    single_job = ET.SubElement(jobs, "job")
                    ET.SubElement(single_job, "id").text = str(job['id'])
                    ET.SubElement(single_job, "name").text = job['meta']['name']
                    ET.SubElement(single_job, "description").text = job['meta']['description'][:15]
                    ET.SubElement(single_job, "user").text = job['user']['id']
                    ET.SubElement(single_job, "container").text = job['container']['image']
                    ET.SubElement(single_job, "event").text = str(job['status']['secondary'])
                    ET.SubElement(single_job, "status").text = exitCode
                    ET.SubElement(single_job, "ram").text = str(job['requirements']['ram'])
                    ET.SubElement(single_job, "cpu").text = str(job['requirements']['cpu'])
                    ET.SubElement(single_job, "root").text = str(job['container']['root'])
                    ET.SubElement(single_job, "interactive").text = str(job['command']['interactive'])
                except:
                    print("Error parsing json for job :"+str(job['id']))

        # write in a temp xml file
        tree = ET.ElementTree(jobs)
        tree.write("/tmp/.jobs.xml")
        xml = xmldom.parse("/tmp/.jobs.xml").toprettyxml()

        # write in a final xml (pretty)
        xmlfile = open("jobs_list.xml", 'w')
        xmlfile.write(xml)
        xmlfile.close()

        print("Results are available in jobs_list.xml file")


    @staticmethod
    def get_list_tasks_table(tasks, regex=None):
        """ return the over tasks in a table """

        table_data = []
        table_data.append(
            ['id',
            'name',
            'description',
            'user',
            'container',
            'event',
            'status',
            'ram',
            'cpu',
            'root',
            'interactive']
        )
        if regex is not None:
            for job in tasks:
                try:
                    # test for over jobs
                    exitCode = '-'
                    if job['container']['meta'] is not None and 'State' in job['container']['meta']:
                        exitCode = Utils.get_execution_status(job['container']['meta']['State']['ExitCode'])

                    tags = ",".join(job['meta']['tags'])
                    # test regex
                    if re.search(regex, str(job['id'])) or \
                       re.search(regex, str(job['meta']['name'])) or \
                       re.search(regex, str(job['meta']['description'])) or \
                       re.search(regex, str(job['user']['id'])) or \
                       re.search(regex, str(job['container']['image'])) or \
                       re.search(regex, tags) or \
                       re.search(regex, exitCode):
                        table_data.append(
                          [
                            str(job['id']),
                            job['meta']['name'],
                            job['meta']['description'][:15],
                            job['user']['id'],
                            job['container']['image'],
                            str(job['status']['secondary']),
                            exitCode,
                            str(job['requirements']['ram']),
                            str(job['requirements']['cpu']),
                            str(job['container']['root']),
                            str(job['command']['interactive'])
                          ]
                        )
                except:
                    print("Error parsing json for job :"+str(job['id']))
        else:
            for job in tasks:
                try:
                    # test for over jobs
                    exitCode = '-'
                    if job['container']['meta'] is not None and 'State' in job['container']['meta']:
                        exitCode = Utils.get_execution_status(job['container']['meta']['State']['ExitCode'])

                    table_data.append(
                        [
                        str(job['id']),
                        job['meta']['name'],
                        job['meta']['description'][:15],
                        job['user']['id'],
                        job['container']['image'],
                        str(job['status']['secondary']),
                        exitCode,
                        str(job['requirements']['ram']), str(job['requirements']['cpu']),
                        str(job['container']['root']),
                        str(job['command']['interactive'])
                        ]
                   )
                except:
                    print("Error parsing json for job :"+str(job['id']))

        return SingleTable(table_data)

    @staticmethod
    def get_job_infos(job_id):

        task = HttpUtils.http_get_request(
            "/api/1.0/task/"+str(job_id),
            Auth.server,
            {'Authorization':'Bearer '+Auth.token},
            Auth.noCert
        )

        return task.json()

    @staticmethod
    def get_project_tables(project):
        # classic infos
        project_info = []
        project_info.append(['id', 'description', 'priority'])
        project_info.append(
            [
                str(project['id']),
                project['description'][:15],
                str(project['prio'])
            ]
        )
        table_info = SingleTable(project_info, "global infos")

        #members infos
        members_infos = []
        members_infos.append(["members"])
        for member in project["members"]:
            members_infos.append([member])

        table_members = SingleTable(members_infos, "members")

        #quota
        quota_infos = []
        quota_infos.append(["ram", "cpu", "time (HH:MM:SS)"])
        quota_infos.append(
            [
                str(project["quota_ram"]),
                str(project["quota_cpu"]),
                str(timedelta(seconds=project['quota_time']))
            ]
        )

        table_quota = SingleTable(quota_infos, "quota")

        # volumes
        data_volumes = []
        if 'volumes' in project:
            data_volumes.append(['name', 'path', 'mount', 'acl'])
            for volume in project['volumes']:
                data_volumes.append([str(volume['name']), str(volume['path']), str(volume['mount']), str(volume['acl'])])

        table_volumes = SingleTable(data_volumes, "volumes")


        return table_info, table_members, table_quota, table_volumes

    @staticmethod
    def get_usage_table(usage):
        # usage infos
        usage_data=[]
        usage_data.append(["date", "ram (Gb)", "cpu", "time (HH:MM:SS)"])
        for date in usage.json():
            date_clear = datetime.strptime(str(date['date']), "%Y_%m_%d").strftime('%d %b %Y')
            usage_data.append([date_clear, str(date['ram']), str(date['cpu']), str(timedelta(seconds=date['time']))])

        table_usage = SingleTable(usage_data, "usage per date")

        return table_usage
