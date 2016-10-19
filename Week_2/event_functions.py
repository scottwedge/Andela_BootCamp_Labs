import sqlite3, time, datetime
from unix_time_conversions import unix_to_readable, readable_to_unix

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()


# Creates events using according to the args provided
def create_event(name, start_date, end_date, venue):

	c.execute("INSERT INTO events (event_name, event_start_date, event_end_date, event_venue) VALUES (?, ?, ?, ?)" , 
		(name, start_date, end_date, venue))
	conn.commit()
	print ('''The following event has been added to the database
		Name: 			%s
		Start Date:		%s
		End Date: 		%s
		Venue: 			%s''' %(name, unix_to_readable(start_date), unix_to_readable(end_date), venue))
	return True


# Views all events
def view_all_events():
	c.execute("SELECT * FROM events")
	events_data = c.fetchall()
	print('Event ID\tName\t\t\tStart Date\tEnd Date\tVenue')
	for row in events_data:
		if len(row[1])>15:
			print(str(row[0]) + '\t\t' + row[1] + '\t' + unix_to_readable(row[2]) + '\t' + unix_to_readable(row[3]) + '\t' + row[4])
		else:		
			print(str(row[0]) + '\t\t' + row[1] + '\t\t' + unix_to_readable(row[2]) + '\t' + unix_to_readable(row[3]) + '\t' + row[4])

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
		print(str(row[0]) + '\t\t' + row[1] + '\t\t' + unix_to_readable(row[2]) + '\t' + unix_to_readable(row[3]) + '\t' + row[4]+'\n')

		user_response = input ("Do you want to edit the event above? Enter 'Y' to edit or any other key to cancel: ").lower()

		# Checks user's response and continue
		if user_response == 'y':
			print ("\nPlease input the new event details below")
			new_name = input ("What is the new name of the event?: ")
			new_start_date = readable_to_unix (input ('What is the new start date? (format DD-MM-YYYY): '))
			new_end_date = readable_to_unix(input ('What is the new end date? (format DD-MM-YYYY): '))
			# Checking dates make sense
			while True:
				if new_end_date > new_start_date:
					break
				else:
					new_end_date = readable_to_unix( input("End date cannot be before start date. Please enter another end date: "))
			new_venue = input ("What is the new venue?: ")

			c.execute ("UPDATE events SET event_name = ?, event_start_date = ?, event_end_date = ?, event_venue = ? WHERE event_ID = ? ", 
				(new_name, new_start_date, new_end_date, new_venue, int(event_ID)) )

			conn.commit()

			print ("\nEdit made successfully")
			c.execute("SELECT * FROM events WHERE event_ID=?", (int(event_ID),))
			print('Event ID\tName\t\tStart Date\tEnd Date\tVenue')
			row = c.fetchone()
			print(str(row[0]) + '\t\t' + row[1] + '\t' + unix_to_readable(row[2]) + '\t' + unix_to_readable(row[3]) + '\t' + row[4])
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
		for item in data:
			print ("Event ID:\t\t" + str(item [0]))
			print ("Event name:\t\t" + item [1])
			print ("Event Start Date:\t" + unix_to_readable(item [2]))
			print ("Event End Date:\t\t" + unix_to_readable(item [3]))
			print ("Event Venue:\t\t" + item [4])

		
		user_response = input("\nDo you want to delete the following event? Enter 'Y' to delete or any other key to cancel this deletion: ").lower()
		
		# Checks users response to confirm deletion
		if user_response == 'y':
			c.execute ("DELETE FROM events WHERE event_ID = ?", (int(event_ID),))
			conn.commit()
			print ("Event successfully deleted")

		else:
			print ("Event not deleted")


