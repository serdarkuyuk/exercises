from collections import defaultdict
'''
non reeat element
Taka a string and return character that never repats
if multiple uniques then return only the first unique
'''

def non_repeting_string(a_string):
	my_dict = {}
	for el in a_string:
		if el not in my_dict:
			my_dict[el] = 1
		else:
			my_dict[el] += 1

	for k, v in my_dict.items():
		if v == 1:
			return k

def non_repeting_string_v2(a_string):
	my_dict = defaultdict(int)
	for el in a_string:
		my_dict[el] += 1

	for k, v in my_dict.items():
		if v == 1:
			return k


text = "ahmetlme"
print(non_repeting_string(text))
print(non_repeting_string_v2(text))

