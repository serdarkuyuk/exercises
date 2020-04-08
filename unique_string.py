from time_decorator import timeit
'''
Given a string, are all characters unique?
should give a True or False return
using python built in functions
'''
@timeit
def find_unique_string(a_string):
	my_dict = {}
	for el in a_string:
		if el not in a_string:
			my_dict[el] = 1
		else:
			return False
	return True

@timeit
def find_unique_string_v1(a_string):
	my_set = set()
	for el in a_string:
		if el not in a_string:
			my_set.add(el)
		else:
			return False
	return True

@timeit
def find_unique_string_v2(a_string):
	return len(set(a_string)) == len(a_string)


inputs = "abcdefghijklmnopqrstvwyz"*10000000
print(find_unique_string(inputs))
print(find_unique_string_v1(inputs))
print(find_unique_string_v2(inputs))