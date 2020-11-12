# coding:utf-8
import requests

def get_plugin_info():
    plugin_info = {
        "name": "Apache solr未授权访问",
        "info": "Apache solr未授权访问",
        "level": "中危",
        "type": "未授权访问",
        "author": "zinc",
        "url": "",
        "keyword": "server:apache",
        "source": 1
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        url = ''
        urls = ''

        path = '/solr/#/'
        if port == 443:
            url = 'https://%s%s' % (ip, path)
        elif port == 80:
            url = 'http://%s%s' % (ip, path)
        else:
            url = 'http://%s:%d%s' % (ip, port, path)
            urls = 'https://%s:%d%s' % (ip, port, path)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        url = url if url else urls

        r = requests.get(url, headers=headers, timeout=timeout, verify=False)
        if 'solr admin' in r.content.lower():
            print u"未授权访问"
            return u"未授权访问"

    except Exception as e:
        print e

if __name__ == '__main__':
    check('120.25.24.162', 8983, 3)