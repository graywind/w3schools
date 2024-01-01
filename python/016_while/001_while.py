#!/usr/bin/env python3
"""
Section Name: Python While Loops
URL: https://www.w3schools.com/python/python_while_loops.asp
"""

i = 0
while i < 6:
  print(i)
  i += 1

#break loop when condition
i = 0
while i < 6:
  print(i)
  if i == 3: break
  i += 1

#skip remaning iter with cont
i = 0
while i < 6:
  i += 1
  print(i)
  if i == 3: continue

#else when done
i = 0
while i < 6:
  i += 1
  print(i)
else:
  print("i is no longer less than 6")
