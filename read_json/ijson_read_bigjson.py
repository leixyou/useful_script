#!/usr/bin/env python
import ijson
import json
import optparse
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
        f.write(json.dumps(apis))
        #for x in apis:
            #f.write(json.dumps(x))
            #f.write('\n')
        f.close()
if __name__=='__main__':
    option=optparse.OptionParser(usage='usage: %prog [src_report.json] [dest_filname.json]\n' )
    option_list=['read_apistats','read_dlls']
    option.add_options(option_list)
    (options,args)=option.parse_args()
    
    
    print option.print_usage()
 
    report_filepath='./report.json'
    #apis=read_apistats(report_filepath)
    generic=read_dlls(report_filepath)
    #write_file(args[1],apis)
    try:
        write_file(args[1], generic)
    except:
        print 'no second recv file'
