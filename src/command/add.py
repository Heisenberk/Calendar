import datetime
import time
import sqlite3

# Function to test the number of arguments
def testArgAdd(argvTab):
	assert (len(argvTab)>=5)

# Function to add a new event
def addEvent(argvTab):

	# Test the number of arguments
	try:
		testArgAdd(argvTab)
	except Exception:
		print("Not enough arguments for an addition of event")
		exit(1)

	# Generate the date for SQL
	try:
		dateTimeObject = datetime.datetime.strptime(argvTab[4], '%Y/%m/%d')
		dateStr = str(dateTimeObject.date().year) + "-" + str(dateTimeObject.date().month) + "-" + str(dateTimeObject.date().day)

	except Exception as e:
		print("Invalid format date for this event")
		exit(1)

	# Test the date
	dateToday = datetime.date.today()
	diffToday = (dateToday - datetime.date(1970, 1, 1)).total_seconds()
	dateEvent = datetime.date(dateTimeObject.date().year, dateTimeObject.date().month, dateTimeObject.date().day)
	diffEvent = (dateEvent - datetime.date(1970, 1, 1)).total_seconds()
	if(diffEvent <= 0):
		print("Invalid date for this event")
		exit(1)

	if(diffEvent < diffToday):
		print("Invalid date for this event")
		exit(1)


	# Insert the event
	try:
		conn = sqlite3.connect('data/calendar.db')
		cursor = conn.cursor()
		
		data = {"title" : argvTab[2], "content" : argvTab[3], "dateEvent" : dateStr}
		cursor.execute("""INSERT INTO events(title, content, dateEvent) VALUES(:title, :content, :dateEvent)""", data)
		conn.commit()
		print("An event has just been created")
		print(argvTab[2] +" ("+dateStr+"): "+argvTab[3])

	# If the table events doesn't exist, we create it
	except sqlite3.OperationalError :

		cursor.execute("""
			CREATE TABLE events (
    			title VARCHAR(100), 
    			content VARCHAR(300) NOT NULL, 
    			dateEvent DATE NOT NULL, 
    			CONSTRAINT PK_events PRIMARY KEY(title, dateEvent));
			""")
		conn.commit()

		cursor.execute("""INSERT INTO events(title, content, dateEvent) VALUES('%s', '%s', '%s')""" % (argvTab[2], argvTab[3], dateStr))
		conn.commit()
		print("An event has just been created")
		print(argvTab[2] +" ("+dateStr+"): "+argvTab[3])
		

	# If the event already exists, we don't make the transaction
	except sqlite3.IntegrityError as e:
		print("Error : This event already exists")

	finally:
		conn.close()

	

	