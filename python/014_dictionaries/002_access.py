#!/usr/bin/env python3
"""
Section Name: Python - Access Dictionary Items
URL: https://www.w3schools.com/python/python_dictionaries_access.asp
"""

#access examples
anotherdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "year" : 2001,
  "colors" : ["red","white","green","black"]
}
print(anotherdict["colors"][0])
#using get()
print(anotherdict.get("colors")[0])
#get keys with method
x = anotherdict.keys()
for i in x:
	print(i)

anotherdict["colors"][2] = "emerald"
print(anotherdict["colors"][2])
#use values() method to get a list of v
x = anotherdict.values()
print(x)
