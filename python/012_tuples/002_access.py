#!/usr/bin/env python3
"""
Section Name: Python - Access Tuple Items
URL: https://www.w3schools.com/python/python_tuples_access.asp
"""
thistuple = ("apple","banana","cherry")
print(thistuple[1]) #banana
print(thistuple[-1]) #cherry

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5]) #prints pos 3,4,5, but not 6

print(thistuple[:4]) #ignore pos 5 and beyond
print(thistuple[2:]) #ignore up to pos 2

print(thistuple[-4:-1]) #look back from end 4, ignore last entry

if "apple" in thistuple:
  print("Yes, 'apple' is in thistuple")
