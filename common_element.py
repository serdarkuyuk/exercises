


def common_elem(list1, list2):
	ind_l1 = 0
	ind_l2 = 0
	out_list = []


	while ind_l1 < len(list1) and ind_l2 < len(list2):

		if list1[ind_l1] == list2[ind_l2]:
			out_list.append(list1[ind_l1])
			ind_l2 += 1
			ind_l1 += 1

		elif list1[ind_l1] > list2[ind_l2]:
			ind_l2 += 1

		elif list1[ind_l1] < list2[ind_l2]:
			ind_l1 += 1

	return out_list

def common_elem_set(list1, list2):
	return list(set(list1).intersection(set(list2)))


list1 = [1, 3, 4, 6, 7, 9]
list2 = [1, 2, 4, 5, 9, 10]

print(common_elem(list1, list2))
print(common_elem_set(list1, list2))