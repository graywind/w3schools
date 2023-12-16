#!/usr/bin/env python3
"""
Section Name:
URL: https://www.w3schools.com/python/python_strings_slicing.asp
"""
# Slice from the start to pos 5 (not included)

b = "Hello, World!"
print(b[:5])

# Slice to the end

print(b[2:])

# Negative Indexing, start slice from the end of the string

print(b[-5:-2])

# Get the last two chars from the end of the string

print(b[-2:])

# Drop the last two chars from the end of the string

print(b[:-2])
