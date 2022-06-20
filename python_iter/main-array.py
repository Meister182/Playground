#!/bin/python3

# Exprimenting with __iter___ dunder method.

# A basic class that holds a list
class my_basic_iterator:
	def __init__(self, some_list):
		self.list = some_list
	def __iter__(self):
		# initialize iterator
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self.list):
			value = self.list[self.index]
			self.index += 1
			return value
		else:
			# Stop loop
			raise StopIteration

mc = my_basic_iterator(['a','b','c'])
for i in mc:
	print(i)
