class Telephone(object):
	"""docstring for Telephone"""
	def __init__(self):
		pass

	def place_call(self, phone_number):
		print ('Hold on a minute. Calling...' + str(phone_number))

	def description(self):
		print('This is a basic phone that only has the ability to place calls')

class MobilePhone(Telephone):
	"""docstring for CellPhone"""
	type = 'cellular phone'
	def __init__(self, manufacturer, model):
		self.manufacturer = manufacturer
		self.model = model
		self.call_log = []
		self.phone_book = {'Default ISP Num': '0000'}

	def place_call(self, phone_number):
		# add to call log
		self.call_log.append(phone_number)
		print('Calling ' + str(phone_number))

	def send_sms(self, num, text):
		print('Sending ' + text + ' to' + str(num))

	def add_num_to_phonebook(self, name, num):
		if num in self.phone_book.values():
			print (str(num) + ' is already in the phone book')
			return False
		else:
			self.phone_book.update({name:num})
			print (str(num) + ' saved in the phonebook under the name ' + name)
			return True

class SmartPhone(MobilePhone):
	"""docstring for Smartphone"""
	def __init__(self, manufacturer, model):
		self.manufacturer = manufacturer
		self.model = model
		self.call_log = []
		self.phone_book = {'Default ISP Num': '0000'}
		self.installed_apps = []
	def install_app(self, app):
		if app not in installed_apps:
			installed_apps.append (app)
			print('Completed installing ' + str(app))
		else:
			print('The app is already installed')

		