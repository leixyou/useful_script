#!/usr/bin/env python
import json
import gc


def get_pid(result):
    pid=result['behavior']['generic'][0]['pid']
    # type(pid)
    return pid

#---------------------------------------------------------------------
def read_json(json_path):
    """"""
    with open(json_path,'r') as f:
        result=json.load(f)
        f.close()
    #pid=get_pid(result)
    pid=1
    return result,pid

def read_behavior(result):
    
    behavior= result.get('behavior')

    behavior_str=json.dumps(behavior)
    with open('behavior.json','a+') as ff:
        ff.truncate()
        ff.write(behavior_str)
        ff.close()        
    #------------collect memory----start---
    del behavior_str
    gc.collect()
    #------------collect memory----end-----
    return behavior

#----------------------------------------------------------------------
def read_signatures(result):
    """read signatures which has callbacks~"""
    signatures= result['signatures']
    signatures_str=json.dumps(signatures)
    with open('signatures.json','a+') as ff:
        ff.truncate()
        ff.write(signatures_str)
        ff.close()        
    #------------collect memory----start---
    del signatures_str
    gc.collect()
    #------------collect memory----end-----
    return signatures    
    



def read_apistat(result):
    
    apistat=result.get('behavior',{}).get('apistats',[])
    
       
    #apistat_str=json.dumps(apistat)   
    with open('apistat.json','a+') as ff:
        ff.truncate()
        
        ff.write(json.dumps(apistat))
        ff.close()
    api=[]
    with open('api.json','a+') as ff:
        ff.truncate()
        
        for k in apistat.keys():
            api.append(json.dumps(k))        
            ff.writelines(json.dumps(k))
            ff.write('\n')
        ff.close()
    return api

#----------------------------------------------------------------------
def read_calls(result):
    """read the calls of process"""
    calls=[]
    for process in result.get('behavior',{}).get("processes",[]):
        calls.append(process["calls"])
        process["calls"]=[]
    with open('./calls.json','a+') as f:
        f.truncate()
        f.write(json.dumps(calls))
        f.close()
    del calls
    
#----------------------------------------------------------------------
def read_summary(result):
    """"""
    
    summary=result['behavior']['summary']
    for key,value in summary.items():
        with open('./'+key+'.json','a+') as f:
            f.truncate()
            f.write(json.dumps(value))
            f.close()
    

if __name__=='__main__':
    
    json_path='./report.json'
    result,pid=read_json(json_path)
    #behavior=read_behavior(result)
    api=read_apistat(result)
    #print api
    signature=read_signatures(result)
    read_calls(result)
    read_summary(result)
