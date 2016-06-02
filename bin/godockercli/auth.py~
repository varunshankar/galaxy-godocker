#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from os.path import expanduser
import os.path
import sys
#import ConfigParser

import requests, json

from godockercli.httputils import HttpUtils

class Auth:
    # static variables
    token = None
    server = None
    login = None
    apikey = None
    noCert = False

    @staticmethod
    def authenticate():
        """authentification method lauched by godocker command"""
        # config location (move in a .ini file)
        config_path = expanduser("~")+"/.godocker_auth"

        # if file doesn't exists, exit
        if not os.path.exists(config_path):
            print("please launch the godlogin command to authenticate")
            return 0
        else:
            # read auth
            auth_infos=json.loads(open(config_path, 'r').readline())
            Auth.server = auth_infos["server"]
            Auth.login = auth_infos["user"]
            Auth.apikey = auth_infos["apikey"]
            Auth.noCert = auth_infos["noCert"]

            data=json.dumps({'user': Auth.login, 'apikey': Auth.apikey})

            res = HttpUtils.http_post_request("/api/1.0/authenticate", data, Auth.server, {'Content-type': 'application/json', 'Accept': 'application/json'}, Auth.noCert)

            Auth.token = res.json()['token'].encode('ascii','ignore').decode('utf-8')

    @staticmethod
    def create_auth_file(apikey, login, server, noCert):

        file_path = expanduser("~")+"/.godocker_auth"

        try:
            #  write the url server with the token
            auth_file = open(file_path, "w")

            # add information in auth file (login, apikey and server name)
            json.dump({'user':login, 'apikey':apikey, 'server':server, 'noCert':noCert}, auth_file)

            # close auth file
            auth_file.close()

        except IOError:
            print("Error I/O")
