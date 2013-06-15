#For room stuff
import random
class Room:
	
	def __init__(self,x,y,roomTypeList):
		
		self.roomName = "Room"
		self.roomCoords = {'x':x, 'y':y}
		self.discovered = False
		self.roomImage = 'X'
		random.seed()
		self.roomTypeList = read(roomTypeList)
		self.roomValue = random.randint(0,100)
		self.generateRoomType(self.roomValue)
	def printRoomCoords(self):
		print (self.roomName, end=" "),
		print ("X:",self.roomCoords['x'], end = " ")
		print ("Y:", self.roomCoords['y'],end=" ")
	def printRoom(self):
			print(self.roomImage,end = "")
		
	def generateRoomType(self, roomValue):
		if roomValue <
	def enterRoom(self):
		self.discovered = True
		self.roomImage = 'O'