#grongusMainTake2
import GrongusExceptions
import GrongusMap
import GrongusCharacter
#import GrongusActions
import random
import sys


def newGame():
	random.seed()
	
#be sure to change back to randomly picking the values for mapHeight and Width to random
	while True:
		try:
			value = input("Enter cave width: ")
			quitProgram(value)
			mapHeight = int(value)
			value = input("Enter cave height: ")
			quitProgram(value)
			mapWidth = int(value)
			if mapHeight <= 0 or mapWidth <= 0:
				print("Can't have a negative space cave!")
			else:
				break
		except ValueError:
			print("That's not a valid number!")
			
	
	randCoords = {'x':random.randint(1,mapWidth-1),'y':random.randint(1,mapHeight-1)}
	player = GrongusCharacter.Player(0, mapHeight-1)
	weapon = GrongusCharacter.Spear()
	player.addItems(weapon.name,weapon)
	grongus = GrongusCharacter.Grongus()
	map = GrongusMap.GrongusMap(mapHeight,mapWidth,player,grongus,randCoords)
	gameControl(player,grongus,map,mapWidth,mapHeight)
def quitProgram(input):
	if input.lower() == "q" or input.lower() == "quit":
		sys.exit()
		
def endGame(player,grongus):
	if grongus.curHealth <= 0:
		print("You have slain the Grongus!  In the distance...a horrible howl is heard...")
	elif player.curHealth <= 0:
		print("You have died.  Your body rests amongst the scattered corpses of the brave warriors who came before you.")
	elif player.curEnergy <= 0:
		print("Unable to slay your foe, you stumble out of the cave and collapse, beaten by your own lack of will")
	else:
		return
		
	action = input("New Game? Y/N: ").lower()
	
	if action == "y" or action == "yes":
		newGame()
	else:
		sys.exit()
		
def addDirection(thing, amount):
	thing += amount
	return thing
		
def gameControl(player,grongus,map,mapWidth,mapHeight):
	x = 0
	y = 0
	
	#insert exceptions and flow control for game.  Will do after refactoring of other code.
	while True:
		try:
			action = input("What do you do? ").lower()
			quitProgram(action)
			
			if action == "n" or action == "north": #y-1
				x = player.coords['x'] 
				y = addDirection(player.coords['y'],-1)
			elif action == "s" or action == "south": #y+1
				x = player.coords['x']
				y = addDirection(player.coords['y'],1)
			elif action == "w" or action == "west": # x-1
				x = addDirection(player.coords['x'],-1)
				y = player.coords['y']
			elif action == "e" or action == "east":#x+1
				x = addDirection(player.coords['x'],1)
				y = player.coords['y']
			#attack command tree
			elif action == "a" or action == "attack":
				x = player.coords['x']
				y = player.coords['y']
				attackD = input("Which direction?").lower()
				if attackD == "north" or attackD == "n": #y-1
					attackX = player.coords['x'] 
					attackY = addDirection(player.coords['y'],-1)	
				elif attackD == "south" or attackD == "s": #y+1
					attackX = player.coords['x'] 
					attackY = addDirection(player.coords['y'],1) 
				elif attackD == "west" or attackD == "w":#x-1
					attackX = addDirection(player.coords['x'],-1) 
					attackY = player.coords['y'] 
				elif attackD == "east" or attackD == "e": #x+1
					attackX = addDirection(player.coords['x'],1)
					attackY = player.coords['y'] 
				
				damage = player.validAttack(player.items["Spear"],1)
				map.gameMap[attackX][attackY].attackRoomContents(damage)
					
					
			elif action == "new game" or action == "ng":
				newGame()
			else:
				print("Please enter a proper command")
				x = player.coords['x']
				y = player.coords['y']
				
			if x >= mapWidth or x < 0 or y >= mapHeight or y < 0:
				x = player.coords['x']
				y = player.coords['y']
				map.printMap()
				raise GrongusExceptions.OutOfBounds(y,"You have reached the edge of the cave")
			
			map.playerMoved(x,y,player,grongus)
			player.printRawStats()
			map.printMap()
			endGame(player,grongus)
		except GrongusExceptions.OutOfBounds as e:
			print(e.message)
			
newGame()