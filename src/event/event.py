from event.event import *

class Event:
	'Common base class for all events'

	# Constructor of Event
	def __init__(title, content, date):
		self.title = title
		self.content = content
		self.date = date

	# Print Event
	def displayEvent(self):
		print("Title : " + self.title + ", Content : " + self.content + ", Date : " + self.date)