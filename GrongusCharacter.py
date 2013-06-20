#character

class Character:
	
	def __init__(self,health,icon):
		self.health = health
		self.icon = icon

class Spear(Character):
		def __init__(self):
			self.name = "spear"
			self.weaponRange = 1
			self.energyCost = -1
			self.damage = 1
			
		def isValidRange(self,range):
			if range <= self.weaponRange:
				return True
			return False
			
class Player(Character):
	def __init__(self,xcoord,ycoord):
		"""initializing player stats.  I intend to 
			expand the input by a /bunch/.  Energy, etc 
			will not be so static.  I will
			try to write in such a manner that it will be
			expandable
		"""
		self.name = "Tom"
		self.maxHealth = 100
		self.curHealth = self.maxHealth
		
		self.icon = "T"
		self.items =  {}
		self.maxEnergy = 100
		self.curEnergy = self.maxEnergy
		self.coords = {'x':xcoord, 'y':ycoord}
		self.items = {}
	#for updating the current player coordinates
	def addItems(self,name,item):
		self.items[name] = item
	def updatePlayerPosition(self,newX,newY):
		self.coords['x'] = newX
		self.coords['y'] = newY
		
	def printPlayer(self):
		print("Health: ", self.curHealth)
		print("Energy: ",self.curEnergy)
		print("Icon: ", self.icon)
		print("Current Location: ", self.coords)
	
	def hasEnergy(self,weapon):
		if self.curEnergy >= weapon.energyCost:
			return True
		return False
		
	def attack(self,weapon,direction,range):
		#need to add enemy check
		
			if weapon.isValidRange(range):
				if self.hasEnergy(weapon):
					return weapon.damage
				else:
					print("Not enough energy!")
			else:
				print("Not within range!")
		
class Grongus(Character):
		def __init__(self):
			self.name = "Grongus"
			self.maxHealth= 1
			self.curHealth = self.maxHealth
			
			self.icon = "G"
			self.energy = 0
			self.coords = {}
		
		def takeDamage(self,damage):
			self.curHealth -= damage
			
		def updatePosition(self, x ,y):
			self.coords = {'x':x,'y':y}
		

		
		
	
		