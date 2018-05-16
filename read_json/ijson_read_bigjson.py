#!/usr/bin/env python
import ijson
import json
import optparse
def read_apistats(report_filepath):
    
    with open(report_filepath,'r') as f:
        apistats=ijson.items(f,'behavior.apistats')
        apis=[]
        for pid in apistats:
            for api in pid.values():
                apis.append(api)
        f.close()
    return apis

def write_file(filepath,apis):
    with open(filepath,'a+') as f:
        f.truncate()
        for x in apis:
            f.write(json.dumps(x))
            f.write('\n')
        f.close()
if __name__=='__main__':
    option=optparse.OptionParser(usage='usage: %prog [src_report.json] [dest_filname.json]\n' )
    (options,args)=option.parse_args()
    
    if len(args)!=2:
        print option.print_usage()
    else:
        report_filepath=args[0]
        apis=read_apistats(report_filepath)
    
        write_file(args[1],apis)
    
