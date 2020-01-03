#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb, os
import json

cgitb.enable()
try:
    print("Cache-control: private, max-age=0, no-cache")
    print("Content-type: application/json\r\n\r\n")
    filelist = os.listdir("./send/")
    filelist = filter(lambda x: (x[0] != '.' and x!='cgi-bin'), filelist)
    filelist = list(filelist)
    filedict = {'files' : filelist}
    jsonout = json.dumps(filedict)
    print(jsonout)

except:
    cgitb.handler()

