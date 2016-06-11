import json
import inspect
import time
from datetime import datetime

from godockercli.auth import Auth
from godockercli.httputils import HttpUtils
from godockercli.utils import Utils

def test_login(apikey,login,server,noCert = False):
    data=json.dumps({'user': login, 'apikey': apikey})
    auth = HttpUtils.http_post_request("/api/1.0/authenticate",data,server,{'Content-type': 'application/json','Accept': 'application/json'},noCert)
    print "Auth: "+ str(auth) + "\n"
    print "Auth code: " + str(auth.status_code) + "\n"
    if not auth:
        print("Authentication Error!!")
    else:
        Auth.create_auth_file(apikey, login, server, noCert)
        auth = auth.json()['token']
        print "Token : "+ str(auth) + "\n"
    return auth

def post_task(job,auth):
    #Sumbit job to godocker
    Auth.authenticate()
    print("\n JOB POST TASK TO BE EXECUTED \n")
    print("GODOCKER task: "+json.dumps(job))
    result = HttpUtils.http_post_request("/api/1.0/task",json.dumps(job),Auth.server,{'Authorization':'Bearer '+Auth.token,'Content-type': 'application/json', 'Accept':'application/json'},Auth.noCert)
    get_structure(result)
    print result.text
    print("Response from godocker: "+ str(result.json()['msg']) + " ID: " + int(result.json()['id']))
    print("END OF JOB POST TASK\n")
    return result

def get_structure(obj):
    print("\n STRUCTURE \n")
    memb = inspect.getmembers(obj)
    for i in memb:
        print(i)
    print("\n END OF STRUCTURE \n")
    return

def get_job_template():
    print("\n INSIDE JOB CREATION TEMPLATE \n")
    docker_image = "busybox:ubuntu-14.04"
    docker_tags = "test,job1"
    docker_cpu = 1
    docker_ram = 2
    Auth.authenticate()
    dt = datetime.now()
    #god_job_cmd = "#!/bin/bash\n"+"cd "+job_wrapper.working_directory+"\n"+job_wrapper.runner_command_line
    command = "#!/bin/bash\n"+"echo \"command executing helloworld\""
    print("\n Command: "+command)
    try:
        user_infos = Utils.get_userInfos(Auth.login)
    except:
        user_infos = {'id':Auth.login, 'uid':Auth.login, 'gid':Auth.login}

    job = {
  "id": "string",
  "notify": {
    "email": True
  },
  "user": {
    "email": "varunshankar@gmail.com",
    "id": "gosc",
    "project": "test project",
    "uid": "gosc",
    "gid": "gosc",
    "sgids": [
      "gosc"
    ]
  },
  "meta": {
    "name": "gosc",
    "description": "",
    "tags": [
      "gosc","test","job"
    ]
  },
  "requirements": {
    "cpu": 1,
    "ram": 2,
    "tasks": None,
    "array": {
      "values": None
    },
    "label": [
      None
    ]
  },
  "container": {
    "id": None,
    "image": "busybox:ubuntu-14.04",
    "meta": {},
    "network": True,
    "root": None,
    "volumes": [
      {
        "name": None,
        "acl": None,
        "path": None,
        "mount": None
      }
    ]
  },
  "command": {
    "interactive": False,
    "cmd": command
  },
  "status": {
    "primary": None,
    "secondary": None,
    "reason": None,
    "exitcode": 0,
    "duration": 0,
    "date_running": 0,
    "date_over": 0
  }
    }
    '''
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
    '''
    print("JOB TEMPLATE: ")
    print(job)
    print("END OF JOB TEMPLATE \n")
    return job


def create(name, description="", tags="", project="galaxy", cpu=1, ram=1, image="", external_image=None, script="", interactive=False, root=False, volume="", array=None, login="", label="", parent="", tmp_storage="", env=None, cmd=None):
    """ create a new job """

    Auth.authenticate()

    # manage volumes
    volumes=[]
    labels=[]

    # command
    command = ''
    if script:
        f = open(script)
        command = f.read()
    if cmd:
        command = cmd

    tags_tab = ['galaxy','godocker_test_tool']
    # manage depends
    tasks_depends = []
    if parent:
        print "\nINSIDE PARENT\n"
        tasks_depends = parent.split(",")


    #user_infos = Utils.get_userInfos(login)

    dt = datetime.now()

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
            'cpu': int(cpu),
            # In Gb
            'ram': int(ram),
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

    print job
    result_submit = HttpUtils.http_post_request(
        "/api/1.0/task", json.dumps(job),
        Auth.server,
        {'Authorization':'Bearer '+Auth.token, 'Content-type': 'application/json', 'Accept':'application/json'},
        Auth.noCert
    )
    result_json = result_submit.json()
    print(str(result_submit.json()['msg'])+". Job id is "+str(result_json['id']))


if __name__ == "__main__":
   auth = test_login("DKZPM1NDE3","gosc","http://cloud-30.genouest.org")
   #job = get_job_template()
   #print post_task(job,auth)
   #godjob create -n job_name -d "example job" -i centos:latest -s script_to_execute.sh -v home
   create(name="test_gettask",description="example job",image="centos:latest",script="demo.sh")#,volume="home")
   


