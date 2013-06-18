#grongusMainTake2
import GrongusExceptions
import GrongusMap
import GrongusCharacter
import random

random.seed()
#randInt = random.randint(0,100)
randCoords = {'x':2,'y':2}
#be sure to change back to randomly picking the values for mapHeight and Width to random
mapHeight = 4
mapWidth = 4
player = GrongusCharacter.Player(0, mapHeight-1)
grongus = GrongusCharacter.Grongus()
map = GrongusMap.GrongusMap(mapHeight,mapWidth,player,grongus,randCoords)


#insert exceptions and flow control for game.  Will do after refactoring of other code.
x = 0
y = 0
while True:
	try:
		action = input("What do you do? ").lower()
		if action == "q" or action == "quit":
			print("in q")
			break
		elif action == "n" or action == "north":
			x = player.coords['x'] 
			y = player.coords['y'] -1
		elif action == "s" or action == "south":
			x = player.coords['x']
			y = player.coords['y'] + 1
		elif action == "w" or action == "west":
			x = player.coords['x'] - 1
			y = player.coords['y']
		elif action == "e" or action == "east":
			x = player.coords['x'] + 1
			y = player.coords['y']
		if x >= mapWidth or x < 0 or y >= mapHeight or y < 0:
			x = player.coords['x']
			y = player.coords['y']
			map.printMap()
			raise GrongusExceptions.OutOfBounds(y,"You have reached the edge of the cave")
		
		map.playerMoved(x,y,player)
		player.updatePlayerPosition(x,y)
		map.printMap()
	except GrongusExceptions.OutOfBounds as e:
		print(e.message)