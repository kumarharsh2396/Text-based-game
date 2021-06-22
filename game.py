import csv
import click
import random

# Function to load .csv to a list and return it
def generateList(topicName):
	fileName = "CSVs/" + topicName + ".csv"

	with open(fileName, 'r') as f:
	    reader = csv.reader(f)
	    rawList = list(reader)

	itemList = []
	for miniList in rawList:
		for item in miniList:
			itemList.append(item.lower())

	return itemList

def chooseGenre(beenHere):
	
	click.clear()	
	# List of all available topics
	print("Choose one of the following topics:\n")
	print("1. Fruits")
	print("2. Countries")
	print("3. Names")
	# Add more choices here

	if not beenHere:
		choice = input("\nChoose one of the above options: ")
	else:
		choice = input("\nPlease choose a valid option from above: ")	

	if choice == "1":
		return "fruits"
	elif choice == "2":
		return "countries"
	elif choice == "3":
		return "Names"	

	# Add more elif statements here	
	else:
		 return chooseGenre(True)	


# Function for a new game
def newGame():

	genre = chooseGenre(False)
	itemList = generateList(genre)
	
	# If Items loaded into itemList, proceed to play. Else, abort.
	if len(itemList) > 0:
		print("Loaded List Successfully. Proceed to play the game")
	else:
		print("Error loading items into the list. Aborting!")
		exit()

	# A list that keeps track of the items mentioned in the game
	gameList = []

	# Game continues until the itemList is exhausted
	while len(itemList) > 0:

		# Player's turn
		click.clear()
		print(genre.upper() + "\n")
		print("Player's Turn\n")

		if len(gameList) > 0:
			print("Enter the list itemwise, in order, as you remember it. If you forget any of the items, type in 'idk' in its place.")

		# List to maintain the entries of the player	
		playerList = []

		# Ask the player to enter all the items mentioned so far
		for i in range(len(gameList)):
			playerEntry = input("Item " + str(i+1) + ": ").lower()
			# Break out, incase the player forgets in the middle
			if playerEntry == "idk":
				break
			# If an entry is made, append it to the playerList	
			playerList.append(playerEntry)

		# Checking if the player remebers the items correctly:
		areSame = True
		# If the length of both the lists are same and the contents are also the same, the player gets to proceed.
		if len(gameList) == len(playerList):
			for i in range(len(gameList)):
				if playerList[i] != gameList[i]:
					areSame = False
		# If the length of the lists are different, the player had typed an idk in the middle. So end the game.			
		else:
			areSame = False		

		# If the lengths were the same but the list items were different, then also end the game.	
		if not areSame:
			break

		# Motivate the player for remebering right
		if len(gameList) > 0:
			print("\nGood job! You remember the list right.\n")

		# Prompt player to add new item to the list	
		newInput = input("Add a new item to the list: ").lower()

		# Check if the entry is valid for given genre or if the

		knowsMore = True
		while newInput not in itemList:
			print("Sorry! That item is invalid! Enter a valid item or enter 'idk' if you don't know any more items:")
			newInput = input()
			if newInput == "idk":
				knowsMore = False
				break

		if not knowsMore:
			break

		print("\n'" + newInput.upper() +"' added to the list!")	

		# Once a valid input is made, remove it from itemList, so it cannot be repeated. Add it to gameList so it is in play.
		itemList.remove(newInput)
		gameList.append(newInput)


		# Print updated List
		print("\nThe updated list is:\n")
		for item in gameList:
			print(item)

		print("\nHit enter to continue.")
		input()

		# Computer's turn

		click.clear()
		print("FRUITS\n")
		print("Computer's Turn\n")

		# Make a random choice from the ones available and add it to the gameList. Also, remove from itemList so that it can't be repeated
		choiceIndex = random.randrange(0, len(itemList))
		gameList.append(itemList[choiceIndex])
		itemList.remove(itemList[choiceIndex])

		# Prompt the user of the new item.
		print("Computer adds '" + gameList[-1].upper() + "' to the list. This list is now:\n")

		# Print the updated list for them to memorize
		for item in gameList:
			print(item)

		print("\nMemorize this list. Hit enter when you're ready!")
		input()

	# If by some miracle, they manage to empty the itemList, they win. 
	if len(itemList) == 0:
		print("\nYou Won!")
	elif not knowsMore:	
		print("\nYou could have said " + itemList[random.randrange(0, len(itemList))].upper() + ". ;)")
	else:
		print("\nSorry! Looks like you forgot! The list was:\n")
		for item in gameList:
			print(item)
		
	print("\nGood Run! Your score is " + str(len(gameList)) + ".\n")	

	input("Press enter to return to main menu")	



def instructions():
	click.clear()
	print("INSTRUCTIONS\n")
	with open("instructions.txt", "r") as f:
		print(f.read())	
	print("\nChoose one of the following:")
	print("1. Start the game")
	print("2. Quit")
	choice = input("\nChoose one of the above options: ")

	while choice not in ["1", "2"]:
		choice = input("Please enter a valid option: ")

	if(choice == "1"):
		newGame()
	else:
		print("\nGoodbye!")
		exit()

def main():
	click.clear()
	print("MEMORY GAME\n")
	print("Welcome to the memory game! Choose one of the following:\n")
	print("1. New Game")
	print("2. Instructions")
	print("3. Quit")

	choice = input("\nChoose one of the above options: ")

	while choice not in ["1", "2", "3"]:
		choice = input("Please enter a valid option: ")

	if(choice == "1"):
		newGame()
	elif(choice == "2"):
		instructions()
	else:
		print("Goodbye!")
		exit()	

if __name__ == "__main__":
	main()