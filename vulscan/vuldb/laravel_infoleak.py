# coding:utf-8
import requests

def get_plugin_info():
    plugin_info = {
        "name" : "laravel信息泄露",
        "info" : "laravel信息泄露",
        "level" : "中危",
        "type" : "信息泄露",
        "author" : "zinc",
        "url": "",
        "keyword" : "server:web",
        "source" : 1,
    }
    return plugin_info

def check(ip, port, timeout):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept-Encoding': 'gzip'
        }
        url = 'http://%s:%d/' % (ip, port)
        r = requests.post(url, headers=headers)
        if 'Environment & details' in r.content:
            #print u'信息泄露'
            return u"信息泄露"
    except Exception as e:
        print e

if __name__ == '__main__':
    check('127.0.0.1', 80, 3)