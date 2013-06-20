#GrongusMap
import GrongusRoom
import GrongusExceptions
import GrongusCharacter
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
		
		
	#	map generation.  Early on, it will only create a blank set of rooms
	#	using python dictionaries.  Will call helper functions to generate#
	#actual contents later.  
	#invariants:x and y of map
	
	def generateGameMap(self,randCoords,grongus):
		self.gameMap = [[GrongusRoom.Room(i,j) for i in range(self.x)] for j in
		range(self.y)]
		x = randCoords['x']
		y = randCoords['y']
		self.gameMap[x][y].addToRoom("grongus",grongus)
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
		if self.gameMap[x][y].containsThing("grongus") :
			self.gameMap[x][y].updateRoom(grongus.icon, roomDiscovered)
			print("Found the Grongus!")
			return
		
		self.gameMap[x][y].applyRoomEffects(player)
		self.gameMap[player.coords['x']][player.coords['y']].updateRoom("O",roomDiscovered)
		self.gameMap[x][y].updateRoom(player.icon, roomDiscovered)
		player.updatePlayerPosition(x,y)
		
		
		#"""
	#		if self.gameMap[player.coords['x']][player.coords['y']].discovered == True:
#			self.gameMap[x][y].updateIcon(player.icon)
	#		self.gameMap[player.coords['x']][player.coords['y']].roomLeft()
	#		player.updatePlayerPosition(x,y)
			
	#		elif "grongus" in self.gameMap[x][y].thingsInRoom :
	#		print ("You see the awful Grongus",self.gameMap[x][y].thingsInRoom["grongus"].icon)
	#		self.gameMap[x][y].updateIcon(self.gameMap[x][y].thingsInRoom["grongus"].icon)
	#		else:
	#		self.gameMap[x][y].discoverRoom(player.icon)
	#		self.gameMap[player.coords['x']][player.coords['y']].roomLeft()
	#		player.updatePlayerPosition(x,y)
	#	"""
	
		