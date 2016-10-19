import sqlite3, time, datetime

conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()

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
			Start Date: 	%s
			End Date: 		%s
			Venue: 			%s''' %(name, start_date, end_date, venue))
		return True
