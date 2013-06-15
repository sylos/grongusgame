#GrongusMap
import grongusRoom
class GrongusMap:
	"""initialize the map, that is set the maximum boundaries for the height and width
"""
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
		self.gameMap = []
		self.generateGameMap()
		self.printMap()
		roomList = open('roomList,'r')
		
	#	"""map generation.  Early on, it will only create a blank set of rooms
#		using python dictionaries.  Will call helper functions to generate#
		#actual contents later.  
		#invariants:x and y of map
	#"""
	def generateGameMap(self):
		self.gameMap = [[grongusRoom.Room(i,j) for i in range(self.x)] for j in
		range(self.y)]
		
		
		#reason I didn't use a dictionary.  I need it sorted for x,y coordinates?
		#I'm not sure if dictionaries can be used like a map.
		#gameMap = {(x,y):"room" for x in range(self.x) for y in range(self.y)}	
		
		"""printMap:  prints a room map, base on room discovery.
		"""
	def printMap(self):
		for i in range(self.y):
			for j in range(self.x):	
				self.gameMap[i][j].printRoom()
				
			print("")	
		
		
	
		
	
		