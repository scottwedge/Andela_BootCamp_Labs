
import email, smtplib, sqlite3, time, datetime
from unix_time_conversions import unix_to_readable, readable_to_unix
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Connecting to the SQLite DB
conn = sqlite3.connect('dummy_data.db')
c = conn.cursor()
 
 
def send_initial_email(email_address, ticket_ID):
	ticket_ID = int(ticket_ID)
	#Getting data from the database
	# Ticket Table
	c.execute ("SELECT * FROM tickets WHERE ticket_ID = ?", (ticket_ID,))
	ticket_data = c.fetchone()
	event_ID = ticket_data [1]
	ticket_status = None
	if ticket_data[3] == 1:
		ticket_status = 'Valid'
	elif ticket_data[3] == 0:
		ticket_status = 'Invalid'
	ticket_time_stamp = datetime.datetime.fromtimestamp(int(ticket_data [4])).strftime('%d-%m-%Y %H:%M')


	# Events Table
	c.execute ("SELECT * FROM events WHERE event_ID = ?", (event_ID,))
	event_data = c.fetchone()
	event_name = event_data[1]
	event_start_date = event_data[2]
	event_end_date = event_data[3]
	event_venue = event_data[4]


	# Checking if ticket is valid
	if ticket_status == 'Invalid':
		print ("The ticket with this ticket ID is invalid. Email not sent")
		return False

	else:
		
		fromaddr = "simpleticketservice@gmail.com"
		toaddr = email_address
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Ticket generated for " + str(event_name).upper()
		 
		body = '''
Hi there,

Just wanted to confirm that your ticket has been successfully created. Here are the event details:
Event Name:		%s
Start Date:		%s
End Date:		%s
Event Venue:	%s

Your ticket ID is %d and was created on %s

Regards,
Ticket Service Team

        ''' %(event_name, unix_to_readable(event_start_date), unix_to_readable(event_end_date), event_venue, ticket_ID, ticket_time_stamp)

		msg.attach(MIMEText(body, 'plain'))
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "simpleticketservicepassword")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		return True
