#!/usr/bin/env python3
"""
Section Name: Python Sets
URL: https://www.w3schools.com/python/python_sets.asp
"""
#Sets are unordered, unchangeable*, and unindexed.
#(set items are unchangeable directly, but you can add and delete items)
thisset = {"apple","banana","cherry"}
print(thisset)

#duplicates are not allowed, but note no exception thrown. Free dedup?
thisset = {"apple","banana","cherry","apple"}
print(thisset)

#True and 1 and False and 0 are considered the same.
thisset = {"apple","banana","cherry","apple", True, 1, False, 0, 2}
print(thisset)

#items can be any data type and mixed as seen above.

print(type(thisset))

#using the set constructor
thisset = set(("apple","banana","cherry"))
print(thisset)
