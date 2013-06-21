#GrongusRoom2

#For room stuff
import GrongusCharacter

class Room:
	#name,x coords, y coords, energyCost,discovered,canContainGrongus,icon
	def __init__(self,name,x,y,energyCost,discovered,canContain,icon):
		self.name = name 
		self.roomCoords = {'x':x,'y':y}
		self.energyCost = energyCost
		self.discovered = discovered
		self.canContainGrongus = canContain
		self.HiddenImage = "X"
		self.revealedImage = icon
		self.roomImage = self.HiddenImage
		self.roomContents = {}
	
	
	def roomEntered(self,icon):
		self.roomImage = icon
		self.discovered = True
		
	def roomExited(self):
		self.roomImage = self.revealedImage
		
	def updateRoom(self,icon,status):
		self.roomImage = icon
		self.discovered = status
		
	def printRoomCoords(self):
		print (self.roomName, end = " ")
		print (self.roomCoords)
	
	def printRoom(self):
		print(self.roomImage,end = "")		
	
	def addToContents(self,key,thing):
		self.roomContents[key] = thing
		
		
	"""Note:I recommend overriding this with subclass method, since 
		each room will want to have special effects it does to the player
	"""
	def applyRoomEffects(self,player):
		player.curEnergy -= self.energyCost
		
	def containsObject(self,thing):
		if thing in self.roomContents:
			return True
	
	def attackRoomContents(self,damage):
		for key in self.roomContents:
			object = self.roomContents[key]
			print("Attacking: ",object.name, " for ", damage," damage!")
			object.takeDamage(damage)
			print("It has ",object.curHealth," HP remaining")
			
class SandRoom(Room):
	
	def __init__(self,x,y):
		#name,x coords, y coords, energyCost,discovered,canContainGrongus,icon
		super().__init__("Sand",x,y,1,False,True,"S")
	
		
	
	
		
	

	
	
	
	
	