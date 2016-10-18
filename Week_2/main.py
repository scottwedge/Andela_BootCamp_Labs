from event_functions import create_event, view_all_events, edit_event, delete_event
from instructions import print_instructions
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
		pass


	elif 'event list' in user_input:
		pass

	elif 'event view' in user_input:
		pass


	elif 'ticket generate' in user_input:
		pass

	elif 'ticket invalidate' in user_input:
		pass

	else:
		print ("Sorry. That instruction could not be understood")

conn.close()
c.close()
print("Exiting. Thank you for using the ticketing app")
outro_pic()




#delete_event(int(input('Delete event ID:')))

#view_all_events()

#edit_event(int(input('Event ID for edit: ')))

# Create Event Tests
'''
name = input ('Event name: ')
start_date = input ('Start Date(format DD-MM-YYYY): ')
end_date = input ('End Date(format DD-MM-YYYY): ')
venue = input ('Venue: ')

create_event(name, start_date, end_date, venue)

'''
