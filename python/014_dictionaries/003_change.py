#!/usr/bin/env python3
"""
Section Name: Python - Change Dictionary Items
URL: https://www.w3schools.com/python/python_dictionaries_change.asp
"""

anotherdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "year" : 2001,
  "colors" : ["red","white","green","black"]
}

#Changing values directly by key name

anotherdict["year"] = 1998

print(anotherdict)

#Using update method

anotherdict.update({"year":2001})

print(anotherdict["year"])

