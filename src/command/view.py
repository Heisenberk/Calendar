import sqlite3
import datetime
import time

# Function to test the number of arguments
def testArgView(argvTab):
	return len(argvTab)

def getDayWeekStr(dayWeek):
	if dayWeek == 0:
		return "Monday"
	elif dayWeek == 1:
		return "Tuesday"
	elif dayWeek == 2:
		return "Wednesday"
	elif dayWeek == 3:
		return "Thursday"
	elif dayWeek == 4:
		return "Friday"
	elif dayWeek == 5:
		return "Saturday"
	else:
		return "Sunday"

def getMonthStr(month):
	if month == 1:
		return "January"
	elif month == 2:
		return "February"
	elif month == 3:
		return "March"
	elif month == 4:
		return "April"
	elif month == 5:
		return "May"
	elif month == 6:
		return "June"
	elif month == 7:
		return "July"
	elif month == 8:
		return "August"
	elif month == 9:
		return "September"
	elif month == 10:
		return "October"
	elif month == 11:
		return "November"
	else:
		return "December"



# Function to view all events in the calendar
def viewAllEvents():
	conn = sqlite3.connect('data/calendar.db')
	cursor = conn.cursor()
	sql = "SELECT * FROM events ORDER BY events.dateEvent"

	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		newDay = 1
		test = 0
		tempDay = None
		for row in result:
			title = row[0]
			content = row[1]
			dateEvent = row[2]
			test = 1

			if(newDay == 1):
				dateTimeObject = datetime.datetime.strptime(dateEvent, '%Y-%m-%d')
				dayWeek = dateTimeObject.weekday()
				month = dateTimeObject.month
				day = dateTimeObject.day
				year = dateTimeObject.year
				
				if((tempDay == None) or (tempDay != dateTimeObject)):
					print("\033[1m\033[91m" + getDayWeekStr(dayWeek) + ", " + getMonthStr(month) + " " + str(day) + ", " + str(year) + "\033[0m\033[39m") 

				tempDay = dateTimeObject


			print(" \033[1m\033[93m%s:\033[0m\033[39m %s" % (title, content))

		if (test == 0):
			print("No event in the calendar")

	except sqlite3.OperationalError as e:
		cursor.execute("""
			CREATE TABLE events (
    			title VARCHAR(100), 
    			content VARCHAR(300) NOT NULL, 
    			dateEvent DATE NOT NULL, 
    			CONSTRAINT PK_events PRIMARY KEY(title, dateEvent));
			""")
		conn.commit()
		print("No event in the calendar")

	conn.close()


# Function to see events
def viewEvents(argvTab):
	viewAllEvents()