#!/bin/python3

class Foo:
    def __init__(self):
        self.__some_dict = {'a':1, 'b':2}

    @property
    def a(self):
        return self.__some_dict.get('a', None)
    
    @a.setter
    def a(self, value):
       self.__some_dict['a'] = value
    
    @property
    def b(self):
        return self.__some_dict.get('b', None)


f = Foo()
print(f"{f.a = }")
f.a = "asd"
print(f"{f.a = }")

print(f"{f.b = }")

# Fails: AttributeError: can't set attribute
# f.b = "asd"

# Fais: AttributeError: 'Foo' object has no attribute '__some_dict'
# f.__some_dict['b'] = "dsa"
# print(f"{f.b = }")
