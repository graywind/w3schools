#!/usr/bin/env python3
"""
Section Name: Numbers
URL: https://www.w3schools.com/python/python_numbers.asp
"""

x = 1 #int
y = 2.8 #float
z = 1j #complex

xx = x
yy = y
zz = z

print(type(x))
print(type(y))
print(type(z))

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type conversion exercise

a = float(xx)
b = int(yy)
c = complex(xx)

print(xx)
print(a)

print(yy)
print(b)

print(xx)
print(c)

print(type(a))
print(type(b))
print(type(c))
