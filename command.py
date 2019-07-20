import sys

# Function of general display
def printPresentation():
	print("\033[1m\033[34m                            ____        _                   _ ")
	print("                          / ___| __ _ | |  ___  _ __    __| |  __ _  _ __ ")
	print("                         | |    / _` || | / _ \| '_ \  / _` | / _` || '__|")
	print("                         | |___| (_| || ||  __/| | | || (_| || (_| || |   ")
	print("                          \____|\__,_||_| \___||_| |_| \__,_| \__,_||_|  ")
	print("\033[39m              ____         \033[31m  _   _        _                    _                  _    ")
	print("\033[39m             | __ )  _   _ \033[31m | | | |  ___ (_) ___   ___  _ __  | |__    ___  _ __ | | __")
	print("\033[39m             |  _ \ | | | |\033[31m | |_| | / _ \| |/ __| / _ \| '_ \ | '_ \  / _ \| '__|| |/ /")
	print("\033[39m             | |_) || |_| |\033[31m |  _  ||  __/| |\__ \|  __/| | | || |_) ||  __/| |   |   < ")
	print("\033[39m             |____/  \__, |\033[31m |_| |_| \___||_||___/ \___||_| |_||_.__/  \___||_|   |_|\_\\")
	print("\033[39m                     |___/  \033[0m\033[39m")
	print("")
	print("\033[1m\033[32mcalendar -h/--help \033[0m\033[39mto see commands")

# Function to add a new event
def addEvent(argvTab):
	print("add")

# Function to see events
def viewEvents(argvTab):
	print("view")

# Function to delete an event 
def deleteEvent(argvTab):
	print("delete")

# Function to detect the command chosen by the user
def detectCommand(argvTab):

	# General display
	if len(argvTab) == 1:
		printPresentation()

	# Add a new event
	elif argvTab[1] == "-a":
		addEvent(argvTab)
	elif argvTab[1] == "--add":
		addEvent(argvTab)

	# View events
	elif argvTab[1] == "-v":
		viewEvents(argvTab)
	elif argvTab[1] == "--view":
		viewEvents(argvTab)

	# Delete events
	elif argvTab[1] == "-d":
		deleteEvent(argvTab)
	elif argvTab[1] == "--delete":
		deleteEvent(argvTab)


def main():
	detectCommand(sys.argv)

	return 0

main()



