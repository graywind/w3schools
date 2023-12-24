#!/usr/bin/env python3
"""
Section Name: Python - Loop Lists
URL: https://www.w3schools.com/python/python_lists_loop.asp
"""

thislist = list(("apple","banana","cherry"))
for thing in thislist:
  print(thing)

for i in range(len(thislist)):
  print(thislist[i] + str(i))

i = 0
while i < len(thislist):
  print(str(i)+thislist[i])
  i += 1
del i

#shorthand for loop using list comprehension
[print(thing) for thing in thislist]
