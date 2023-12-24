#!/usr/bin/env python3
"""
Section Name: Python Tuples
URL: https://www.w3schools.com/python/python_tuples.asp
"""

"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""

thistuple = tuple(("apple","banana","cherry"))
#dupes allowed
thistuple = tuple(("apple","banana","cherry","apple","cherry"))
print(len(thistuple))
thistuple = tuple(("apple",)) #tuple with a single item must have trailing comma
print(thistuple)
#items can  be any time, and can also be mixed
tuple1 = ("apple","banana","cherry")
tuple2 = (1,5,7,9,3)
tuple3 = (True, False, False)

tuple4 = ("abc", 34, True,  40, "male", None)

print(type(tuple4))
