#!/usr/bin/env python3
"""
Section Name: Python - Remove List Items
URL: https://www.w3schools.com/python/python_lists_remove.asp
"""
#remove method removes first occurance
thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple","banana","cherry","banana","kiwi"]
thislist.remove("banana")
print(thislist)

#pop method removes item and specified index, without an index removes last item. Defaults to last unspecified
thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)

#del keyword usage
test = "thing"
del test

thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)

#destroy entire list
del thislist

#clear list method, leaves empty list intact
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)
