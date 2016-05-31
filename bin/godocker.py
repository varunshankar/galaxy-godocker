import logging
import os
import json

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
        self.server = "https://godocker.genouest.org" #"https://docker-ui/genouest.org"
    	runner_param_specs = dict(
    		godocker_master = dict(map = str),
    		job_name = dict(map = str),
    		tags = dict(map = str),
    		desc = dict(map = str),
    		cpu = dict(map = int,valid = lambda x: int > 0,default = 1),
    		ram = dict(map = int,valid = lambda x: int > 0,default = 1),
    		image = dict(map = str), #"centos:latest","rastasheep/ubuntu-sshd","osallou/dockernode"
    		user = dict(map = str),
    		apikey = dict(map = str)
        )
        if 'runner_param_specs' not in kwargs:
        	kwargs['runner_param_specs'] = dict()
        
        kwargs['runner_param_specs'].update(runner_param_specs)
        
        # godocker API login call to be done here
        self.auth = self.login(self.runner_params["apikey"],self.runner_params["user"],self.server)

        if not self.auth:
            log.debug("Authentication failure!! Job cannot be started")
        else:
            super(GodockerJobRunner, self).__init__(app, nworkers, **kwargs)
            """ Following methods starts threads.
                threading.Thread(name,target) invokes methods monitor() and run_next()
            """
            self._init_monitor_thread()
            self._init_worker_threads()


    def queue_job(self, job_wrapper):

    	job_name = self.get_unique_job_name(job_wrapper)
    	log.debug("Starting queue_job for job " + job_name)
        if not self.prepare_job(job_wrapper, include_metadata=False, include_work_dir_outputs=False):
            return
        job_destination = job_wrapper.job_destination

        # Create the Json object and call the godocker API here

        ajs = AsynchronousJobState(files_dir = job_wrapper.working_directory,job_wrapper = job_wrapper,job_id = job_name,job_destination = job_destination)
        self.monitor_queue.put(ajs)
        

    def check_watched_item(self, job_state):
        # Get the job current status from godocker using jobid
        job = self.get_task(job_state.job_id)
        
        #Update the job status to galaxy here
        

    def stop_job(self,job):
    	pass
    
    def recover(self,job):
    	pass
	
    #Helper functions
    def get_unique_job_name(self, job_wrapper):
        return "god-" + job_wrapper.get_id_tag()


    #GoDocker API helper functions

    def login(self,apikey,login,server,noCert = False):

        data=json.dumps({'user': login, 'apikey': apikey})
        auth = HttpUtils.http_post_request("/api/1.0/authenticate",data,server,{'Content-type': 'application/json','Accept': 'application/json'},noCert)

        if not auth:
            print("Authentication Error!!")
        else:
            Auth.create_auth_file(apikey, login, server, noCert)
        return auth


    def post_task(self,job):

        Auth.authenticate()
        
        # TODO fill the job template. 
        #Job template
        """
        job = {
        'user' : {
            'id' : user_infos['id'],
            'uid' : user_infos['uid'],
            'gid' : user_infos['gid'],
            'project' : project
        },
        'date': time.mktime(dt.timetuple()),
        'meta': {
            'name': name,
            'description': description,
            'tags': tags_tab
        },
        'requirements': {
            'cpu': cpu,
            # In Gb
            'ram': ram,
            'array': { 'values': array},
            'label': labels,
	    'tasks': tasks_depends,
            'tmpstorage': None
        },
        'container': {
            'image': str(image),
            'volumes': volumes,
            'network': True,
            'id': None,
            'meta': None,
            'stats': None,
            'ports': [],
            'root': root
        },
        'command': {
            'interactive': interactive,
            'cmd': command,
        },
        'status': {
            'primary': None,
            'secondary': None
        }

      }
        """
        result = HttpUtils.http_post_request("/api/1.0/task",json.dumps(job),Auth.server,{'Authorization':'Bearer '+Auth.token,'Content-type': 'application/json', 'Accept':'application/json'},Auth.noCert)
        log.debug("Response from godocker: "+ str(result.json()['msg']) + " ID: " + int(result.json()['id']))

    def get_task(self,job_id):
        #Get job details
        Auth.authenticate()
        result = HttpUtils.http_get_request("/api/1.0/task/"+str(job_id),Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
        job=result.json()
        return job

