#!/usr/bin/env python3
"""
Section Name: Python - Remove Dictionary Items
URL: https://www.w3schools.com/python/python_dictionaries_remove.asp
"""

anotherdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "colors" : ["red","white","green","black"],
  "year" : 2001
}

#pop method to remove specified key name

anotherdict.pop("brand")

print(anotherdict)

#popitem method removes the last added item, which returns the removed kv as a tuple

x = anotherdict.popitem()
print(type(x))
print(x)
print(anotherdict)

#del keyword can be used on a specific item

del anotherdict["model"]
print(anotherdict)

#clear method empties the dict
anotherdict.clear()
print(anotherdict)
#del works as expected against the whole dict

del anotherdict
#print(anotherdict) #undef
