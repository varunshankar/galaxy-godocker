import json
import inspect
import logging
import time
from datetime import datetime

log = logging.getLogger(__name__)

from godockercli.auth import Auth
from godockercli.httputils import HttpUtils
from godockercli.utils import Utils

def get_job_template(job_wrapper):
        #job_destination = job_wrapper.job_destination
        docker_repo = "myprog" #job_destination.params["docker_repo_override"]
        docker_owner = "bioshark" #job_destination.params["docker_owner_override"]
        #docker_image = job_destination.params["docker_image_override"]
        docker_image = "centos:latest" #job_destination.params["docker_default_container_id"]
        docker_tags = "test,job" #job_destination.params["docker_tag_override"]
        docker_cpu = 1 #job_destination.params["docker_cpu"]
        docker_ram = 2 #job_destination.params["docker_memory"]
        Auth.authenticate()

        dt = datetime.now()
        god_job_cmd = "#!/bin/bash\n"+"cd"+"job_wrapper.working_directory"+"\n"+"job_wrapper.runner_command_line"
        command = god_job_cmd
        log.debug("Command: ")
        log.debug(command)
        user_infos = Utils.get_userInfos(Auth.login)
        job = {
        'user' : {
            'id' : user_infos['id'],
            'uid' : user_infos['uid'],
            'gid' : user_infos['gid'],
            'project' : "default"
        },
        'date': time.mktime(dt.timetuple()),
        'meta': {
            'name': "testjob", #name,
            'description': "", #description,
            'tags': docker_tags #tags_tab
        },
        'requirements': {
            'cpu': docker_cpu, #cpu,
            'ram': docker_ram, #ram,
            'array': None, #{ 'values': array},
            'label': None, #labels,
	        'tasks': None, #tasks_depends,
            'tmpstorage': None
        },
        'container': {
            'image': str(docker_image),
            'volumes': "", #volumes,
            'network': True,
            'id': None,
            'meta': None,
            'stats': None,
            'ports': [],
            'root': None #root
        },
        'command': {
            'interactive': False,
            'cmd': command,
        },
        'status': {
            'primary': None,
            'secondary': None
            }
        }
        return job

def post_task(job):
        #Sumbit job to godocker
        Auth.authenticate()
        result = HttpUtils.http_post_request("/api/1.0/task",json.dumps(job),Auth.server,{'Authorization':'Bearer '+Auth.token,'Content-type': 'application/json', 'Accept':'application/json'},Auth.noCert)
        log.debug("Response from godocker: "+ str(result.json()['msg']) + " ID: " + int(result.json()['id']))
        return result

job_wrapper = None
job = get_job_template(job_wrapper)
job_id = post_task(job)
print job_id