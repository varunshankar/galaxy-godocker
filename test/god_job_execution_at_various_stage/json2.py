t = {u'status': {u'date_over': None, u'reason': None, u'exitcode': None, u'primary': u'pending', u'secondary': None}, u'container': {u'stats': None, u'network': True, u'image': u'centos:latest', u'ports': [], u'meta': None, u'volumes': [{u'path': u'/omaha-beach/galaxy/code/galaxy', u'mount': u'/omaha-beach/galaxy/code/galaxy', u'name': u'galaxy', u'acl': u'rw'}], u'root': False, u'id': None}, u'parent_task_id': None, u'meta': {u'description': u'example job', u'name': u'Count', u'tags': [u'galaxy', u'Count1']}, u'command': {u'cmd': u'#!/bin/bash\ncd /omaha-beach/galaxy/code/galaxy/database/job_working_directory/000/17\n/omaha-beach/galaxy/code/galaxy/database/job_working_directory/000/17/tool_script.sh', u'interactive': False}, u'user': {u'sgids': [], u'uid': 1000, u'id': u'gosc', u'project': u'galaxy', u'gid': 1000, u'email': None}, u'date': 1465933782.0, u'requirements': {u'tasks': [], u'ram': 2, u'project_quota_cpu': 0, u'label': [], u'user_quota_cpu': 0, u'project_quota_ram': 0, u'user_quota_ram': 0, u'project_quota_time': 0, u'array': {u'nb_tasks_over': None, u'tasks': [], u'values': None, u'task_id': None, u'nb_tasks': None}, u'user_quota_time': 0, u'tmpstorage': None, u'cpu': 1}, u'_id': {u'$oid': u'57605fd69896051247316edc'}, u'id': 72, u'notify': {u'email': False}}

print t.keys()
path = None
print t['status']['primary']
for vol in t['container']['volumes']:
    if vol['name']=="go-docker":
        path = vol['path']
if path:
    print t['container']['volumes'][1]

##primary -> pending
##exitcode -> None
##secondary -> None
