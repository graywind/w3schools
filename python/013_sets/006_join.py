#!/usr/bin/env python3
"""
Section Name: Python - Join Sets
URL: https://www.w3schools.com/python/python_sets_join.asp
"""

# We have two methods for combining sets. One is union() which returns a new set, and update() which works on an existing set.

set1 = {"a","b","c"}
set2 = set((1,2,3))
set3 = set1.union(set2)

print(set1)
print(set2)
print(set3)

set1.update(set2)
print(set1)

#intersection_update() will keep only items that are present in both sets

x = {"apple","banana","cherry","orange"}
y = {"apple","strawberry","kiwi","orange"}

x.intersection_update(y)
print(x)

#intersection() will return a new set that only contains matches between sets

x = {"apple","banana","cherry","orange"}
y = {"apple","strawberry","kiwi","orange"}

z = x.intersection(y)
print(x)
print(y)
print(z)
del z
#the inverse of this would be symmetric_difference_update() and symmetric_difference() alike

x = {"apple","banana","cherry","orange"}
y = {"apple","strawberry","kiwi","orange"}
x.symmetric_difference_update(y)
print(x)

x = {"apple","banana","cherry","orange"}
z = x.symmetric_difference(y)
print(x)
print(y)
print(z)
del z
