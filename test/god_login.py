import json
import inspect

from godockercli.auth import Auth
from godockercli.httputils import HttpUtils

def test_login(apikey,login,server,noCert = False):
    data=json.dumps({'user': login, 'apikey': apikey})
    auth = HttpUtils.http_post_request("/api/1.0/authenticate",data,server,{'Content-type': 'application/json','Accept': 'application/json'},noCert)
    if not auth:
        print("Authentication Error!!")
    else:
        Auth.create_auth_file(apikey, login, server, noCert)
    return auth

auth = test_login("DKZPM1NDE3","gosc","http://cloud-30.genouest.org")
print auth
mem = inspect.getmembers(auth)
for i in mem:
	print i

auth = auth.json()
print "Auth token: " + auth['token']

