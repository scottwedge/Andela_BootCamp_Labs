import unittest, sqlite3
from create_event import create_event

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

class TestInitialClass(unittest.TestCase):
    def test_pass(self):
         self.assertEqual(True,True)




if __name__ == "__main__":
	unittest.main()
