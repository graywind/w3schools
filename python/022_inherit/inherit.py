#!/usr/bin/env python3
"""
Section Name: Python Inheritance
URL: https://www.w3schools.com/python/python_inheritane.asp
"""

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#playing with the builtins and adding a method

class Person:
  def __init__(self,fname,lname,age):
    self.firstname = fname
    self.lastname = lname
    self.age = age
  def __str__(self):
    return f"{self.firstname} {self.lastname}({self.age})"
  def hello(self):
    print("Hello my name is " + self.firstname)

p1 = Person(fname = "John",lname="Long",age = 36)

print(p1)
p1.hello()

p1.age = 25
p1.fname = "Sean"

p1.hello()
print(p1)
class Empty:
  pass

#End of almost copy of class session

class Student(Person):
  def __init__(self, fname, lname, age, year):
    super().__init__(fname,lname,age)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Waldo","Gibson",35,2019)

x.hello()
x.welcome()
