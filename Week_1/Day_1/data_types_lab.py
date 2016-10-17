def data_type(data):
	if type(data) is str:
		return len(data)
	elif data is None:
		return 'no value'
	elif type(data) is bool:
		return data
	elif type(data) is int:
		if data > 100:
			return 'more than 100'
		elif data < 100:
			return 'less than 100'
		else:
			return 'equal to 100'
	elif type(data) is list:
		if (len(data)) >= 3:
			return data[2]
		else:
			return None