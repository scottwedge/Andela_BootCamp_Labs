class BinarySearch(list):
	"""docstring for BinarySearch"""
	def __init__(self, a, b):
		self.length = a
		self.step = b

	def search(self, value):
		index = 0
		for item in self:
			if value == item:
				break
			else:
				index += 1
		return {'count':index}