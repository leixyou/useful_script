#!/usr/bin/env python
import json
import gc


def get_pid(data):
    pid=data['behavior']['generic'][0]['pid']
    # type(pid)
    return pid

#---------------------------------------------------------------------
def read_json(json_path):
    """"""
    with open(json_path,'r') as f:
        data=json.load(f)
        f.close()
    pid=get_pid(data)
    return data,pid

def read_behavior(data):
    
    behavior= data['behavior']
#------------collect memory----start---
    del data
    gc.collect()
#------------collect memory----end-----
    behavior_str=json.dumps(behavior)
    with open('behavior.txt','a+') as ff:
        ff.truncate()
        ff.write(behavior_str)
        ff.close()        
    #------------collect memory----start---
    del behavior_str
    gc.collect()
    #------------collect memory----end-----
    return behavior





def read_apistat(behavior,pid):
    
    apistat=behavior['apistats'][str(pid)]
    api=[]
    
    #apistat_str=json.dumps(apistat)   
    with open('apistat.json','a+') as ff:
        ff.truncate()
        ff.write(json.dumps(apistat))
        ff.close()
        
    with open('api.txt','a+') as ff:
        ff.truncate()
        
        for k in apistat.keys():
            api.append(k)        
            ff.writelines(k)
            ff.write('\n')
        ff.close()
    return api



if __name__=='__main__':
    
    json_path='./report.json'
    data,pid=read_json(json_path)
    behavior=read_behavior(data)
    api=read_apistat(behavior,pid)
    print api