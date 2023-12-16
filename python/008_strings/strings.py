#!/usr/bin/env python3
"""
Section Name: Python Strings
URL: https://www.w3schools.com/python/python_strings.asp
"""

'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello" .
You can display a string literal with the print() function:
'''


print("Hello")
print('Hello')

# Assign string to a var"

a = "Hello"
print(a)

# You can assign a multiline string to a var by using three quotes. Note how similar this is to the multiline comments above.

a = """I'm a little teapot
short and stout"""
print(a)

# Single quotes are also acceptable
a = '''Here is my handle
here is my spout'''
print(a)

# Strings in python are arrays of bytes representing unicode characters.
# Howver, Python does not have a character data type, a single char is simply a string with a length of 1.
a = "Hello, World!"
print(a[1])

# Use a for loop to print a string char by char
for x in "banana":
    print(x)

# Get the length of a given string
a = "Hello, World!"
print(len(a))

# Check if "free" is present in the following text

txt = "The best things in life are free!"
print("free" in txt)

# We can also directly assign this shorthand as a bool
b = "free" in txt
print(type(b))

# if it up
if "free" in txt:
    print("Yes, 'free' is present.")

# do the reverse

print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
