#!/bin/python3

# Exprimenting with __iter___ dunder method.

# A more complex class that holds a dictionary
class my_dict_iterator:
	def __init__(self, some_dict):
		self.dict = some_dict

	def values(self):
		return self.dict.values()

	def __iter__(self):
		self._index = 0
		return self

	def __next__(self):
		if self._index < len(self.dict):
			next_value = list(self.dict.items())[self._index]
			self._index += 1
			return next_value
		else:
			raise StopIteration

some_dict = {'a':1,'b':2,'c':[1,2]}
md = my_dict_iterator(some_dict)

for key, value in md:
	print(f'{key} -> {value}')

for value in md.values():
	print(f'-> {value}')