import sqlite3

conn = sqlite3.connect('test_data.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS events (event_ID INTEGER PRIMARY KEY AUTOINCREMENT, event_name TEXT, event_start_date REAL, event_end_date REAL, event_venue TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS tickets (ticket_ID INTEGER PRIMARY KEY AUTOINCREMENT, event_ID INTEGER, email_address TEXT, ticket_status BOOLEAN NOT NULL CHECK(ticket_status IN (0,1)), ticket_time_stamp REAL)")

'''
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS test_table (textCol TEXT, numCol INT)")


def manual_data_entry():
	c.execute("INSERT INTO test_table VALUES ('Some Text', 5)")
	conn.commit()


create_table()
manual_data_entry()'''
