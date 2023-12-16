#!/usr/bin/env python3
"""
Section Name: String Methods
URL: https://www.w3schools.com/python/python_strings_methods.asp
"""

# capitalize()

# The first letter is capitalized

txt = "hello, and welcome to my world."
print(txt.capitalize())

# The first char is converted to uppercase, but plot twist, the rest are converted to lower case.

txt = "python is FUN!"
print(txt.capitalize())

# Numbers do nothing at the start, but the plot twist still applies.
txt = "36 is my AGE."
print(txt.capitalize())

# casefold()
"""
The casefold() method returns a string where all the characters are lower case.

This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will
convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
"""

txt = "Hello, And Welcome To My World!"
print(txt.casefold())

# center()
# The center() method will center align the string, using a specified character (space is default) as the fill character.
# Could see this being useful with the width of the terminal known to be fancy
txt = "banana"
print(txt.center(80))

# Override the default padding of space
print(txt.center(80,"$"))

# count()
# Returns the number of times a specified value appears in the sring

txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple"))

# Search from pos 10 to 24
print(txt.count("apple", 10, 24))

# encode()
# Encodes the string, using the specified encoding. If no encoding is specified, defaults to UTF-8

txt = "My name is Ståle"
print(txt)
print(txt.encode())

# Other examples, using ascii
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endswith()
# Returns True if string ends with specified value, otherwise false
txt = "Hello, welcome to my world."
print(txt.endswith("."))

# Accepts a string.
print(txt.endswith("my world."))

print(txt.endswith("my world.", 5, 11))

print(txt.endswith("lo", 1, 5))

# expandtabs()
# Sets the tab size to specified num of whitespaces, default is 8
txt  = "H\te\tl\tl\to "
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# find()
"""
The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
"""
txt = "Hello, welcome to my world."
print(txt.find("welcome"))

# First occurrence of e
print(txt.find("e"))

# Find e when searching between pos 5 and 10
print(txt.find("e",5,10))


# find returns -1
print(txt.find("q"))
# however index returns an exception
#print(txt.index("q"))

# format()

"""
Formatting Types
:< Left aligns the result (within the available space)
:> Right aligns the result (within the available space)
:^ Center aligns the result (within the available space)
:= Places the sign to the left most position
:+ Use a plus sign to indicate if the result is positive or negative
:- Use a minus sign for negative values only
:  Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:, Use a comma as a thousand separator
:_ Use a underscore as a thousand separator
:b Binary format
:c Converts the value into the corresponding unicode character
:d Decimal format
:e Scientific format, with a lower case e
:E Scientific format, with an upper case E
:f Fix point number format
:F Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g General format
:G General format (using a upper case E for scientific notations)
:o Octal format
:x Hex format, lower case
:X Hex format, upper case
:n Number format
:% Percentage format
"""

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = "36")

print(txt1)

print("I would walk a {0:,} miles.".format(1000))
print("{0:.0%}".format(1.0))

print("We have {:^8} chickens".format(49))

# format_map()
# Returns a dictionary key's value
a = {'x':'John', 'y':'Wick'}
print("{x}'s last name is {y}".format_map(a))


"""
The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
Syntax
str.maketrans(x, y, z)
Parameter Values
Parameter 	Description
x 	Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
y 	Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
z 	Optional. A string describing which characters to remove from the original string.
"""
#Use a mapping table to replace many chars, note the string pos of x and y
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

# Use the third param to describe characters to remove from the string
txt = "Good night Sam!"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

# Return the dict describing replacement
print(str.maketrans(x,y,z))

# index()
# Operates almost the same as find, just throws an exception when a match isn't found
txt = "Hello, welcome to my world"
print(txt.index("e"))

# isalnum()
# Check if all chars are alphanumeric, a-z 0-9
txt="GreatAsset"
print(txt.isalnum())

# isalpha()
# Check if all chars are alphabet letters, a-z
print(txt.isalpha())

# isascii()
# Check if all chars are ascii
txt = "Company123"
print(txt.isascii())

# isdecimal()
# Check if all chars are decimals 0-9
print("1234".isdecimal())

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

