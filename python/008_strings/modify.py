#!/usr/bin/env python3
"""
Section Name: Python - Modify Strings
URL: https://www.w3schools.com/python/python_strings_modify.asp
"""

# Upper case method
a = "Hello, World!"
print(a.upper())

# Lower case method
print(a.lower())

# Strip method to remove whitespace from start and end
a = " Hello, World! "
print(a.strip())

# Split method returns a list where the text between the separator becomes list times.

a = "Hello, World!"
b = a.split(",")
print(type(b))
print(b)

