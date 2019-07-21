import datetime
import sqlite3

# Function to test the number of arguments
def testArgAdd(argvTab):
	assert (len(argvTab)>=5)

# Function to add a new event
def addEvent(argvTab):
	try:
		testArgAdd(argvTab)
	except Exception:
		print("Not enough arguments for an addition of event")

	try:
		dateTimeObject = datetime.datetime.strptime(argvTab[4], '%Y/%m/%d')
		print(dateTimeObject.date().year)
		print(dateTimeObject.date().month)
		print(dateTimeObject.date().day)
	except Exception:
		print("Invalid date for this event")

	try:
		conn = sqlite3.connect('data/calendar.db')
		cursor = conn.cursor()
		
		data = {"title" : "titre", "content" : "le contenu", "dateEvent" : '2015-02-04'}
		cursor.execute("""INSERT INTO events(title, content, dateEvent) VALUES(:title, :content, :dateEvent)""", data)
		conn.commit()
	# If the table events doesn't exist, we create it
	except sqlite3.OperationalError :
		cursor.execute("""
			CREATE TABLE events (
    			title VARCHAR(100), 
    			content VARCHAR(300) NOT NULL, 
    			dateEvent DATE NOT NULL, 
    			CONSTRAINT PK_events PRIMARY KEY(title, dateEvent));
			""")
		data2 = {"title" : "titre", "content" : "le contenu", "dateEvent" : '2015-02-04'}
		cursor.execute("""INSERT INTO events(title, content, dateEvent) VALUES(?, ?, ?)""", data2)
		conn.commit()

	# If the event already exists, we don't make the transaction
	except sqlite3.IntegrityError as e:
		print("Error : This event already exists")
		print(e)

	finally:
		conn.close()

	

	