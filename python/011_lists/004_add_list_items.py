#!/usr/bin/env python3
"""
Section Name: Python - Add List Items
URL: https://www.w3schools.com/python/python_lists_add.asp
"""

#Append method
thislist = ["apple","banana","cherry"]
thislist.append("orange") #add to end of list
print(thislist)

#Insert method
thislist = ["apple","banana","cherry"]
thislist.insert(1,"orange") #insert at second position
print(thislist)

#Append from another list
thislist = ["apple","banana","cherry"]
tropical = ["mango", "pinapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#extend takes any iterable, for example a tuple
thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)
