#!/usr/bin/env python
import ijson
def read_alert():
    
    filepath="./alert.json"
    with open(filepath,'r') as f:
        objects=ijson.items(f,'')
        for x in list(objects):
            print x 
            
        f.close()
        
if __name__=='__main__':
    read_alert()