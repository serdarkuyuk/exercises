from collections import Counter	

my_list = [1, 2, 3, 4, 1, 2, 1]

def find_freq_elem(a_list):
	return(Counter(a_list).most_common(1)[0][0])

print(find_freq_elem(my_list))