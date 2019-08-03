import datetime
import time
import sqlite3

# Function to test the number of arguments
def testArgDelete(argvTab):
	assert (len(argvTab)>=4)

# Function to delete an event
def deleteEvent(argvTab):

	# Test the number of arguments
	try:
		testArgDelete(argvTab)
	except Exception:
		print("Not enough arguments for an deletion of event")
		exit(1)

	# Generate the date for SQL
	try:
		dateTimeObject = datetime.datetime.strptime(argvTab[3], '%Y/%m/%d')
		dateStr = str(dateTimeObject.date().year) + "-" + str(dateTimeObject.date().month) + "-" + str(dateTimeObject.date().day)

	except Exception as e:
		print(argvTab[3])
		print("Invalid format date for this event")
		print(e)
		exit(1)

	# Delete the event
	try:
		conn = sqlite3.connect('data/calendar.db')
		cursor = conn.cursor()
		
		data = {"title" : argvTab[2], "dateEvent" : dateStr}
		sql = "DELETE FROM events WHERE title = '%s' AND dateEvent = '%s'" % (argvTab[2], dateStr)
		cursor.execute(sql)
		conn.commit()
		print("An event has just been deleted")

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

	# If the event already exists, we don't make the transaction
	except sqlite3.IntegrityError as e:
		print("Error : This event can not be deleted")

	finally:
		conn.close()
