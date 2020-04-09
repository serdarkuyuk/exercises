'''
use stack data structure to convert integer values to binary
'''
from stack_file import Stack



def make_binary(num):

	ob = Stack()

	while num > 0:
		remainder = num % 2
		ob.push(remainder)
		num = num // 2

	strings = ''
	while not ob.is_empty():
		strings += str(ob.pop())

	return strings
	
print(make_binary(242))
