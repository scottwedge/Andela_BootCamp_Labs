import sqlite3

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

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
			print ("Event successfully deleted")

		else:
			print ("Event not deleted")
