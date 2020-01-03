#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb, os
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("<ul>")
for doc in os.listdir("./"):
    if doc != "cgi-bin" and doc[0] != ".":
        print("<li><a href=\"../{}\">{}</a></li>".format(str(doc), str(doc)))
print("</ul>")
print("</body>")
print("</html>")
