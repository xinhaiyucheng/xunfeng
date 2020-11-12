#!/usr/bin/env python
#coding=utf-8
import requests

def get_plugin_info():  # 插件描述信息
    plugin_info = {
        "name": "Swagger-ui信息泄露",
        "info": "导致开发接口信息泄露，可查看接口请求方式、参数等信息",
        "level": "低危",
        "type": "信息泄露",
        "author": "carry_me",
        "url": "",
        "keyword": "tag:swagger-ui",  # 推荐搜索关键字
    }
    return plugin_info

def req(url):
    headers = {
        'Connection': 'close',
    }
    r = requests.get(url, headers=headers, timeout=3, verify=False)
    if 'Swagger UI' in r.content:
        return True
    return False

def req2(url):
    headers = {
        'Connection': 'close',
    }
    r = requests.get(url, headers=headers, timeout=3, verify=False)
    if 'apisSorter' in r.content:
        return True
    return False

def check(ip, port, timeout):
    port = str(port)
    if port == '443':
        url = 'https://' + ip + '/swagger-ui.html'
    else:
        url = 'http://' + ip + ':' + port + '/swagger-ui.html'
    try:
        if req(url):
            url = 'http://' + ip + ':' + port + '/swagger-resources/configuration/ui'
            if req2(url):
                return u"信息泄露"
        print 'No'
    except Exception as e:
        print e

if __name__ == '__main__':
    print check('183.11.223.2',8901, 3)