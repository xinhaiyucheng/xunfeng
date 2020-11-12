#!/usr/bin/env python
#coding=utf-8
import requests

def get_plugin_info():
    plugin_info = {
        "name": "Springboot actuator未授权访问",
        "info": "WebLogic 特定版本存在 命令执行漏洞，未授权 的攻击者可通过发送精心构造的恶意请求，触发反序列化，造成远程命令执行，从而获取服务器权限。",
        "level": "低危",
        "type": "未授权访问",
        "author": "zinc",
        "url": "",
        "keyword": "server:web",
        "source": 1
    }
    return plugin_info

def req(url):
    headers = {
        'Connection': 'close',
    }
    r = requests.get(url, headers=headers, timeout=3, verify=False)
    if 'profiles' in r.content:
        return True
    return False

def check(ip, port, timeout):
    port = str(port)
    path = '/env'
    if port == '80':
        url = 'http://%s%s' % (ip, path)
    elif port == '443':
        url = 'https://%s%s' % (ip, path)
    else:
        url = 'http://%s:%s%s' % (ip, port, path)

    try:
        if req(url):
            print u'未授权访问'
            return u'未授权访问'

    except Exception as e:
        pass

if __name__ == '__main__':
    check('43.240.130.72', 8888, 3)
