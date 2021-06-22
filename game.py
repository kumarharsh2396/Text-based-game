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