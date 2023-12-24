#!/usr/bin/env python3
"""
Section Name: Python - Change List Items
URL: https://www.w3schools.com/python/python_lists_change.asp
"""

thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist) #show banana change

thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist) #show 2nd and 3rd change

thislist = ["apple","banana","cherry"]
thislist[1:2] = ["blackcurrant","watermelon"]
print(thislist) #insert two seperate vals in place of 2nd

thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #replace 2nd and 3rd val with 1 val

#insert method
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)
