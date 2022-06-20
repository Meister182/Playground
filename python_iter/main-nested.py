#!/bin/python3
# Experimenting with __iter__ and __next__ dunder methods.

# An iterable class which hold other iterable objects.


from curses import can_change_color

from pyparsing import line


class changed_file:
    def __init__(self, file_name, changed_lines) -> None:
        self.__file_name = file_name
        if isinstance(changed_lines, list):
            self.__changed_lines = [[line, 'NA'] for line in changed_lines]
        else:
            self.__changed_lines = [[changed_lines, 'NA']]

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index < len(self.__changed_lines):
            line = self.__changed_lines[self.__index][0]
            return line
        else:
            self.__index = -1
            raise StopIteration

    def set_line_OK(self):
        # Cannot be changed if already set to "NOK"
        if self.__index >= 0 and self.__changed_lines[self.__index][1] != "NOK":
            self.__changed_lines[self.__index][1] = "OK"

    def set_line_NOK(self):
        if self.__index >= 0:
           self.__changed_lines[self.__index][1] = "NOK"

    def get_status(self):
        status = "OK"
        for changed_line, line_status in self.__changed_lines:
            if line_status == "NOK":
                return "NOK"
            if line_status == "NA":
                status = "NA"
        return status

    def get_file_name(self):
        return self.__file_name
    
    def get_changes(self):
        return [line[0] for line in self.__changed_lines]

class Commit:
    def __init__(self, commit_dic) -> None:
        self.__changes = [changed_file(k,v) for k,v in commit_dic.items()]
    
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index < len(self.__changes):
            return self.__changes[self.__index]
        else:
            raise StopIteration

    def get_status(self):
        status = "OK"
        for change in self.__changes:
            change_status = change.get_status()
            if change_status == "NOK":
                return "NOK"
            if change_status == "NA":
                status = "NA"
        return status

some_dict = {
	'a':1,
	'b':2,
	'c':[1,2],
	'd': 4,
	'e': [5,6],
	'f': 8,
	}

commit = Commit(some_dict)

# Validation
for change in commit:
    for changed_line in change:
        print(f'validatin: {change.get_file_name()} -> {changed_line}')
        if changed_line == 4:
            change.set_line_OK()
        elif changed_line < 4:
            change.set_line_NOK()
        # change.set_line_OK()

# Results
for change in commit:
    print(f'{change.get_status()} -> {change.get_file_name()} :  {change.get_changes()}')

# Overall result
print(f'commit overall status -> {commit.get_status()}')