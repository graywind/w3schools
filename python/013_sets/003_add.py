#!/usr/bin/env python3
"""
Section Name: Python - Add Set Items
URL: https://www.w3schools.com/python/python_sets_add.asp
"""
# add method
thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

# add items from another set

tropical = set(("pineapple","mango","papaya"))
thisset.update(tropical)
print(thisset)

#can be added from any iterable
morefruit = ["strawberry","kiwi"]
thisset.update(morefruit)
print(thisset)
