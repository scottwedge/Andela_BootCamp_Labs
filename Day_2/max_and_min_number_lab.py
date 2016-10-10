def find_max_min(list_of_numbers):
	sorted_list = sorted(list_of_numbers)
	min = sorted_list[0]
	max = sorted_list[-1]
	if min == max:
		return [len(sorted_list)]
	else:
		return [min, max]