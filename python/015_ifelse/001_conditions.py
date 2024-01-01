#!/usr/bin/env python3
"""
Section Name: Python If ... Else
URL: https://www.w3schools.com/python/python_conditions.asp
"""

"""
Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.
"""

b = 33
a = 200
c = 500

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Shorthand if oneliner
if a > b: print("a is greater than b")

#Shorthand ifelse (ternary ops or conditional expressions)

print("A") if a > b else print("=") if a == b else print("B")

#and
if a>b and c>a: print("Both conditions are true")

#or
if a>b or a>c: print("At least one of the conditions is True")

#nested if for indentation fun

x = 41

if x > 10:
  print("Above ten,")
  if x > 10:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass statement, use for if statement with no content as that avoids an error. Yay stubs
if a > b:
  pass


