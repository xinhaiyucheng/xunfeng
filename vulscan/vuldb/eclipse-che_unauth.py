#!/usr/bin/eny python
#coding=utf-8
import requests

def get_plugin_info():  # 插件描述信息
    plugin_info = {
        "name": "Eclipse Che 未授权访问",
        "info": "导致workspace信息泄露，可查看ssh keyd等敏感信息。",
        "level": "低危",
        "type": "未授权访问",
        "author": "carry_me",
        "url": "",
        "keyword": "tag:eclipse-che",  # 推荐搜索关键字
    }
    return plugin_info

def req(url):
    headers = {
        'Connection': 'close',
    }
    r = requests.get(url, headers=headers, timeout=3, verify=False)
    if 'Eclipse Che' in r.content:
        return True
    return False

def check(ip, port, timeout):
    target = ip + ':' + str(port)
    url = 'http://' + target + '/dashboard/'
    try:
        if req(url):
            return u'未授权访问'
    except Exception as e:
        print e
        return False

if __name__ == '__main__':
    print check('101.89.92.181', 8080, 3)