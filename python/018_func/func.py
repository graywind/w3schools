#!/usr/bin/env python3
"""
Section Name: Python Functions
URL: https://www.w3schools.com/python/python_functions.asp
"""

"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""

def funcy():
  print("Doing the needful")

def funky(doit):
  print("Doing the {}".format(doit))

def business():
  x = "needful."
  return x

funky(doit = business())

"""
Number of Arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less. 
"""

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Arbitrary Arguments. If you don't know how many args will be passed into the function, add a * before the param name in the function def.
#This way the function will receive a tuple of args and can access them accordingly.

#Went off course since I wanted the index in the for loop
#ended up at https://stackoverflow.com/questions/522563/how-to-access-the-index-value-in-a-for-loop

"""
Use the built-in function enumerate():

for idx, x in enumerate(xs):
    print(idx, x)

It is non-pythonic to manually index via for i in range(len(xs)): x = xs[i] or manually manage an additional state variable.

Check out PEP 279 (https://docs.python.org/3/library/functions.html#enumerate) for more.
"""



def trouble(*double):
  for idx, x in enumerate(double,start=1):
    print(str(idx) + " " + x)

trouble("Emil","Tobias","Linus")

"""
Keyword Arguments

You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
"""


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

"""
Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#default param value example

def my_function(country = "a far away place"):
  print("I am from " + country)

my_function()

#pass keyword can be used as a function cannot be empty
def my_function():
  pass

#Positional only arguments, to enforce add ", /" after the args

def my_function(x, /):
  print(x)

my_function(3)

#Ensures below cannot be used and throws
#my_function(x = 3)

#Keyword only args, add "*, " before the args

def my_function(*,x):
  print(x)
my_function(x = 3)

#Combining positional only and keyword only
#Any arg before the / , are positional only and any arg after the *, are keyword only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


"""
Recursion

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a
function which never terminates, or one that uses excess amounts of memory or processor power.
However, when written correctly recursion can be a very efficient and mathematically-elegant
approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We
use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends
when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out
is by testing and modifying it.
"""

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(20)
