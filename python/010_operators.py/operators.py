#!/usr/bin/env python3
"""
Section Name: Python Operators
URL: https://www.w3schools.com/python/python_operators.asp
"""

#Arithmetic Operators

#Addition
print(2+8)
#Subtraction
print(2-8)
#Multiplication
print(2*8)
#Division
print(2/8)
#Modulus
print(9%4)
#Floor Division
print(9//4)
#Exponentation
print(2**8)

#Assignment Operators
x = 5
print(x)
#x = x + 3
x += 3
print(x)
#x = x - 3
x -= 3
print(x)
#x = x * 3
x *= 3
print(x)
#x = x / 3
x /= 3
print(x)
#x = x % 3
x %= 3
print(x)
#x = x // 3
x //= 3
print(x)

x = 5

#x = x ** 3
x **= 3
print(x)

# Bitwise Assignment Operators
"""
&  	AND 	Sets each bit to 1 if both bits are 1 	x & y
| 	OR 	Sets each bit to 1 if one of two bits is 1 	x | y
^ 	XOR 	Sets each bit to 1 if only one of two bits is 1 	x ^ y
~ 	NOT 	Inverts all the bits 	~x
<< 	Zero fill left shift
	Shift left by pushing zeros in from the right and let the leftmost bits fall off
		x << 2
>> 	Signed right shift
	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
		x >> 2
"""

#x = x & 3
x &= 3
print(x)

#x = x & 4
x = 10

x &= 4
print(x)

x = 10

#x = x | 4
x |= 4
print(x)

#x = x ^ 4
x = 10

x ^= 4
print(x)

x = 10
x = ~x
print(x)

x = x << 1
print(x)
x = x << 2
print(x)
x = x >> 1
print(x)
x = x >> 2
print(x)

#Precedence Order
"""
() 	Parentheses
** 	Exponentiation
+x  -x  ~x 	Unary plus, unary minus, and bitwise NOT
*  /  //  % 	Multiplication, division, floor division, and modulus
+  - 	Addition and subtraction
<<  >> 	Bitwise left and right shifts
& 	Bitwise AND
^ 	Bitwise XOR
| 	Bitwise OR
==  !=  >  >=  <  <=  is  is not  in  not in  	Comparisons, identity, and membership operators
not 	Logical NOT
and 	AND
or 	OR
"""
