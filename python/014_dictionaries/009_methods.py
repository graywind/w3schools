#!/usr/bin/env python3
"""
Section Name: Python Dictionary Methods
URL: https://www.w3schools.com/python/python_dictionary_methods.asp
"""

#Methods not covered in previous lessons

#fromkeys() Returns a dictionary with provided keys with a default value

x = dict.fromkeys(('key1','key2','key3'),None)
print(x)

#setdefault(), method returns the value of the item with the specified key, sets value if key doesn't exist.

print(x.setdefault('key3',0))
print(x.setdefault('key4',0))
print(x)
