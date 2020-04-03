

def rotation_func(list1, list2):
	''''
	Return True if two list is rationtion. False otherwise 
	'''

	if len(list1) != len(list2):
		return False

	key1 = 0

	for index, num in enumerate(list2):
		if num == list1[key1]:
			key2 = index
		else:
			return False

	for i in range(len(list1)):

		n_index1 = key1+i 
		n_index2 = (key2+i) % len(list2)	

		if list1[n_index1] != list2[n_index2]:
			return False
		
	return True


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [6, 7, 1, 2, 4, 3, 5]

print(rotation_func(list1,list2))