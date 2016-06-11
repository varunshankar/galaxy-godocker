import logging
import os
import json
import time
import inspect
from datetime import datetime

from galaxy import model
from galaxy.jobs.runners import AsynchronousJobState, AsynchronousJobRunner

from godockercli.auth import Auth
from godockercli.httputils import HttpUtils
from godockercli.utils import Utils

log = logging.getLogger(__name__)

__all__ = ['GodockerJobRunner']

class GodockerJobRunner(AsynchronousJobRunner):
    """
	Job runner backed by a finite pool of worker threads. FIFO scheduling
    """
    runner_name = "GodockerJobRunner"
    
    def __init__(self, app, nworkers, **kwargs):

    	log.debug("Loading app %s",app)
    	self.auth = None
        #self.server = "https://godocker.genouest.org" #"https://docker-ui/genouest.org"
    	runner_param_specs = dict(
    		godocker_master = dict(map = str),
    		user = dict(map = str),
    		key = dict(map = str)
        )
        if 'runner_param_specs' not in kwargs:
        	kwargs['runner_param_specs'] = dict()
        
        kwargs['runner_param_specs'].update(runner_param_specs)
        super(GodockerJobRunner, self).__init__(app, nworkers, **kwargs)
        
        log.debug("runner_params before godocker login: \n")
        log.debug(self.runner_params)
        # godocker API login call to be done here
        self.auth = self.login(self.runner_params["key"],self.runner_params["user"],self.runner_params["godocker_master"])
        log.debug("runner_params after godocker login: \n")
        log.debug(self.runner_params)
        
        if not self.auth:
            log.debug("Authentication failure!! Job cannot be started")
        else:
            """ Following methods starts threads.
                threading.Thread(name,target) invokes methods monitor() and run_next()
            """
            self._init_monitor_thread()
            self._init_worker_threads()


    def queue_job(self, job_wrapper):

    	#job_name = self.get_unique_job_name(job_wrapper)
        if not self.prepare_job(job_wrapper, include_metadata=False, include_work_dir_outputs=False):
            return

        job_destination = job_wrapper.job_destination
        log.debug("JOB_WRAPPER")
        #log.warn(job_wrapper)
        #self.get_structure(job_wrapper)
        #self.get_structure(job_wrapper.tool)
        #log.debug(job_wrapper.tool.name)
        log.debug("END OF JOB_WRAPPER \n")
        job_id = self.post_task(job_wrapper)
        log.debug("Job response from GoDocker")
        log.debug(job_id)
        if not job_id:
            log.debug("Job creation faliure!! No Response from GoDocker")
        else:
            log.debug("Starting queue_job for job " + job_id)
            ajs = AsynchronousJobState(files_dir = job_wrapper.working_directory,job_wrapper = job_wrapper,job_id = job_id,job_destination = job_destination)
            self.monitor_queue.put(ajs)
        return None


    def check_watched_item(self, job_state):
        # Get the job current status from godocker using jobid
        job_status = self.get_task_status(job_state.job_id)
        print("\n JOB STATUS FROM GODOCKER \n")
        print job
        #self.get_structure(job)
        print("\nEND OF JOB STATUS\n")
        if job_status.primary == "over":
            job_state.running = False
            self.mark_as_failed(job_state)
        
        return job_state
        
        # Possible Job states: state["secondary"]= suspended | running | kill requested | suspend requested
        #Update the job status to galaxy here
        

    def stop_job(self,job):
    	#Call the godocker API here
        #Update the status to galaxy
        return
    
    def recover(self,job):
    	pass
	
    #Helper functions
    def get_unique_job_name(self, job_wrapper):
        return "god-" + job_wrapper.get_id_tag()

    #GoDocker API helper functions

    def login(self,apikey,login,server,noCert = False):
        log.debug("LOGIN TASK TO BE EXECUTED \n")
        log.warn("GODOCKER LOGIN: "+str(login)+":"+str(apikey))
        data=json.dumps({'user': login, 'apikey': apikey})
        auth = HttpUtils.http_post_request("/api/1.0/authenticate",data,server,{'Content-type': 'application/json','Accept': 'application/json'},"False")
        self.get_structure(auth)
        
        if not auth:
            print("Authentication Error!!")
        else:
            Auth.create_auth_file(apikey, login, server, noCert)
            auth = auth.json()['token']
            log.debug(auth)
        log.debug("END OF LOGIN TASK \n")
        return auth


    def post_task(self,job_wrapper):
        #Sumbit job to godocker
        Auth.authenticate()
        log.debug("\n INSIDE JOB CREATION TEMPLATE \n")
        job_destination = job_wrapper.job_destination
        docker_repo = job_destination.params["docker_repo_override"]
        docker_owner = job_destination.params["docker_owner_override"]
        docker_image = job_destination.params["docker_default_container_id"]
        docker_tags = job_destination.params["docker_tag_override"]
        docker_cpu = job_destination.params["docker_cpu"]
        docker_ram = job_destination.params["docker_memory"]

        
        #volume = "home"
        #docker_image="centos:latest"
        volumes=[]
        labels=[]
        #tags
        #tags_tab = docker_tags.split(",")
        tags_tab = ['galaxy',job_wrapper.tool.id]

        # manage depends
        tasks_depends = []
        name = job_wrapper.tool.name
        description= "example job"
        array = None
        project = "galaxy"
        
        dt = datetime.now()
        god_job_cmd = "#!/bin/bash\n"+"cd "+job_wrapper.working_directory+"\n"+job_wrapper.runner_command_line
        command = god_job_cmd
        log.debug("\n Command: ")
        log.debug(command)

        job = {
        'user' : {
            #'id' : user_infos['id'],
            #'uid' : user_infos['uid'],
            #'gid' : user_infos['gid'],
            'project' : project
        },
        'date': time.mktime(dt.timetuple()),
        'meta': {
            'name': name,
            'description': description,
            'tags': tags_tab
        },
        'requirements': {
            'cpu': int(docker_cpu), #cpu,
            'ram': int(docker_ram), #ram,
            'array': { 'values': array},
            'label': labels,
	    'tasks': tasks_depends,
            'tmpstorage': None
        },
        'container': {
            'image': str(docker_image),
            'volumes': volumes,
            'network': True,
            'id': None,
            'meta': None,
            'stats': None,
            'ports': [],
            'root': False #root
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
        log.debug("JOB TEMPLATE: ")
        log.debug(job)
        log.debug("END OF JOB TEMPLATE \n")
        log.debug("\n JOB POST TASK TO BE EXECUTED \n")
        result = HttpUtils.http_post_request(
           "/api/1.0/task", json.dumps(job),
           Auth.server,
           {'Authorization':'Bearer '+Auth.token, 'Content-type': 'application/json', 'Accept':'application/json'},
           Auth.noCert
        )
        #self.get_structure(result)
        log.debug(result.text)
        log.debug("Response from godocker: "+ str(result.json()['msg']) + " ID: " + str(result.json()['id']))
        log.debug("END OF JOB POST TASK\n")
        return str(result.json()['id'])

    def get_task(self,job_id):
        #Get job details
        job = False
        if Auth.authenticate():
            result = HttpUtils.http_get_request("/api/1.0/task/"+str(job_id),Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
            job = result.json()
        return job

    def task_suspend(self,job_id):
        #Suspend actively running job
        job = False
        if Auth.authenticate():
            result = HttpUtils.http_get_request("/api/1.0/task/"+str(job_id)+"/suspend",Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
            job = result.json()
        return job

    def get_task_status(self,job_id):
        #Get job status
        job = False
        if Auth.authenticate():
            result = HttpUtils.http_get_request("/api/1.0/task/"+str(job_id)+"/status",Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
            job = result.json()
        return job

    def delete_task(self,job_id):
        #Delete a job 
        job = False
        if Auth.authenticate():
            result = HttpUtils.http_delete_request("/api/1.0/task/"+str(job_id),Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
            job = result.json()
        return job

    def get_structure(self,obj):
        log.debug("\n STRUCTURE \n")
        memb = inspect.getmembers(obj)
        for i in memb:
            log.debug(i)
        log.debug("\n END OF STRUCTURE \n")
        return
    
    def get_all_members_recursive(self,obj):
        print inspect.getmembers(obj)
        for i in inspect.getmembers(obj):
            if "object" in str(i[1]) or "instance" in str(i[1]):
                self.get_all_members_recursive(i[1])

