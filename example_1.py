
def is_odd(my_list):
	'''
	Converts list to a list contain True if number is odd
	and False it is even
	'''
	new_list=[]
	for i in my_list:
		if i % 2 == 1:
			new_list.append(True)
		else:
			new_list.append(False)
	return new_list

def my_func(a_func, a_list):
	'''
	this function gets a function and list and returns
	applying it

	'''
	
	solution = a_func(a_list)

	list_im = []
	for index, bul in enumerate(solution):
		
		if bul == True:
			list_im.append(a_list[index])
	return list_im


my_list = range(1, 100)
p_list = my_func(is_odd, my_list)
print(p_list)