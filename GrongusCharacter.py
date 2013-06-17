#character

class Character:
	
	def __init__(self,health,icon):
		self.health = health
		self.icon = icon

		
class Player(Character):
	def __init__(self,xcoord,ycoord):
		"""initializing player stats.  I intend to 
			expand the input by a /bunch/.  Energy, etc 
			will not be so static.  I will
			try to write in such a manner that it will be
			expandable
		"""
		Character.health = 100
		Character.icon = "T"
		self.energy = 100
		self.coords = {'x':xcoord, 'y':ycoord}
		
	#for updating the current player coordinates
	def movePlayer(self,newX,newY):
		self.coords['x'] = newX
		self.coords['y'] = newY
		
	def printPlayer(self):
		print("Health: ", self.health)
		print("Energy: ",self.energy)
		print("Icon: ", self.icon)
		print(self.coords)
		
class Grongus(Character):
		def __init__(self, xcoord,ycoord):
			Character.health = 1
			Character.icon = "B"
			self.energy = 0
			self.coords = {'x':xcoord,'y':ycoord}
			
			
		

		
		
	
		