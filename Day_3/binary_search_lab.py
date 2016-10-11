class BinarySearch(list):
	"""docstring for BinarySearch"""
	def __init__(self, a, b):
		self.length = a
		self.step = b
		for i in range(self.step, (self.length*self.step)+1, self.step):
			self.append(i) 

	def search(self, value):
		first_index = 0
		last_index = self.length - 1
		count = 0
		index = -1
		found_value = False
		while first_index <= last_index and not found_value:
			midpoint = (first_index + last_index)//2
			if self[midpoint] == value:
				count += 1
				index = midpoint
				found_value = True
			else:
				count += 1
				if value < self[midpoint]:
					last_index = midpoint - 1
				else:
					first_index = midpoint + 1
		return {'count': count, 'index': index}