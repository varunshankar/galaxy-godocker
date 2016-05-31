import json
import inspect

from godockercli.auth import Auth
from godockercli.httputils import HttpUtils

def post_task(job):
    Auth.authenticate()
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
    print "token: "+ Auth.token
    print "Server: "+ Auth.server
    print "User: "+ Auth.login
    print "Apikey: "+ Auth.apikey
    print "Cer: "+ str(Auth.noCert)
    #result = HttpUtils.http_post_request("/api/1.0/task",json.dumps(job),Auth.server,{'Authorization':'Bearer '+Auth.token,'Content-type': 'application/json', 'Accept':'application/json'},Auth.noCert)
    #log.debug("Response from godocker: "+ str(result.json()['msg']) + " ID: " + int(result.json()['id']))

if __name__ == "__main__":
    post_task("None")
