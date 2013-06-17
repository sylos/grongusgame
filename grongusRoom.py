#For room stuff
import random
class Room:
	"""This is not quite how I want to do rooms.  I think maybe
		I want to create a bunch of subclasses that have an "apply to user function"
		and call that.  Allows for more expandability, I think.  Perhaps, in the longest of runs
		I can use XML or something 
	"""

	energyCost = 1
	healPlayer = False
	canContainGrongus = True
	thingsInRoom = {}
	def __init__(self,x,y):
		self.roomName = "Room"
		self.roomCoords = {'x':x, 'y':y}
		self.discovered = False
		self.roomImage = 'X'
		random.seed()
		#self.roomTypeList = read(roomTypeList)
		self.roomValue = random.randint(0,100)
		#self.generateRoomType(self.roomValue)
	def printRoomCoords(self):
		print (self.roomName, end=" "),
		print ("X:",self.roomCoords['x'], end = " ")
		print ("Y:", self.roomCoords['y'],end=" ")
	def printRoom(self):
		print(self.roomImage,end = "")
	
		
	#def generateRoom(self):
	def updateIcon(self,icon):
		self.roomImage = icon
		
	def discoverRoom(self,icon):
		self.discovered = True
		self.roomImage = icon
		
	def roomLeft(self):
		self.roomImage = "O"