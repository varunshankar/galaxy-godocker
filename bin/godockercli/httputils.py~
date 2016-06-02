#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from os.path import expanduser
import os.path
import sys
import re

import requests, json

class HttpUtils:
    @staticmethod
    def http_post_request(query, data, server, header, noCert):
        """ post request with query """

        #remove warnings if using --no-certificate
        requests.packages.urllib3.disable_warnings()

        verify_ssl = not noCert

        try:
            url=server+query
            res = requests.post(url, data, headers=header, verify=verify_ssl)

        except requests.exceptions.ConnectionError as e:
            print('A Connection error occurred:', e)

            if re.search("SSL3_GET_SERVER_CERTIFICATE", str(e)):
                print("Use the --no-certificate option if you trust the remote godocker server certificate.")

            sys.exit(1)

        except requests.exceptions.HTTPError as e:
            print('A HTTP error occurred:', e)
            sys.exit(1)

        HttpUtils.test_status_code(res)

        return res

    @staticmethod
    def http_get_request(query, server, header, noCert):
        """ get request with query, server and header required """

        #remove warnings if using --no-certificate
        requests.packages.urllib3.disable_warnings()

        verify_ssl = not noCert

        try:
            url=server+query
            res = requests.get(url, headers=header, verify=verify_ssl)

        except requests.exceptions.ConnectionError as e:
            print('A Connection error occurred:', e)
            sys.exit(1)

        except requests.exceptions.HTTPError as e:
            print('A HTTP error occurred:', e)
            sys.exit(1)

        HttpUtils.test_status_code(res)

        return res

    @staticmethod
    def http_delete_request(query, server, header, noCert):
        """ delete request with query, server and header required """

        #remove warnings if using --no-certificate
        requests.packages.urllib3.disable_warnings()

        verify_ssl = not noCert

        try:
            url=server+query
            res = requests.delete(url, headers=header, verify=verify_ssl)

        except requests.exceptions.ConnectionError as e:
            print('A Connection error occurred:', e)
            sys.exit(1)

        except requests.exceptions.HTTPError as e:
            print('A HTTP error occurred:', e)
            sys.exit(1)

        HttpUtils.test_status_code(res)

        return res

    @staticmethod
    def http_put_request(query, data, server, header, noCert):
        """ put request with query """

        #remove warnings if using --no-certificate
        requests.packages.urllib3.disable_warnings()

        verify_ssl = not noCert

        try:
            url=server+query
            res = requests.put(url, data, headers=header, verify=verify_ssl)

        except requests.exceptions.ConnectionError as e:
            print('A Connection error occurred:', e)
            sys.exit(1)

        except requests.exceptions.HTTPError as e:
            print('A HTTP error occurred:', e)
            sys.exit(1)

        HttpUtils.test_status_code(res)

        return res

    @staticmethod
    def test_status_code(httpresult):
        """ exit if status code is 401 or 403 or 404 """

        if httpresult.status_code == 401:
            print('Unauthorized : this server could not verify that you are authorized to access the document you requested.')
            sys.exit(0)

        if httpresult.status_code == 403:
            print('Forbidden : Access was denied to this resource. Not authorized to access this resource.')
            sys.exit(0)

        if httpresult.status_code == 404:
            print('Not Found : The resource could not be found.')
            sys.exit(0)
