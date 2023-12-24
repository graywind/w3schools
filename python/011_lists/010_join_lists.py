#!/usr/bin/env python3
"""
Section Name: Python - Join Lists
URL: https://www.w3schools.com/python/python_lists_join.asp
"""
list1 = list(("a","b","c"))
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# Using append method with list comp
[list1.append(x) for x in list2]
print(list1)

list1 = list(("a","b","c"))
# Use extend method instead
list1.extend(list2)
print(list1)
