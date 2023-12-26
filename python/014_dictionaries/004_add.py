#!/usr/bin/env python3
"""
Section Name: Python - Add Dictionary Items
URL: https://www.w3schools.com/python/python_dictionaries_add.asp
"""

anotherdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "year" : 2001,
  "colors" : ["red","white","green","black"]
}

#process is identical to updating from previous lesson

#Changing values directly by key name

anotherdict["transmission"] = "Automatic 4WD"

#Using update method

anotherdict.update({"oil":"15W40"})

print(anotherdict)

