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
	
		runner_param_specs = dict(
			godocker_master = dict(map = str,default = os.environ.get('godocker_master', None)),
			job_name = dict(map = str),
			cpu = dict(map = int,valid = lambda x: int > 0,default = 1),
			ram = dict(map = int,valid = lambda x: int > 0,default = 1),
			image = dict(map = str,valid = lambda x: x in ("centos:latest","rastasheep/ubuntu-sshd","osallou/dockernode"))
        )
        if 'runner_param_specs' not in kwargs:
			kwargs['runner_param_specs'] = dict()

		kwargs['runner_param_specs'].update(runner_param_specs)

		super(GodockerJobRunner, self).__init__(app, nworkers, **kwargs)
		""" Following methods starts threads.
			threading.Thread(name,target) invokes methods monitor() and run_next() 
		"""
		self._init_monitor_thread()
        self._init_worker_threads()

    def queue_job(self, job_wrapper):

        log.debug("Starting queue_job for job " + job_wrapper.get_id_tag())
		
		

	def stop_job(self,job):
		pass

	def recover(self,job):
		pass
