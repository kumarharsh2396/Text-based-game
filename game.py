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