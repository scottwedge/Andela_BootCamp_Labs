from instructions import print_instructions
from event_functions import create_event, view_all_events, edit_event, delete_event
from ticket_functions import generate_ticket, view_tickets_for_event, invalidate_ticket
from ascii_pics import intro_pic, outro_pic
from unix_time_conversions import unix_to_readable, readable_to_unix
from send_email import send_initial_email
import sqlite3


conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

print("\t\t\t\t\t\tWelcome to the Ticket Booking Service\t\t\t\t\t")
intro_pic()


while True:

	user_input = input ("\nWhat would you like to do? For a list of available instructions, type 'instr': ").lower()

	if user_input == 'cancel':
		break

	elif user_input == 'instr':
		print_instructions()

	elif 'event create' in user_input:
		response =  input("Creating new event. Type 'X' to cancel, otherwise press enter to continue: ").lower()
		if response == 'x':
			print ('Event creation cancelled successfully')
		else:
			name = input ('Event name: ')
			venue = input ('Venue: ')
			start_date = readable_to_unix (input ('Start Date(format DD-MM-YYYY): '))
			end_date = readable_to_unix(input ('End Date(format DD-MM-YYYY): '))
			# Checking dates make sense
			while True:
				if end_date > start_date:
					break
				else:
					end_date = readable_to_unix( input("End date cannot be before start date. Please enter another end date: "))
			
			# Going to create function to create data using user data			
			create_event(name, start_date, end_date, venue)
				

	elif 'event edit' in user_input:
		instr_list = user_input.split(' ')
		if len(instr_list)>=3:
			event_ID = instr_list[2]
			try:
				edit_event(int(event_ID))
			except ValueError:
				print ("Value provided after 'event edit' not a valid event ID")
		else:
			print ('Could not find event ID instruction to edit')
			response = input ("Please enter event ID. Or type 'X' to cancel: ").lower()
			if response == 'x':
				print ("Event edit successfully cancelled")
			else:
				try:
					edit_event(int(response))
				except ValueError:
					print ("Sorry. That can not be used as an event ID")



	elif 'event delete' in user_input:
		instr_list = user_input.split(' ')
		if len(instr_list)>=3:
			event_ID = instr_list[2]
			try:
				delete_event(int(event_ID))
			except ValueError:
				print ("Sorry. Value provided after 'event delete' not a valid event ID")
		else:
			print ('Could not find event ID instruction to delete')
			response = input ("Please enter event ID. Or type 'X' to cancel: ").lower()
			if response == 'x':
				print ("Event deletion successfully cancelled")
			else:
				try:
					delete_event(int(response))
				except ValueError:
					print ("Sorry. That value can not be used as an event ID")


	elif 'event list' in user_input:
		view_all_events()

	elif 'event view' in user_input:
		instr_list = user_input.split(' ')
		if len(instr_list)>=3:
			event_ID = instr_list[2]
			try:
				view_tickets_for_event(int(event_ID))
			except ValueError:
				print ("Sorry. Value provided after 'event view' not a valid event ID")
		else:
			print ('Could not find event ID instruction to list all tickets')
			response = input ("Please enter event ID. Or type 'X' to cancel: ").lower()
			if response == 'x':
				print ("Viewing all tickets for a particular ID successfully cancelled")
			else:
				try:
					view_tickets_for_event(int(response))
				except ValueError:
					print ("Sorry. That value can not be used as an event ID")



	elif 'ticket generate' in user_input:
		instr_list = user_input.split(' ')

		response = input ("Please enter the event ID for which the ticket is to be generated. (Enter 'X' to cancel): ").lower()

		if response == 'X':
			print ("Cancelled successfully. No ticket has been generated or enail sent")
		else:
			try:
				event_ID = int (response)
				if len(instr_list)>=3:
					email = instr_list[2]
					generate_ticket(event_ID, email)
				else:
					generate_ticket(event_ID)
			except ValueError:
				print ("Value provided cannot be a valid event ID")
			

	elif 'ticket send' in user_input:
		instr_list = user_input.split(' ')
		# Checks if all the arguments were input
		if len (instr_list) >= 4:
			ticket_ID = instr_list[2]
			email_address = instr_list[3]
		else:
			print ("You have not input the required number of fields for this command")
			# Checks that the ticket ID is a number
			while True:
				try:
					ticket_ID = int(input ("Please input a ticket ID: "))
					break
				except ValueError:
					print ("The ticket ID must be a number.")
			email_address = input ("Please input email address: ")

		print ("Trying to send email...")
		email_sent = send_initial_email(email_address, ticket_ID)

		if email_sent == True:
			# Checks if user wants to update ticket with new email address if email is sent successfully
			response = input ("Do you want to update this ticket ID " + ticket_ID + " with this new email(" + email_address+ ")?\n\
				Type 'Y' if you want to update or any other key to cancel: ").lower()
			if response == 'y':
				c.execute("UPDATE events SET email_address = ? WHERE ticket_ID = ?", (email_address, ticket_ID))
				conn.commit()
				print ("Ticket updated")


	elif 'ticket invalidate' in user_input:
		# Splits up users input
		instr_list = user_input.split(' ')
		# Checks to see that user provided ticket ID
		if len(instr_list)>=3:
			ticket_ID = instr_list[2]
			try:
				invalidate_ticket(int(ticket_ID))
			except ValueError:
				print ("Sorry. Value provided after 'ticket invalidate' not a valid ticket ID")
		else:
			# Asks for ticket ID if not found in instruction
			print ('Could not find ticket ID instruction to list all tickets')
			response = input ("Please enter ticket ID. Or type 'X' to cancel: ").lower()
			if response == 'x':
				print ("Invalidating ticket successfully cancelled")
			else:
				try:
					invalidate_ticket(int(response))
				except ValueError:
					print ("Sorry. That value can not be used as an ticket ID")

	else:
		print("Sorry, that instruction could not be understood. Please try again")
		

conn.close()
print("Exiting. Thank you for using the ticketing app")
outro_pic()

