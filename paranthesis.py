from stack_file import Stack 

def is_balanced(a_strin):
	'''
	This solution is done using stack class written separetely
	Calliing from stack_file
	'''
	my_dict = {"(":")","{":"}","[":"]"}
	p_open = "({["
	p_close = ")}]"

	s = Stack()

	for el in a_strin:
		if el in p_open:
			s.push(el)
		else:
			if s.is_empty():
				return False
				break
			else:
				if el == my_dict[s.peek()]:
					s.pop()

	if s.is_empty():
		return True
	return False

def is_balanced_v2(a_strin):


	'''
	This version is using list data structure 
	'''

	my_dict = {"(":")","{":"}","[":"]"}
	p_open = "({["
	p_close = ")}]"

	new_list = []
	for el in a_strin:
		if el in p_open:
			new_list.append(el)
		else:
			if not new_list:
				return False
				break
			else:
				if el == my_dict[new_list[-1]]:
					new_list.pop()

	if not new_list:
		return True
	return False

tsst = "(([]))))"
print(is_balanced(tsst))
print(is_balanced_v2(tsst))