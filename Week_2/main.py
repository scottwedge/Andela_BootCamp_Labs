from event_functions import create_event, view_all_events, edit_event, delete_event
import sqlite3

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()


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
