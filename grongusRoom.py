#For room stuff
import GrongusCharacter
class SandRoom:
	def init(self,x,y):
		self.energyCost = 4
		self.discovered = False
		self.healPlayer = False
		self.canContainGrongus = True
		self.thingsInRoom = {}
		self.roomCoords = {'x':x,'y':y}
		self.roomImage = 'S'
		
class Room:
	"""This is not quite how I want to do rooms.  I think maybe
		I want to create a bunch of subclasses that have an "apply to user function"
		and call that.  Allows for more expandability, I think.  Perhaps, in the longest of runs
		I can use XML or something 
	"""

	
	def __init__(self,x,y):
		self.energyCost = 1
		self.healPlayer = False
		self.canContainGrongus = True
		self.thingsInRoom = {}
		self.roomCoords = {'x':x, 'y':y}
		self.discovered = False
		self.roomImage = 'X'
		#self.roomDiscoveredImage = 'O'
		
	def printRoomCoords(self):
		print (self.roomName, end=" "),
		print ("X:",self.roomCoords['x'], end = " ")
		print ("Y:", self.roomCoords['y'],end=" ")
	
	def printRoom(self):
		print(self.roomImage,end = "")	
		
	def addToRoom(self,key,thing):
		
		self.thingsInRoom[key] = thing
	#I don't like how this works out.  Seems..inefficient. Ponder how 
	#to apply the room effects to the player without having to go /into/
	#the room.
	def applyRoomEffects(self,player):
		#print("Applied Room effects!")
		player.curEnergy -= 1
	def updateRoom(self,icon,status):
		self.roomImage = icon
		self.discovered = status
	def containsThing(self,thing):
		if thing in self.thingsInRoom:
			return True
		return False
	#not needed, leaving in for sanity	
	def roomLeft(self):
		self.roomImage = "O"