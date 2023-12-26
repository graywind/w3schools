#!/usr/bin/env python3
"""
Section Name: Python Dictionaries
URL: https://www.w3schools.com/python/python_dictionaries.asp
"""

#Dictionaries are used to store data values in k:v pairs and utilize curly braces
#A dictionary is a collection which is ordered, changeable, and does not allow duplicates.

thisdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "year" : 2001
}
print(thisdict["year"])

#The dict constructor will throw on a duplicate.
"""
thatdict = dict(
  brand = "Ford",
  model = "F-350",
  year = 2001,
  year = 1998
)
"""
#To see an example of duplicate values overwriting existing ones, we must skip the constructor
thatdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "year" : 2001,
  "year" : 1998
}
print(thatdict["year"])

print(len(thatdict))

#dictionary itmes can be of any data type
anotherdict = {
  "brand" : "Ford",
  "model" : "F-350",
  "year" : 2001,
  "colors" : ["red","white","green","black"]
}
print(anotherdict["colors"][0])
