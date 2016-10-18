from event_functions import create_event, view_all_events, edit_event, delete_event
from instructions import print_instructions
from ticket_functions import generate_ticket, view_tickets_for_event, invalidate_ticket
from ascii_pics import intro_pic, outro_pic
import sqlite3

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

print("Welcome to the Ticket Booking System")
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
			start_date = input ('Start Date(format DD-MM-YYYY): ')
			end_date = input ('End Date(format DD-MM-YYYY): ')
			venue = input ('Venue: ')
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
		pass

	elif 'ticket invalidate' in user_input:
		instr_list = user_input.split(' ')
		if len(instr_list)>=3:
			ticket_ID = instr_list[2]
			try:
				invalidate_ticket(int(ticket_ID))
			except ValueError:
				print ("Sorry. Value provided after 'ticket invalidate' not a valid ticket ID")
		else:
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
		print ("Sorry. That instruction could not be understood")

conn.close()
c.close()
print("Exiting. Thank you for using the ticketing app")
#outro_pic()

