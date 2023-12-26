#!/usr/bin/env python3
"""
Section Name: Python - Copy Dictionaries
URL: https://www.w3schools.com/python/python_dictionaries_copy.asp
"""

#Copying a dictionary cannot be done with a simple = op, as this will only copy the reference as seen
#in earlier lessons.
def refresh():
  global anotherdict
  anotherdict = {
    "brand" : "Ford",
    "model" : "F-350",
    "colors" : ["red","white","green","black"],
    "year" : 2001
  }

refresh()

#you can utilize the copy method to output a new dict

mydict = anotherdict.copy()

print(mydict)

del mydict
del anotherdict
#another way to make a copy is to use the dict function to output a new copy.

refresh()
mydict = dict(anotherdict)
del anotherdict
print(mydict)
del mydict
