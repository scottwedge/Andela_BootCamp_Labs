import sqlite3, time, datetime

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()


# Creates events using according to the args provided
def create_event(name, start_date, end_date, venue):
	start_day, start_month, start_year = start_date.split('-')
	end_day, end_month, end_year = end_date.split('-')
	unix_startime = datetime.date(int(start_year), int (start_month), int(start_month))
	unix_endtime = datetime.date(int(end_year), int (end_month), int(end_day))

	if (unix_startime > unix_endtime):
		print ("End date cannot occur before start date")
		return False

	else:
		c.execute("INSERT INTO events (event_name, event_start_date, event_end_date, event_venue) VALUES (?, ?, ?, ?)" , 
			(name, start_date, end_date, venue))
		conn.commit()
		print ('''The following event has been added to the database
			Name: 			%s
			Start Date:	%s
			End Date: 		%s
			Venue: 			%s''' %(name, start_date, end_date, venue))
		return True


# Views all events
def view_all_events():
	c.execute("SELECT * FROM events")
	events_data = c.fetchall()
	print('Event ID\tName\t\t\tStart Date\tEnd Date\tVenue')
	for row in events_data:		
		print(str(row[0]) + '\t\t' + row[1] + '\t\t' + row[2] + '\t' + row[3] + '\t' + row[4])

	return True
		


# Edits events according using the event ID
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
		print(str(row[0]) + '\t\t' + row[1] + '\t\t' + row[2] + '\t' + row[3] + '\t' + row[4]+'\n')

		user_response = input ("Do you want to edit the event above? Enter 'Y' to edit or any other key to cancel: ").lower()

		if user_response == 'y':
			print ("\nPlease input the new event details below")
			new_name = input ("What is the new name of the event?: ")
			new_start_date = input ("What is the new start date? (format DD-MM-YYYY): ")
			new_end_date = input ("What is the new end date? (format DD-MM-YYYY): ")
			new_venue = input ("What is the new venue: ")

			c.execute ("UPDATE events SET event_name = ?, event_start_date = ?, event_end_date = ?, event_venue = ? WHERE event_ID = ? ", 
				(new_name, new_start_date, new_end_date, new_venue, int(event_ID)) )

			conn.commit()

			print ("\nEdit made successfully")
			c.execute("SELECT * FROM events WHERE event_ID=?", (int(event_ID),))
			print('Event ID\tName\t\tStart Date\tEnd Date\tVenue')
			row = c.fetchone()
			print(str(row[0]) + '\t\t' + row[1] + '\t' + row[2] + '\t' + row[3] + '\t' + row[4])
			return True

		else:
			print ("Edit cancelled successfully")
			return False

# Deletes events based on the event ID
def delete_event (event_ID):
	c.execute("SELECT * FROM events WHERE event_ID = ?", (int(event_ID),))
	data = c.fetchall()

	if len(data) == 0:
		print ("There no event with event ID " + str(event_ID))


	else:
		print (str(data))
		user_response = input("Do you want to delete the following event? Enter 'Y' to delete or any other key to cancel this deletion: ").lower()
		
		# Checks users response to confirm deletion
		if user_response == 'y':
			c.execute ("DELETE FROM events WHERE event_ID = ?", (int(event_ID),))
			conn.commit()
			print ("Event successfully deleted")

		else:
			print ("Event not deleted")