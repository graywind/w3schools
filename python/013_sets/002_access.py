#!/usr/bin/env python3
"""
Section Name: Python - Access Set Items
URL: https://www.w3schools.com/python/python_sets_access.asp
"""

#without an index we can't while loop, but we can for loop or use an in keyword
thisset = set(("apple","banana","cherry"))
for x in thisset:
  print(x)

print("banana" in thisset)

if "banana" in thisset:
  print("we have bananas!")
