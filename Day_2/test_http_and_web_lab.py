import unittest
from http_and_web_lab import get_weather

class OpenWeatherApiTests(unittest.TestCase):

	def test_get_weather(self):
		self.assertTrue(get_weather('Nairobi') is dict, msg= 'The funtion does not return a dict')







if __name__ == '__main__':
	unittest.main()