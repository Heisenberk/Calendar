import datetime

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

	

	