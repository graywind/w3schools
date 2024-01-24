#!/usr/bin/env python3
"""
Section Name: Python Classes and Objects
URL: https://www.w3schools.com/python/python_classes.asp
"""

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#playing with the builtins and adding a method

class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
  def hello(self):
    print("Hello my name is " + self.name)

p1 = Person(name = "John", age = 36)

print(p1)
p1.hello()

p1.age = 25
p1.name = "Sean"

p1.hello()
print(p1)
class Empty:
  pass
