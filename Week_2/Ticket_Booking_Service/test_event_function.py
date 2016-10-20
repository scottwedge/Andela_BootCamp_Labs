import unittest, sqlite3, time, datetime
from event_functions import create_event, view_all_events, edit_event, delete_event
from unix_time_conversions import unix_to_readable, readable_to_unix

conn = sqlite3.connect('test_dummy_data.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS events (event_ID INTEGER PRIMARY KEY AUTOINCREMENT, event_name TEXT, event_start_date REAL, event_end_date REAL, event_venue TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS tickets (ticket_ID INTEGER PRIMARY KEY AUTOINCREMENT, event_ID INTEGER, email_address TEXT, ticket_status BOOLEAN NOT NULL CHECK(ticket_status IN (0,1)), ticket_time_stamp REAL)")


class EventFunctionsTests(unittest.TestCase):
	self.event_name = 'Test Event'
	self.event_start_date = readable_to_unix(4-5-2010)
	self.event_end_date = readable_to_unix(5-5-2010)
	self.event_venue = 'Test Venue'

	def test_create_event(self):
		self.assertTrue(create_event(self.event_name, self.event_start_date, self.event_end_date, self.event_venue), msg = 'Event create not returning True when after successful completion')

		#c.execute ("SELECT * FROM events WHERE")



if __name__ = '__main__':
	unittest.main()