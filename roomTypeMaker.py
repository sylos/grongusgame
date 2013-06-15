#CreateRoomList
#using pickling to learn about the process and to create a list that can be easily 
#read, since I can use dictionaries which make everything so much easier.
import pickle
def addRooms():
	with open("roomList.p","wb") as roomList:
		while True:
			roomName = input("Enter the room name: ") 
			if roomName == 'done':
				break
			roomChance = input("Enter the % chance of occurence: ")
			roomTypes[roomName]=roomChance
			
		pickle.dump(roomTypes,roomList)	
	
def delRoom():
	
	with open("roomList.p","rb") as roomList: 
		roomName = input("Enter the room name to delete: ")
		roomTypes = pickle.load(roomList)
		del roomTypes[roomName]
	with open("roomList.p","wb") as roomList:
		pickle.dump(roomTypes,roomList)
		
		
		

def viewList():
	with open("roomList.p","rb") as roomList:
		roomTypes = pickle.load(roomList)
		print (roomTypes)	
		
		
roomTypes = {}

while True:
	
	option = input("Add or view List: ")
	if option == "add":
		addRooms()
	elif option == "view":
		viewList()
	elif option == "del":
		delRoom()
	else:
		break
		

	

		
		