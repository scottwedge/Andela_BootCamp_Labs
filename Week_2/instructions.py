def print_instructions():
	print(''' 

As a user, you can type in the following:
-	cancel - exits out of the application
-	instr - prints out a list of instructions
-	event create - Creates a new event in the database table.
	The following fields will have to be submitted:
	-	Event name
	-	Event start date
	-	Event end date
	-	Event venue

-	event delete <event_id> - Deletes an existing event from the database table.

-	event edit <event_id> - Edit an already existing event from the database.
	The following fields will have to be submitted:
	-	Event name
	-	Event start date
	-	Event end date
	-	Event venue

-	event list - Lists all the events in the database

-	event view <event_id> - View all the tickets that have been generated for that event.

-	ticket generate <e_mail> - Generates a new ticket and send it to the supplied e-mail address (if supplied. If not run ticket send <ticket_id> <e_mail> to send the ticket).
-	Once a ticket has been generated, send reminders at weekly intervals to remind the user about the event. (Extra Credit)
-	ticket invalidate <ticket_id> - Invalidates a ticket.


		''')