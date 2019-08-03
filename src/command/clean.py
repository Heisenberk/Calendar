import datetime
import time
import sqlite3

# Function to delete an event
def cleanEvents(argvTab):

	# Generate the date for SQL
	dateTimeObject = datetime.datetime.today()
	dateStr = str(dateTimeObject.date().year) + "-" + str(dateTimeObject.date().month) + "-" + str(dateTimeObject.date().day)
	print(dateStr)

	# Clean old events
	try:
		conn = sqlite3.connect('data/calendar.db')
		cursor = conn.cursor()
		
		data = {"dateEvent" : dateStr}
		sql = "DELETE FROM events WHERE dateEvent < '%s'" % (dateStr)
		cursor.execute(sql)
		conn.commit()
		print("Clean Done")

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
		print("Error : Impossible to clean")

	finally:
		conn.close()
