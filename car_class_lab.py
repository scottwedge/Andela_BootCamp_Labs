class Car(object):
	
	# Defaults to General and GM if no arguments are provided
	def __init__(self, name = 'General', model = 'GM', car_type = 'saloon'):
		self.name = name
		self.model = model
		self.car_type = car_type
		self.speed = 0
	
		# Checks if the name is Porshe or Koenigsegg and changes
		# number of doors to 2
		if (self.name == 'Porshe' or self.name == 'Koenigsegg'):
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		# Wheels check for trailers
		if (self.car_type == 'trailer'):
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

	# Saloon Check
	def is_saloon(self):
		if self.car_type == 'saloon':
			return True
		else:
			return False

	# Speed method
	def drive(self, desired_speed):
		if (self.car_type == 'trailer'):
			self.speed = desired_speed * 11
			return self
		else:
			self.speed = 10 ** desired_speed
			return self