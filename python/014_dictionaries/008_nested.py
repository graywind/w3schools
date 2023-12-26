#!/usr/bin/env python3
"""
Section Name: Python - Nested Dictionaries
URL: https://www.w3schools.com/python/python_dictionaries_nested.asp
"""

#One shot nested dictionary
myfamily = {
  "child1" : {
    "name": "Emil",
    "year" : 2004
  },
  "child2" : {
    "name": "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name": "Linus",
    "year" : 2011
  }
}

print(myfamily)
del myfamily
#it is also possible to add three dictionaries into a new dictionary

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#accessing a nested dict
print(myfamily["child1"]["year"])
print(myfamily["child1"].items())
