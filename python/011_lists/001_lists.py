#!/usr/bin/env python3
"""
Section Name: Python Lists
URL: https://www.w3schools.com/python/python_lists.asp
"""

#List
"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets
"""

#list items are ordered, changeable, and allow duplicate values.
thislist = ["apple","banana","cherry"]
print(thislist)
print(len(thislist))

#Can be any data type
list0 = ["apple","banana","cherry"]
list1 = [1,5,7,9,3]
list2 = [True, False, False]

#Can contain different data types
list4 = [ "beep", 5, False, 4.1, None, ["what","the"]]
print(list4[5][0])
list4[5][0]="hi"
print(list4[5][0])

#list type
print(type(list4[5]))

#Using the list() constructor to make a list
alist = list(("apple","cherry","banana")) # note the double round-brackets
print(alist)
