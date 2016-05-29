import logging
import os

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


    def login(self,apikey,login,server,noCert = False):

        data=json.dumps({'user': login, 'apikey': apikey})
        auth = HttpUtils.http_post_request("/api/1.0/authenticate",data,server,{'Content-type': 'application/json','Accept': 'application/json'},noCert)

        if not auth:
            print("Authentication Error!!")
        else:
            Auth.create_auth_file(apikey, login, server, noCert)
        return auth


    def queue_job(self, job_wrapper):
    	
    	log.debug("Starting queue_job for job " + job_wrapper.get_id_tag())
	
	
    def stop_job(self,job):
    	pass
    
    def recover(self,job):
    	pass
