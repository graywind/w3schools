#!/usr/bin/env python3
"""
Python Variables
https://www.w3schools.com/python/python_variables.asp
"""

x = 5
y = "John"

print(type(x))
print(x)

print(type(y))
print(y)

# Casting

a = str(3)
b = int(3)
c = float(3)

print(type(a))
print(a)
print(type(b))
print(b)
print(type(c))
print(c)

#String variables can be declared with either single or double quotes

h = "John"
k = 'John'

if h == k:
    print('\nmatch!')

#Case sensitivity in var names

H = "Beth"

if h != H:
	print('\nno match!')

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Pascal Case (I feel old)
#Each word starts with a capital letter:
MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore char *his*
my_variable_name = "John"

#Python allows you to assign values to multiple vars in one line:

do, it, nao = "Orange", "Banana", "Cherry"
print(do,'\n',it,'\n',nao,'\n', sep='', end='')

#If you have a collection of values in a list, tuple etc. Python allows you to extract the vals into vars. This is called unpacking.

fruits = [ do, it, nao ]
l, o, L = fruits
print(l,'\n',o,'\n',L,'\n', sep='', end='')
