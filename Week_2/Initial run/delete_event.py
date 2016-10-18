import sqlite3

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

def delete_event (event_ID):
	c.execute("SELECT * FROM events WHERE ")