#!/usr/bin/env python3
"""
Section Name: Python - Copy Lists
URL: https://www.w3schools.com/python/python_lists_copy.asp
"""
# You cannot copy a list with a simple = expression, as this will only refer to the previous list. Consider the below:

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist2 = thislist #this is reference and not a copy
thislist.pop()
print(thislist2) #change made to thislist shows in thislist2

# Copy using method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
thislist.pop()
print(mylist)
thislist = mylist.copy()

# Copy using list method
mylist.clear()
mylist = list(thislist)
print(mylist)
