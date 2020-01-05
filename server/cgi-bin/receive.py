#!/usr/bin/env python3
import cgi, cgitb, os
import json

cgitb.enable()

try:
    form = cgi.FieldStorage()
    print("Cache-control: private, max-age=0, no-cache")
    print("Content-type: application/json\r\n\r\n")
    fileitem = form['filename']
    if fileitem.filename:
    
        fn = os.path.basename(fileitem.filename)
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", "received", fn))
        open(filepath, 'xb').write(fileitem.file.read())
        message = 'The file name "' + fn + '" is transferred.'

    data = {"message" : message, 
    "path": filepath}

    jsonout = json.dumps(data)
    print(jsonout)

except:
    cgitb.handler()
