import sqlite3, time, datetime
from send_email import send_initial_email

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()


def generate_ticket(event_ID, email_address='NULL'):
	# Checks that event with provided event ID exists on the events table
	c.execute("SELECT * FROM events WHERE event_ID = ?", (event_ID,))
	data = c.fetchall()
	if len(data) == 0:
		print ("No event with such an ID exits in the events table. Exiting... ")
	
	else:

		# Checks if no email has been input and gives user a second chance
		if email_address == 'NULL':
			print ("It has been noted that no email address has been associated with this ticket")
			user_response = input ("To add an email address, type 'Y'. Else type any other key").lower()
			if user_response == 'y':
				email_address = input ('Please input email address: ')
			else:
				print ("No email address has been added to this ticket")


		# Adding the data to DB
		c.execute ("INSERT INTO tickets (event_ID, email_address, ticket_status, ticket_time_stamp) VALUES (?, ?, ?, ?)", 
			(event_ID, email_address, 1, round(time.time())))
		conn.commit()
		print ("Ticket has been created successfully")

		# Printing out data that was added
		c.execute ("SELECT * FROM tickets WHERE ticket_ID = (SELECT MAX(ticket_ID) FROM tickets)")
		ticket_data = c.fetchone()
		ticket_ID = ticket_data[0]
		print ("Ticket ID:\t\t" + str(ticket_data [0]))
		print ("Event ID:\t\t" + str(ticket_data [1]))
		print ("Email Address:\t" + ticket_data [2])
		if ticket_data [3] == 1:
			print ("Ticket Status:\t\tValid")
		elif ticket_data [3] == 0:
			print ("Ticket Status:\t\tInvalid")
		else:
			print ("Ticket Status:\t\t" + ticket_data [3])
		print ("Time of creation: " + datetime.datetime.fromtimestamp(ticket_data [4]).strftime('%d-%m-%Y %H:%M'))

		# Add email code 
		if email_address != 'NULL':
			print("Sending email...")
			send_initial_email(email_address, ticket_ID)
			print ("Email sent to " + email_address + " from simpleticketservice@gmail.com")



def view_tickets_for_event(event_ID):
	c.execute("SELECT * FROM tickets WHERE event_ID = ?", (event_ID,))
	data = c.fetchall()
	
	for row in data:
		print ("Ticket ID:\t\t" + str(row [0]))
		print ("Event ID:\t\t" + str(row [1]))
		print ("Email Address:\t\t" + row [2])
		if row [3] == 1:
			print ("Ticket Status:\t\tValid")
		elif row [3] == 0:
			print ("Ticket Status:\t\tInvalid")
		else:
			print ("Ticket Status:\t\t" + row [3])
		print ("Time of creation:\t" + datetime.datetime.fromtimestamp(int(row [4])).strftime('%d-%m-%Y %H:%M'))
		print(50*'*')



def invalidate_ticket(ticket_ID):
	c.execute("SELECT * FROM tickets WHERE ticket_ID = ?", (int(ticket_ID),))
	data = c.fetchall()
	status = True

	# Checks if the chosen ID returns anything from the database
	if data == None:
		print("There is no ticket with that ticket ID found in the database.")

	else:
		# Prints out current ticket status for ID chosen
		for row in data:
			print ("Ticket ID:\t\t" + str(row [0]))
			print ("Event ID:\t\t" + str(row [1]))
			print ("Email Address:\t\t" + row [2])
			if row [3] == 1:
				print ("Ticket Status:\t\tValid")
			elif row [3] == 0:
				print ("Ticket Status:\t\tInvalid")
			else:
				print ("Ticket Status:\t\t" + row [3])
			print ("Time of creation:\t" + datetime.datetime.fromtimestamp(int(row [4])).strftime('%d-%m-%Y %H:%M'))
			print(50*'*')
			if row[3] == 0:
				status = False

		# Checks that the ticket status is not Invalid
		if status == True:
			user_response = input("Would you like to invalidate this ticket? Enter 'Y' to confirm or any other key to cancel: ").lower()
			if user_response == 'y':
				c.execute ("UPDATE ticket SET ticket_status = 0 WHERE ticket_ID = ?", (ticket_ID,))
				print ("Ticket ID no.%d is now invalid" (ticket_ID))

			else:
				print ("No changes have been to the ticket.")
		else:
			print ("The ticket with that ticket ID is already invalid")



