import sqlite3

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

def view_all_events():
	c.execute("SELECT * FROM events")
	events_data = c.fetchall()
	print('Event ID\tName\t\t\tStart Date\tEnd Date\tVenue')
	for row in events_data:		
		print(str(row[0]) + '\t\t' + row[1] + '\t\t' + row[2] + '\t' + row[3] + '\t' + row[4])

	return True
		
