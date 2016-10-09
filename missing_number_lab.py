def find_missing(list1,list2):
	missing = 0
	if len(list1) > len(list2):
		longer_list = list1
		shorter_list = list2
	else:
		longer_list = list2
		shorter_list = list1

	for val in longer_list:
		if val not in shorter_list:
			missing = val

	return missing

