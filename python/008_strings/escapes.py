#!/usr/bin/env python3
"""
Section Name: Escape Characters
URL: https://www.w3schools.com/python/python_strings_escape.asp
"""

# no good example
# txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."

print(txt)

# Single Quote
print("\'")

# Backslash
print("\\\\\\")

# New line
print("\n")

# Carriage Return
print("\r")

# Pretend you are DOS
print("\r\n")

# Tabby tab tab
print("\ttabby\ttab\ttab")

# Backspace
print("Backs\bspace")

# Octal value
print("\100")

# Hex value
print("\x77")
