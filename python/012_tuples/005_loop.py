#!/usr/bin/env python3
"""
Section Name: Python - Loop Tuples
URL: https://www.w3schools.com/python/python_tuples_loop.asp
"""
#standard for loop
thistuple = ("apple","banana","cherry")
for x in thistuple:
  print(x)

#for loop using index nums
for i in range(len(thistuple)):
  print(thistuple[i])

#standard while loop on index
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i += 1
del i
