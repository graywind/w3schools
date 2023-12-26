#!/usr/bin/env python3
"""
Section Name: Python - Loop Dictionaries
URL: https://www.w3schools.com/python/python_dictionaries_loop.asp
"""

anotherdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "colors" : ["red","white","green","black"],
  "year" : 2001
}

#simple for loops

for x in anotherdict:
  print("keytype:{},valuetype{}".format(type(x),type(anotherdict[x])))

for x in anotherdict:
  print("Key: {}, Value: {}".format(x,anotherdict[x]))

#keys() method to return keys
for x in anotherdict.keys():
  print(x)

#values() method to return values
for x in anotherdict.values():
  print(x)

#items() method to return both kv
for x,y in anotherdict.items():
  print(x,y)
