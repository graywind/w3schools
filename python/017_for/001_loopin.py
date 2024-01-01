#!/usr/bin/env python3
"""
Section Name: Python For Loops
URL: https://www.w3schools.com/python/python_for_loops.asp
"""

fruits = list(("apple", "banana", "cherry"))
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping throw a string, this is by char

for x in "banana":
  print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana": break

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana": continue

#fnrange
for x in range(6):
  print(x)

for x in range(2,6):
  print(x)

for x in range(2,30,x^2):
  print(x)

#else
for x in range(6):
  print(x)
else:
  print("clean finish")

for x in range(6):
  if x == 3: break
  print(x)
else: #wont exec with break
  print("clean finish")

#nested loop, inner loop will execute for each iteration of the outer loop

adj = list(("red","big","tasty"))
fruits = list(("apple","banana","cherry"))
for x in adj:
  print("iwuzhere")
  for y in fruits:
    print(x,y)

#for loops can't be emtpy as well, pass statement for filler

for x in [0,1,2]:
  pass
