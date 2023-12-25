#!/usr/bin/env python3
"""
Section Name: Python - Set Methods
URL: https://www.w3schools.com/python/
"""

x = {"apple","orange","kiwi"}
x.add("strawberry")
print(x)

y = {"papaya","starfruit"}
z = x.copy()
print(z)

z = y.difference(x)
print(z)

z = y.intersection(x)
print(z)

print(x.isdisjoint(y))
sub = {"apple",}

print(sub.issubset(x))
