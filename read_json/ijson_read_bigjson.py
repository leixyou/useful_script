#!/usr/bin/env python
import ijson
import json
import getopt
import sys
import decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)



def read_apistats(report_filepath):
    
    with open(report_filepath,'r') as f:
        apistats=list(ijson.items(f,'behavior.apistats'))

    return apistats

#----------------------------------------------------------------------
def read_dlls(report_filepath):
    """show loaded dlls"""
    with open(report_filepath,'r') as f:
        generic=list(ijson.items(f,'behavior.generic'))
        f.close()
    return generic
def write_file(filepath,apis):
    with open(filepath,'a+') as f:
        f.truncate()
        f.write(json.dumps(apis,cls=DecimalEncoder))
        #for x in apis:
            #f.write(json.dumps(x))
            #f.write('\n')
        f.close()
        
        
#----------------------------------------------------------------------
def usage():
    """"""
    print '-h --help print usage'
    print '-f --file=filepath '
    print '-d --read_dlls to read dlls'
        
        
if __name__=='__main__':
    try:
        options,args=getopt.getopt(sys.argv[1:],"hadf:",['help','read_apistats','read_dll','file='])
    except:
        sys.exit()
        
        
    for op,args in options:
        if op in ("-h",'--help'):
            usage()
            
        if op in ('-f','--file'):
            report_filepath=args
            if report_filepath=='':
                usage()
        if op in ('-a','--read_apistats'):
            apis=read_apistats(report_filepath)
            write_file('./apistats.json', apis)
        if op in ('-d','--read_dlls'):
            dlls=read_dlls(report_filepath)
            write_file('./dlls.json',dlls)
