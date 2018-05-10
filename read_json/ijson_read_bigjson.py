#!/usr/bin/env python
import ijson
import json
def read_apistats(report_filepath):
    
    with open(report_filepath,'r') as f:
        apistats=json.dumps(ijson.items(f,'behavior.apistats'))
        #print apistats
        f.close()
    return apistats

def write_file(filepath,data):
    f=open(filepath,'a+')
    f.truncate()
    if type(data) is not str:
        for x in data:
            f.write(x)
            f.write('\n')
    else:
        f.write(data)
    f.close()
    return 
if __name__=='__main__':
    report_filepath="./report.json"
    apistats=read_apistats(report_filepath)
    write_file('./result.json',apistats)
