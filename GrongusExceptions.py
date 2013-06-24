#GrongusExceptions

class Error(Exception):
	"""base exception for grongus exceptions."""
	pass

class OutOfBounds(Error):
	"""For when the character reaches an edge case"""
	def __init__ (self,edge,msg):
		self.edge = edge
		self.message = msg
		
class NothingThere(Error):
	"""for when attacking something that doesn't exist"""
	def __init__(self):
		self.message = "There's nothing to attack there!"
		
class NotEnoughEnergy(Error):
	def __init__(self):
		self.message = "Not enough energy!"
		
class NotWithinRange(Error):
	def __init__(self,target):
		
		self.message = target + " not within range!"
		
class containsObject(Error):
	def __init__ (self,msg):
		self.message = msg
		
class NonCardinalDirection(Error):
	def __init__(self,msg):
		self.message = msg