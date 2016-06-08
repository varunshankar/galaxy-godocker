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
    		godocker_master = dict(map = str), #Where is this used? Find out!
    		#name = dict(map = str),
    		#tags = dict(map = str,default = ""),
    		#cpu = dict(map = int,valid = lambda x: int > 0,default = 1),
    		#ram = dict(map = int,valid = lambda x: int > 0,default = 1),
    		#image = dict(map = str), #"centos:latest","rastasheep/ubuntu-sshd","osallou/dockernode"
    		user = dict(map = str),
    		key = dict(map = str),
                #project = dict(map = str,default = "default"),
                #description = dict(map = str,default = ""),
                #array = dict(map = str,valid = lambda x: x in ("start","stop","step"),default=None),
                #parent = dict(map = str,default = ""),
                #external_image = dict(map = bool,default = False),
                #volume = dict(map = str,default = ""),
                #root = dict(map = bool,default = False),
                #interactive = dict(map = bool,default = False)
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
        log.warn(job_wrapper)
        self.get_structure(job_wrapper)
        log.debug("END OF JOB_WRAPPER \n")
        # Create the Json object and call the godocker API here
        job = self.get_job_template(job_wrapper)
        if not job:
            log.debug("Job creation failure!! Job cannot be started")
        else:
            job_id = self.post_task(job)
            log.debug("Job response from GoDocker")
            log.debug(job_id)
            if not job_name:
                log.debug("Job creation faliure!! No Response from GoDocker")
            else:
                log.debug("Starting queue_job for job " + job_id)
                ajs = AsynchronousJobState(files_dir = job_wrapper.working_directory,job_wrapper = job_wrapper,job_id = job_id,job_destination = job_destination)
                self.monitor_queue.put(ajs)
        
        return None


    def check_watched_item(self, job_state):
        # Get the job current status from godocker using jobid
        #job = self.get_task(job_state.job_id)
        job_state.running = False
        self.mark_as_failed(job_state)
        return None
        
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

    def get_job_template(self, job_wrapper):
        log.debug("\n INSIDE JOB CREATION TEMPLATE \n")
        #project = self.runner_params["project"]
        #name = self.runner_params["name"]
        #description = self.runner_params["description"]
        #tags = self.runner_params["tags"]
        #cpu = self.runner_params["cpu"]
        #ram = self.runner_params["ram"]
        #array = self.runner_params["array"]
        #parent = self.runner_params["parent"]
        #image = self.runner_params["image"]
        #external_image = self.runner_params["external_image"]
        #volume = self.runner_params["volume"]
        #root = self.runner_params["root"]
        #interactive = self.runner_params["interactive"]
        #cmd = self.runner_params["cmd"]
        #script = self.runner_params["script"]
        job_destination = job_wrapper.job_destination
        docker_repo = job_destination.params["docker_repo_override"]
        docker_owner = job_destination.params["docker_owner_override"]
        #docker_image = job_destination.params["docker_image_override"]
        docker_image = job_destination.params["docker_default_container_id"]
        docker_tags = job_destination.params["docker_tag_override"]
        docker_cpu = job_destination.params["docker_cpu"]
        docker_ram = job_destination.params["docker_memory"]
        Auth.authenticate()

        # manage volumes
        '''
        HTTP POST url:"/api/1.0/config"
        '''
        '''
        volumes=[]
        for volume in list(volume):
            acl = Utils.get_acl_for_volume(volume)
            volumes.append({'name': volume, 'acl': str(acl)})
        
        # manage constraints
        labels = []
        available_labels = Utils.get_contraint_labels()
        for user_label in list(label):
            if user_label not in available_labels:
                print("Constraint '"+user_label+" does not exist. Please choose in the list below:")
                for available_label in available_labels:
                    print(" "+available_label)
                return False
            else:
                labels.append(user_label)

        # test image selection
        if not image in Utils.get_docker_images_url() and not external_image:
            print("Wrong image url selected. Please launch 'godimage list' to check your image url or use the --external_image.")
            return False

        if (not script and not cmd and not interactive):
            print("You must use either --script/--cmd or --interactive option")
            return False

        if interactive and image not in Utils.get_docker_images_url_interactive():
            print("You are not allowed to use this image with interactive mode. Please launch 'godimage list' to check your image url")
            return False
        
        # command
        #Not sure of this. How does a tool program executed by this, as galaxy supports multiple programming languages for tool creation
        command = ''
        if script:
            command = script.read()
        if cmd:
            command = cmd

        if env is not None and env:
            template_vars = {}
            for envvar in env:
                if envvar not in os.environ:
                    print("Environment variable %s is not defined" % envvar)
                    return False
                template_vars[envvar] = os.environ[envvar]
            command = Template(command).safe_substitute(template_vars)
        

        #tags
        #tags_tab = tags.split(",")

        # manage depends
        tasks_depends = []
        if parent:
            tasks_depends = parent.split(",")
        '''
        dt = datetime.now()
        god_job_cmd = "#!/bin/bash\n"+"cd "+job_wrapper.working_directory+"\n"+job_wrapper.runner_command_line
        command = god_job_cmd
        log.debug("\n Command: ")
        log.debug(command)
        try:
            user_infos = Utils.get_userInfos(Auth.login)
        except:
            user_infos = {'id':Auth.login, 'uid':Auth.login, 'gid':Auth.login}
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
        log.debug("JOB TEMPLATE: ")
        log.debug(job)
        log.debug("END OF JOB TEMPLATE \n")
        return job


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


    def post_task(self,job):
        #Sumbit job to godocker
        Auth.authenticate()
        log.debug("\n JOB POST TASK TO BE EXECUTED \n")
        log.debug("GODOCKER task: "+json.dumps(job))
        result = HttpUtils.http_post_request("/api/1.0/task",json.dumps(job),Auth.server,{'Authorization':'Bearer '+self.auth,'Content-type': 'application/json', 'Accept':'application/json'},Auth.noCert)
        self.get_structure(result)
        log.debug(result.text)
        log.debug("Response from godocker: "+ str(result.json()['msg']) + " ID: " + int(result.json()['id']))
        log.debug("END OF JOB POST TASK\n")
        return result

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

    


