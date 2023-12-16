#!/usr/bin/env python3
"""
Section Name: Python - Format Strings
URL: https://www.w3schools.com/python/python_strings_format.asp
"""

age = 36

#Below is not valid, only strings can be concatenated, print won't even be hit
#txt = "My name is John, I am " + age
#print(txt)

txt = "My name is John, and I am {}"
print(txt.format(age))

# Format method takes an unlimited number of args

quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

# You can use index numbers to control placeholders

myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity,itemno,price))