# isdigit()
# Checks if all chars are digits
print("50800²".isdigit())
print("50800\u00B2".isdigit())

# isidentfiier()
# Check if string is valid identifier for vars, classes, functions etc.
print("toot toot".isidentifier())
print("toot_toot".isidentifier())

# islower()
# Check if all chars are lowercase
print("hey there!".islower())

# isnumeric()
# Check if all characters are numeric.
print("\u00B2".isnumeric())
print("\u00BC".isnumeric())

# isprintable()
# Check if all chars are printable,
print("Hello! Are you there?".isprintable())
print("Hello!\nAre you there?".isprintable())

# isspace()
# Checks if all chars are whitespace
print("\n\t".isspace())

# istitle()
# Checks if all words in text start with uppercase and no others, odd.
print("Hello".istitle())
print("Hello, And Welcome To My World".istitle())
print("Hello there".istitle())

# isupper()
# Checks if string is yelling
print("THIS IS SPARTA!".isupper())

# join()
# join interables into a string with a specified separator

myTuple = ("John","Peter","Vicky")
myList = ["John","Peter","Vicky"]
mySet = {"John","Peter","Vicky"}
myDict = {"Name" : "John", "country" : "Norway"}
print("&".join(myTuple))
print("&".join(myList))
print("&".join(mySet))
print("&".join(myDict)) #dict returns key names not values

# ljust()
# Returns a left adjusted version of the string, defaults to whitespace
print("banana".ljust(20,"O"))

# rjust()
# Same in reverse
print("banana".rjust(20,"O"))

# lower()
# Returns a string in lowercase
print("BANANA".lower().islower())

# lstrip(), rstrip(), strip()
# Accepts chars as acceptable to remove as param
txt = "     banana     "
print(txt.lstrip())
print(txt.lstrip(" a"))
print(txt.rstrip())
print(txt.rstrip("ba "))
print(txt.strip())
print(txt.strip("b "))

# partition()
# Returns a tuple where the first element contains the part before the string, then the matching element of the
# specified string, and the third containing the part after the match.
print("I could eat bananas and more bananas all day".partition("bananas")) #first occurence of specified string
# with no match the first element contains the full string with the rest being empty
print(txt.partition("apples"))

# rpartition()
# And from the right now
print("I could eat bananas and more bananas all day".rpartition("bananas")) #first occurence of specified string
# with no match the first two elements are empty with the last containing the full string
print(txt.rpartition("apples"))

# rfind()
# Returns the last occurrence of the specified value
txt = "Mi casa, su casa."
print(txt.rfind("casa"))

# rindex()
# Same rules and difference between find and index, raises an exception vs -1 being returned with rfind
print(txt.rindex("casa"))

# split()
# Ever try to write a csv parser?
# Splits a string into a list, defaults to whitespace as a separator
# Accepts a second parameter, maxsplit which specifies how many splits to perform. Default is -1 which is all occurrences

txt = "hello, my name is Peter, I am 26 years old"
print(txt.split(", "))
print(txt.split(", ",1))

# rsplit()
# Same thing in reverse
print(txt.rsplit(", "))
print(txt.rsplit(", ",1))

# splitlines()
# splits a string into a list at linebreaks, accepts a bool as a param on whether to keep linebreaks

txt = "Here we\n\ngo again!"
print(txt.splitlines())
print(txt.splitlines(True))

# startswith()
# Returns true if string starts with specified value, accepts position params
print(txt.startswith("Here"))
print(txt.startswith("we",5))
print(txt.startswith("we",5,7))
print(txt.startswith("we",6,8))

# swapcase()
# Returns a string with the case inverted
txt = "Hello My Name Is PETER"
print(txt.swapcase())

# title()
# Returns a string where the first character of each word is uppercase
print(txt.title())
# Note that the first letter after a non-alpha char is converted to uppercase as well
print("hello b2b2b2 and 3g3g3g".title())

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# maketrans()

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# upper()
# Uppercase all the things
print("all the things!".upper())

# zfill()
# Fill a string with leading zeros of a given count, if the given lenght is less than the full string, no fill is done

print("50".zfill(10))
print("50".zfill(2))
