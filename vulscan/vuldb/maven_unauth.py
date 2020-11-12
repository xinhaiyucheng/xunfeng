#!/usr/bin/eny python
#coding=utf-8
import requests

def get_plugin_info():  # 插件描述信息
    plugin_info = {
        "name": "Maven仓库信息泄露",
        "info": "Sonatype nexus repository manager开源组件未限制访问权限，可访问查看Maven库资源。",
        "level": "低危",
        "type": "信息泄露",
        "author": "carry_me",
        "url": "",
        "keyword": "tag:maven",  # 推荐搜索关键字
    }
    return plugin_info

def req(url):
    headers = {
        'Connection': 'close',
    }
    r = requests.get(url, headers=headers, timeout=3, verify=False)
    if 'Repository Manager' in r.content:
        return True
    return False

def check(ip, port, timeout):
    if port == 443:
        url = 'https://' + ip + '/#browse/welcome'
    else:
        url = 'http://' + ip + ':' + str(port) + '/#browse/welcome'

    try:
        if req(url):
            return u"信息泄露"
    except Exception as e:
        print e

if __name__ == '__main__':
    print check('121.12.87.129',8765, 3)