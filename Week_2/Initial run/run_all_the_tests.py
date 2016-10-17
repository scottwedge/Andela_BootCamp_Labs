from create_event import create_event
import sqlite3

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

name = input ('Event name: ')
start_date = input ('Start Date: ')
end_date = input ('End Date: ')
venue = input ('Venue: ')

create_event(name, start_date, end_date, venue)
#create_event('Some Festival', '12-2-2010', '14-2-2010', 'Mombasa')