#character

"""Character Classes(name,health,energy,icon)
	It's important that the subclasses call super.__init__() with those aforementioned
	attributes.  While not /strictly/ necessary, the class already contains methods for
	dealing with those variables.  
	"""
class Character:
	
	def __init__(self,name,health,energy,icon):
		self.name = name
		self.maxHealth = health
		self.curHealth = self.maxHealth
		self.maxEnergy = energy
		self.curEnergy = self.maxEnergy
		self.icon = icon
		self.coords = {}
		self.items = {}
		
	def addItems(self,name,item):
		self.items[name] = item
		
		
	def takeDamage(self,damage):
		self.curHealth -= damage
		
	def updatePosition(self,x,y):
		self.coords = {'x':x,'y':y}
		
	def printRawStats(self):
		print(self.name, end = " ")
		print("Health: ",self.curHealth,"/",self.maxHealth,end = " ")
		print("Energy", self.curEnergy, "/",self.maxEnergy, end = " ")
		print(self.icon,"Location ","x:",self.coords['x']," ","y:",self.coords['y'])
	
	def hasEnergy(self,cost):
		if self.curEnergy >= cost:
			return True
		raise GrongusExceptions.NotEnoughCost()
		
class Player(Character):
	def __init__(self,x,y):
		super().__init__("Hero",100,100,"T")
		self.updatePosition(x,y)
		self.items = {}
	
	
	
	
	"""Attack(self,weapon,range) works like this
		if the weapon attack range is within the range the plaer wishes to attack
		,for instance, if the player is wielding a spear with 1 attack range, but wants 
		to attack for 2 distance, there will be a failure.  This also checks
		for whether the player has enough energy to attack.
		Note:weapon /must/ have an energy cost.
	"""
	def validAttack(self,weapon,range):
		
			if weapon.isValidRange(range):
				if self.hasEnergy(weapon.energyCost):
					return weapon.damage
		
class Grongus(Character):
		def __init__(self):
			super().__init__("Grongus",1,0,"G")
			
			
class Spear(Character):
		def __init__(self):
			super().__init__("Spear",1,0,"|")
			self.range = 1
			self.energyCost = -1
			self.damage = 1
			
			
		def isValidRange(self,range):
			if range <= self.range:
				return True
			raise GrongusExceptions.NotWithinRange()
		
		
	
		