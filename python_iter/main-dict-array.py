#!/bin/python3
# Experimenting with __iter__ and __next__ dunder methods.

#  A more complex class able to iterate over (key, value) pairs, keys, or values 
# unpacking array elements.

# Observations:
#	- It seems from dict, that instead of implementing this logic it simply 
# 	returns and iterable object.
#
#	- This could be usefull to run a method on for a specific element, for example
#	tagging a value. Because one could call an instance method and the instance 
# 	as access to the loop information through the indexes.
#
#	- We need to take into account if the indexes are updated at the start or
#	at the end of the next calls, in order to know which element of the loop
#	is currently being used.
#
#	- This seems overcomplicated, probably not the best approach. 
# 	But it was fun. ¯\_(ツ)_/¯
#
#	- The simples most elegante way is likely to expand on the dict object, For
# 	sure it will be a future experiment. :)

class my_dict_iterator:
	__KEYS = "KEYS"
	__VALS = "VALS"
	def __init__(self, some_dict):				
		self.dict = some_dict
		self.__list_of_keys = list(self.dict)
		self.__next_mode = ""

	def keys(self):
		print("keys()")
		self.__next_mode = self.__KEYS
		return self

	def values(self):
		print("values()")
		self.__next_mode = self.__VALS
		return self

	def __iter__(self):
		print("__iter__()")
		self.__index_key = 0
		self.__index_val = 0
		return self

	def __next__(self):
		print("__next__()")
		next_call_map = {
			self.__KEYS: self.__next_key,
			self.__VALS: self.__next_val,
		}
		if self.__index_key < len(self.__list_of_keys):
			return next_call_map.get(self.__next_mode, self.__next_default)()
		else:
			self.__next_mode = ""
			raise StopIteration

	def __next_default(self):
		print("__next_default()")
		next_key_value = list(self.dict.items())[self.__index_key]
		self.__index_key += 1
		return next_key_value

	def __next_key(self):
		print("__next_key()")
		next_key = self.__list_of_keys[self.__index_key]
		self.__index_key += 1
		return next_key

	def __next_val(self):
		print("__next_val()")
		next_key = self.__list_of_keys[self.__index_key]
		next_value = self.dict[next_key]

		if isinstance(next_value, list):
			next_value = self.__next_value_list(next_value)
		else:
			self.__index_key += 1
		
		return next_value

	def __next_value_list(self, next_value):
		print("__next_values_list()")
		if self.__index_val < len(next_value):
			# Fetch list next element
			next_value = next_value[self.__index_val]
			self.__index_val += 1
			return next_value
		else:
			# Increment key index and retrigger __next__ method
			self.__index_key += 1
			self.__index_val = 0
			return self.__next__()

	def get_current_iteration_key(self):
		print("get_curr_key()")
		# Only makes sense calling this while the loop is running
		if self.__index_val:
			#  When index_val > 0 we are iterating a list and the key is not
			# incremented 
			return self.__list_of_keys[self.__index_key]
		else:
			return self.__list_of_keys[self.__index_key -1]

	def get_current_iteration_value(self):
		print("get_curr_val()")
		# Only makes sense calling this while the loop is running
		key = self.get_current_iteration_key()
		return self.dict[key]

# ===== main =====
some_dict = {
	'a':1,
	'b':2,
	'c':[1,2],
	'd': 4,
	'e': [5,6],
	'f': 8,
	}
md = my_dict_iterator(some_dict)

print("-"*30)
for key, value in md:
	print(f'#### : {key} -> {value}')

print("-"*30)
for key in md.keys():
	print(f'#### : {key} -> {md.get_current_iteration_value()}')

print("-"*30)
for value in md.values():
	print(f'#### : {md.get_current_iteration_key()} -> {value}')
