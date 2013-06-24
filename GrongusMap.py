#GrongusMap
import GrongusRoom
import GrongusExceptions
import GrongusCharacter

import random
class GrongusMap:
	"""initialize the map, that is set the maximum boundaries for the height and width
"""
	def __init__(self,x,y,player,grongus,randCoords):
		self.x = x
		self.y = y
		
		self.gameMap = {}
		self.generateGameMap(randCoords,grongus)
		
		self.gameMap[0][y-1].updateRoom(player.icon,True)
		self.printMap()
	def roomSounds(self,player):
	
		for x,y in self.gameMap:
			self.gameMap[x][y].roomSounds(player)
			
	def roomOpen(self):
		#f = open('roomlist.txt','r')
		#rooms = {}
		#for line in f:
		#	k,v, = line.strip().split(' ')
		#	rooms[k.strip()] = float(v.strip())
		#f.close()
		#print (rooms)
		rooms = {GrongusRoom.SandRoom:90,GrongusRoom.RestPool:10}
		return rooms
		
	def generateRoom(self,i,j):
		total = 0
		winner = 0
		rooms = self.roomOpen()
		for key, value in rooms.items():
			total+= value
			if random.random() * total < value:
				winner = key
		return winner(i,j)
				
		
		
	def generateGameMap(self,randCoords,grongus):
		#rooms = self.roomOpen()
		
		self.gameMap = [[self.generateRoom(i,j) for i in range(self.x)] for j in
		range(self.y)]
		x = randCoords['x']
		y = randCoords['y']
		self.gameMap[x][y].addToContents("grongus",grongus)
		grongus.updatePosition(randCoords['x'],randCoords['y'])
				
		print("Grongus Located at: ",x,",",y)
	
					
					
		#reason I didn't use a dictionary.  I need it sorted for x,y coordinates?
		#I'm not sure if dictionaries can be used like a map.
		#gameMap = {(x,y):"room" for x in range(self.x) for y in range(self.y)}	
		
		"""printMap:  prints a room map, base on room discovery.
		"""
	def printMap(self):
		for i in range(self.y):
			for j in range(self.x):	
				self.gameMap[j][i].printRoom()
				
			print("")		
		
	def playerMoved(self, x,y,player,grongus):
		roomDiscovered = True
		
		if self.gameMap[x][y].containsObject("grongus") :
			self.gameMap[x][y].updateRoom(grongus.icon, roomDiscovered)
			print("Found the Grongus!")
			
			return
		print("Not found the grongus")
		self.gameMap[x][y].applyRoomEffects(player)
		self.roomSounds()
		self.gameMap[player.coords['x']][player.coords['y']].roomExited()
		self.gameMap[x][y].roomEntered(player.icon)
		player.updatePosition(x,y)
		
	
		