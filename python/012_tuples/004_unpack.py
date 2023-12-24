#!/usr/bin/env python3
"""
Section Name: Python - Unpack Tuples
URL: https://www.w3schools.com/python/python_tuples_unpack.asp
"""

fruits = ("apple","banana","cherry")

#extract values back to variables
(green, yellow, red) = fruits

print("{}, {}, {}".format(green,yellow,red))

fruits = ("apple","banana","cherry","strawberry","raspberry")

#Asterisks assigns additional values as a list.
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#If the asterisk is added to a variable other than the last, then a list is created and added to until the number of values match the number of variables

fruits = ("apple","mango","papaya","pineapple","cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
