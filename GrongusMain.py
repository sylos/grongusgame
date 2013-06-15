#HuntTheGrongus
"""Objective:Hunt down the grongus, which exists in one of several rooms
Coded in python.  An experiment in early python programming.
Author: Thomas Pachura
Coded in notepad++, compiled with Python 3.3
"""

import GrongusExceptions
import GrongusMap
import random


"""This one controls the flow of the gameplay.  While I'm sure there's a way to do
it without the need for a class, I don't know how.  So, the game is controlled
/created inside GrongusMain for mental ease.
"""
class GrongusMain:
	
	def __init__(self):
		random.seed()
		
		self.x = int(random.randint(0,4))
		self.y = int(random.randint(0,4))
		print("x: ",self.x,"y:",self.y)
		grongusMap = GrongusMap.GrongusMap(self.x,self.y)
		

grongusMain = GrongusMain()

while True:
	action = input("What do you do?")
	
	
