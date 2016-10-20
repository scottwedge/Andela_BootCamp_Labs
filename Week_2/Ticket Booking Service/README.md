# Andela BootCamp Labs
## Ticket Booking Service Project


### Introduction

This is a repository containing all the files needed for Ticket Booking Service Project done for the Andela Cohort X BootCamp Week 2. 

### Objectives
For this project, the objective is to creating a service for use at service stations where ticket bookings can be made. We should be able to create events, delete events, edit event and generate tickets (of various types).

As a user, you should be able to perform the following operations:
* `event create <event_details>` - Creates a new event in the database table. Event details should contain the following fields
  * Event name
  * Event start date
  * Event end date
  * Event venue
* `event delete <event_id>` - Deletes an existing event from the database table.
* `event edit <event_id> <new_event_details>` - Edit an already existing event from the database.
* `event list` - Lists all the events in the database
* `event view <event_id> `- View all the tickets that have been generated for that event.
* `ticket generate <e_mail>` - Generates a new ticket and send it to the supplied e-mail address (if supplied. If not run `ticket send <ticket_id> <e_mail>` to send the ticket).
  * Once a ticket has been generated, send reminders at weekly intervals to remind the user about the event. (Extra Credit)
* `ticket invalidate <ticket_id>` - Invalidates a ticket.



### Installation

The scripts were written for Windows and may not work correctly with other systems. 
You can run the python files using idle or directly from cmd. 

To install, clone the directory using the `git clone` command: 
- `git clone https://github.com/bobmwaniki/Andela_BootCamp_Labs/tree/master/Week_2`

Then run `main.py`: `py main.py`

**Note:** All the files are written for Python 3.x and above and will not work properly on earlier versions

### Description
##### Main function
The ticket service is to be run from `main.py`. Once run the function listens for certain key words to create, edit, list or edit events or tickets. This then calls on the other functions in the directoty to pull/push data to the database.

##### Event_Functions
Contains all the functions necessary to carry out the event commands i.e. `event create <event_details>`,  `event delete <event_id>`, `event edit <event_id> <new_event_details>` and `event list` 

##### Ticket_Functions
Contains all the functions necessary to carry out the ticket commands i.e. `event view <event_id>`, `ticket generate <e_mail>`, `ticket send <ticket_id> <e_mail>` and `ticket invalidate <ticket_id>`.

##### Dummy_Data
`dummy_data.db` is the SQLite database that contains all the data for the service. It has 2 tables: `events` and `tickets`. 

`events` table contains all the event data with the following columns `event_ID`, `event_name`, `event_start_date`, `event_end_date`, and `event_venue`.

`tickets` table contains ticket data under the following headings `ticket_ID`, `event_ID`, `email_address`, `ticket_status` and `ticket_time_stamp`.

##### Ascii_Pics
Contains the ASCII pictures that appear as the Welcome and Outro text.

##### Instructions.py
Function that can be called to list all the valid commands

##### Send_email
Function used to generate emails to specified senders when the commands  `ticket generate <e_mail>` or `ticket send <ticket_id> <e_mail>` are run. Emails are sent from `simpleticketservice@gmail.com`.

##### Unix_time_Conversion
Functions to convert dates entered to and from UNIX time. This is because the dates are stored in `dummy_data.db` in UNIX time but is displayed to and entered by the user in the format DD-MM-YYYY.





### Tests 






