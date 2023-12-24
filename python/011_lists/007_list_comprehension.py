#!/usr/bin/env python3
"""
Section Name: Python - List Comprehension
URL: https://www.w3schools.com/python/python_lists_comprehension.asp
"""
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

#Consider the following, based on a list containing fruits you want to create a new list matching a substring of "a"
#Here is the long form method without list comp

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = list(())

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist.clear()

# List comp offers a oneliner version
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist.clear()
# Exclude match
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist.clear()

# No if needed
newlist = [x for x in fruits]
print(newlist)

newlist.clear()

# range iterable
newlist = [x for x in range(10)]
print(newlist)

newlist.clear()

# range iterable under 5
newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist.clear()

# string upper method over iterable
newlist = [x.upper() for x in fruits]
print(newlist)
newlist.clear()

# replace each
newlist = ['hello' for x in fruits]
print(newlist)
newlist.clear()

# replace matching string
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
del newlist
