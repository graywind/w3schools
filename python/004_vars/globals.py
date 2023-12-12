#!/usr/bin/env python3
"""
Python Variables
https://www.w3schools.com/python/python_variables_global.asp
"""

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def gscope():
    global x
    x = "fantastic"

gscope()

print("Python is " + x)
