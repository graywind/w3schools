#!/usr/bin/env python3
"""
Section Name: Python - Access List Items
URL: https://www.w3schools.com/python/python_list_access.asp
"""

thislist = [ "apple", "banana", "cherry" ]
print(thislist[0]) # from the start
print(thislist[-1]) # from the end (Negative Indexing)
print(thislist[0:2]) # a range! Remember start index is included, end index is not included

biglist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(biglist[2:5]) #three items
print(biglist[2:]) #start at 2, go to end of list
print(biglist[-4:-1])

if "orange" in biglist:
  print("Yes, 'orange' is in the list.")
