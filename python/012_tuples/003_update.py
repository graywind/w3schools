#!/usr/bin/env python3
"""
Section Name: Python - Update Tuples
URL: https://www.w3schools.com/python/
"""

#tuples are immutable, but workarounds with lists are available.

x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

x = ("apple","banana","cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

#It is possible to add tuples to tuples

x = ("apple","banana","cherry")
y = ("orange",) #trailing comma req to be recognized as a tuple with one item
x += y
print(x)


#Removing works in a similar way

x = ("apple","banana","cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

#delete keyword as expected
del x,y
