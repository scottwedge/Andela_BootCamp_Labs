import unittest
from OOP_lab import Telephone, MobilePhone, SmartPhone

class OOPLabTest(unittest.TestCase):

	def test_instance_and_attributes(self):
		self.simple_telephone = Telephone()
		self.nokia = MobilePhone('Nokia', '3310')
		self.iphone = SmartPhone('Apple', 'iPhone')

		# Checking instances
		self.assertIsInstance(self.simple_telephone, Telephone, msg='simple_telephone is not an instance of class Telephone')
		self.assertIsInstance(self.nokia, MobilePhone, msg='Nokia is not an instance of class MobilePhone')
		self.assertIsInstance(self.iphone, Telephone, msg='iPhone is not an instance of class SmartPhone')

		#Checking attributes
		self.assertEqual(self.nokia.manufacturer, 'Nokia', msg= 'Nokia not showing as manufacturer')
		self.assertEqual(self.iphone.model, 'iPhone', msg= 'iphone not showing as iPhone as model')

	def test_place_call(self):
		self.nokia = MobilePhone('Nokia', '3310')
		self.iphone = SmartPhone('Apple', 'iPhone')
		self.nokia.place_call(123)
		self. iphone.place_call(999)
		self.assertTrue(123 in self.nokia.call_log)
		self.assertTrue(999 in self.iphone.call_log)

	def test_phonebook(self):
		self.nokia = MobilePhone('Nokia', '3310')
		self.iphone = SmartPhone('Apple', 'iPhone')
		nokia_response = self.nokia.add_num_to_phonebook('Guy', 456)
		iphone_response = self.iphone.add_num_to_phonebook('Guy', '0000')
		self.assertTrue(nokia_response, msg = 'Number not added to nokia phonebook')
		self.assertFalse(iphone_response, msg = 'iPhone should not able to save the same number twice')








if __name__ == '__main__':
  unittest.main()