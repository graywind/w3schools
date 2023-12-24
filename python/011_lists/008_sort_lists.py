#!/usr/bin/env python3
"""
Section Name: Python - Sort Lists
URL: https://www.w3schools.com/python/python_lists_sort.asp
"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist2 = [100,50,65,82,23]
thislist2.sort()
print(thislist2)

#Now in reverse using keyword reverse
thislist.sort(reverse = True)
print(thislist)
thislist2.sort(reverse = True)
print(thislist2)

#Customized sort, base on distance to 50
def distance(n):
  return abs(n-50)

thislist2.sort(key=distance)
print(thislist2)

#Sort is case sensitive
thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort()
print(thislist)
#Case insensitive sort
thislist.sort(key = str.lower)
print(thislist)

#Reverse order of a list regardlist of alpha
thislist.reverse()
print(thislist)
