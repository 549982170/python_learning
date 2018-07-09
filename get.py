#!user/bin/python
# -*- coding: utf-8 -*-

import requests
import json



url = 'http://localhost:5000'

query_args = {"username": "yzw", "pwd": "123456", "type": "2"}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(query_args), headers=headers)

print r.json()