#coding:utf-8
#author:zinc
import os
import json

def run(ip_list,path,rate):
    try:
        
        result_file = open('tmp.log', 'r')
        result_json = result_file.readlines()
        result_file.close()
        open_list = {}
        for res in result_json:
            try:
                res = json.loads(res)
                open_list[res['ipaddr']] = res['ports']
            except:pass

        os.remove('tmp.log') 
        return open_list
    except:
        pass
