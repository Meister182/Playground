#!/bin/python3

# Exprimenting with __repr__ and __str__  dunder methods.

class myClass:
    def __init__(self, val1, val2) -> None:
        self.__val1 = val1
        self.__val2 = val2

    def __repr__(self) -> str:
        return f'repr: myClass({self.__val1}, {self.__val2})'

    def __str__(self):
        return "str: myClass str form"


mc = myClass(1,2)
mc2 = myClass(3,4)
print(mc)               # triggers string form
print(f'fstring {mc}')  # triggers string form
print(repr(mc))         # triggers repr form
print([mc, mc])         # calls repr for array elements


print("-"*15, "nested Classes", "-"*15)
class ClassHolder:
    def __init__(self, input_list) -> None:
        self.__input = input_list
        self.__mcs = [myClass(v1,v2) for v1,v2 in input_list]

    def __str__(self) -> str:
        return f'str: ClassHolder({self.__mcs})'
    
    def __repr__(self) -> str:
        return f"repr: ClassHolder({self.__input})"

cH = ClassHolder([(1,2), (3,4), (5,6)])
# 1st - Calls ClassHolder str
# 2nd - ClassHolder str tries to print an array of myClass's
# 3th - so calls it calls the repr of each one
print(cH)