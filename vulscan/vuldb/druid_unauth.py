#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def get_plugin_info():
    plugin_info = {
        "info": "Druid未授权访问",
        "source": 1,
        "name": "Druid未授权访问",
        "keyword": "server:web",
        "level": "中危",
        "url": "",
        "author": "zinc",
        "type": "未授权访问"
    }
    return plugin_info

def check(host, port, timeout):
	if port == 443:
		url = "https://%s/druid/index.html" %(host, )
	else:
		url = "http://%s:%d/druid/index.html" % (host, port)
	
	try:
		r = requests.get(url, timeout=timeout, verify=False)
		if r.status_code == 200 and 'Druid Stat Index' in r.content:
			return u'未授权访问'
		else:
			print 'No'
	except Exception, e:
		print e

if __name__ == '__main__':
	with open('web.txt') as f:
		contents = f.read().split('\n')
	for line in contents:
		ip, port = line.split('\t')
		if check(ip, int(port), 2):
			print ip, port
			with open('result.txt', 'w') as f:
				f.write(ip + port + '\n')

