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
		self.msg = "There's nothing to attack there!"