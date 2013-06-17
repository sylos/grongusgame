#HuntTheGrongus
"""Objective:Hunt down the grongus, which exists in one of several rooms
Coded in python.  An experiment in early python programming.
Author: Thomas Pachura
Coded in notepad++, compiled with Python 3.3
"""

import GrongusExceptions
import GrongusMap
import GrongusCharacter
import random


"""This one controls the flow of the gameplay.  While I'm sure there's a way to do
	it without the need for a class, I don't know how.  So, the game is controlled
	/created inside GrongusMain for mental ease.
"""
class GrongusMain:
	
	def __init__(self):
		random.seed()
		self.x = 4 #int(random.randint(1,4))
		self.y = 4 #int(random.randint(1,4))
		#print("x: ",self.x,"y:",self.y)
		self.grongusMap = GrongusMap.GrongusMap(self.x,self.y)

grongusMain = GrongusMain()
player = GrongusCharacter.Player(grongusMain.x-1,grongusMain.y-1)
grongusMain.grongusMap.startPosition(grongusMain.x-1,grongusMain.y-1,player)
grongusMain.grongusMap.printMap()

while True:
	try:
		action = input("What do you do? ")
		if action == "q" or action == "quit":
			print("in q")
			break
		elif action == "n" or action == "north":
			x = player.coords['x'] 
			y = player.coords['y'] -1
			if y < 0:
				raise GrongusExceptions.OutOfBounds(y,"You have reached the top of the cave")
		elif action == "s" or action == "south":
			x = player.coords['x']
			y = player.coords['y'] + 1
			if y >= grongusMain.y:
				raise GrongusExceptions.OutOfBounds(y,"You have reached the bottom of the cave")
		elif action == "w" or action == "west":
			x = player.coords['x'] - 1
			y = player.coords['y']
			if x < 0:
				raise GrongusExceptions.OutOfBounds(y,"You have reached the edge of the cave")
		elif action == "x" or action == "east":
			x = player.coords['x'] + 1
			y = player.coords['y']
			if x >= grongusMain.x:
				raise GrongusExceptions.OutOfBounds(y,"You have reached the edge of the cave")
		grongusMain.grongusMap.movePlayer(x,y,player)
		grongusMain.grongusMap.printMap()
	except GrongusExceptions.OutOfBounds as e:
		print(e.message)
			
	
