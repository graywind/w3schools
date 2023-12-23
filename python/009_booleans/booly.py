#!/usr/bin/env python3
"""
Section Name:
URL: https://www.w3schools.com/python/
"""
#Expressions are evaluated and return a bool
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Non empty values return True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#Empty values, null, or naturally false (0vs1) return False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


"""
One more value, or object in this case, evaluates to False, and
that is if you have an object that is made from a class with a
__len__ function that returns 0 or False:
"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

def truthy():
    return True

print(truthy())

def myFunction() :
  return True

if myFunction():
  print("DO THE THING!")
else:
  print("NO!")
