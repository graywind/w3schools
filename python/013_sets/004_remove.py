#!/usr/bin/env python3
"""
Section Name: Python - Remove Set Items
URL: https://www.w3schools.com/python/python_sets_remove.asp
"""
thisset = {"apple","banana","cherry"}
#remove method will throw if there isn't a match
thisset.remove("banana")
#thisset.remove("grape")
print(thisset)

thisset = set(("apple","banana","cherry"))
thisset.discard("banana")
thisset.discard("grape")
print(thisset)

#pop is usable but will remove a random item, could be fun
thisset = set(("apple","banana","cherry"))
x = thisset.pop()
#the return value of pop is the removed value
print(thisset)
print(x)

thisset.clear()
print(thisset)

#del keyword works as expected
del thisset
#print(thisset)

