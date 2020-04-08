from collections import Counter, defaultdict
from time_decorator import timeit

'''
Given an array what is the most feequently 
occuring element
'''

#best way
@timeit
def find_freq_elem(a_list):
	return(Counter(a_list).most_common(1)[0][0])

#better way
@timeit
def find_freq_elem_v2(a_list):
	d = defaultdict(int)
	for el in a_list:
		d[el] += 1
	return d.items()

#bad way
@timeit
def find_freq_elem_v3(a_list):
	count = {}
	max_count = 0
	max_item = None

	for el in a_list:
		if el not in count:
			count[el] = 1
		else:
			count[el] += 1

		if count[el] > max_count:
			max_count = count[el]
			max_item = el

	return max_item, max_count

my_list = [1, 2, 3, 4, 1, 2, 1]*1000000

print(find_freq_elem(my_list))
print(find_freq_elem_v2(my_list))
print(find_freq_elem_v3(my_list))