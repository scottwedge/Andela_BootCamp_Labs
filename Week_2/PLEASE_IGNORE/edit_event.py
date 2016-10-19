import sqlite3

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()


def edit_event(event_ID):
	c.execute("SELECT * FROM events WHERE event_ID=?", (int(event_ID),))
	row = c.fetchone()
	

	if row == None:
		# If the event ID cannot be found
		print('There is no event with event ID ' + str(event_ID))
		return False
	else:
		# Shows the current event details
		print('Events found with event ID ' + str(event_ID) + ' : ')
		print('Event ID\tName\t\t\tStart Date\tEnd Date\tVenue')
		print(str(row[0]) + '\t\t' + row[1] + '\t\t' + row[2] + '\t' + row[3] + '\t' + row[4])

		print ("\nPlease input the new event details below")
		new_name = input ("What is the new name of the event?: ")
		new_start_date = input ("What is the new start date? (format DD-MM-YYYY): ")
		new_end_date = input ("What is the new end date? (format DD-MM-YYYY): ")
		new_venue = input ("What is the new venue: ")

		c.execute ("UPDATE events SET event_name = ?, event_start_date = ?, event_end_date = ?, event_venue = ? WHERE event_ID = ? ", 
			(new_name, new_start_date, new_end_date, new_venue, int(event_ID)) )

		conn.commit()

		print ("Edit made successfully")
		print('Event ID\tName\t\tStart Date\tEnd Date\tVenue')
		print(str(row[0]) + '\t\t' + row[1] + '\t' + row[2] + '\t' + row[3] + '\t' + row[4])
		return True

	