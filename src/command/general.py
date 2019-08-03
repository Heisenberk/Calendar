import sys

from presentation import *
from add import *
from delete import *
from view import *
from help import *
from clean import *
from error import *

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

	# Help
	elif argvTab[1] == "-h":
		printHelp()
	elif argvTab[1] == "--help":
		printHelp()

	# Delete events
	elif argvTab[1] == "-d":
		deleteEvent(argvTab)
	elif argvTab[1] == "--delete":
		deleteEvent(argvTab)

	# Clean old events
	elif argvTab[1] == "-c":
		cleanEvents(argvTab)
	elif argvTab[1] == "--clean":
		cleanEvents(argvTab)

	else:
		error()