#!/bin/python3
import re

# Trying to expand the string object.
#
#   - The main idea is to be able to feed instances of my class to functions that
#   consume str objects.
#
#   - Also this allows to create a custom str with custom methods and propreties.
#
#   *- Its even possible to redifine private dunders.
#   *- Not sure if this could mess other logics, but seems to work fine.

#

class my_string(str):
    def __new__(cls, str_content, *args, **kwargs):
        # explicitly only pass value to the str constructor
        return super(my_string, cls).__new__(cls, str_content)

    def __init__(self, str_content, other_info = "UNDEFINED") -> None:
        self.__other_info = other_info

    def get_other_info(self):
        return self.__other_info
    
    def set_other_info(self, other_info):
        self.__other_info = other_info

    # Its even possible to redifine private dunders.
    # Not sure if this could mess other logics, but seems to work fine.
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index < len(self.__other_info):
            return self.__other_info[self.__index]
        else:
            self.__index = -1
            raise StopIteration


pattern = ".*"
# ---- Teste normal string ----
normal_string = "some text"
match = re.match(pattern, normal_string)
print(f'normal string : {normal_string}')
print(f'teste match   : {match}')
print('-'*20)

# ---- Teste my string -----
_my_string = my_string(normal_string)
match = re.match(pattern, _my_string)
print(f'my string     : {_my_string}')
print(f'teste match   : {match}')
print(f'hidden info 1 : {_my_string.get_other_info()}')
_my_string.set_other_info("NEW INFO")
print(f'hidden info 2 : {_my_string.get_other_info()}')

# ---- Test looping ----
for i in _my_string:
    print(i)