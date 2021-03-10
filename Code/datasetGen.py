import random
import sys
import math

NO_OF_TRANSACTION = 4000
MAX_FREQ_ITEMSET_SIZE = 8
TRANSACTION_AVG_WIDTH = 10
TOTAL_ITEMS = 350
FREQ_COUNT = 20 # default
FREQ_RATIO = 0.05

# DATASET
dataSet = []

def gernerate_random_array(totalSum):
	lowerbound = 1
	upperbound = 2 * TRANSACTION_AVG_WIDTH 
	nums = [lowerbound] * NO_OF_TRANSACTION
	diff = totalSum - lowerbound * NO_OF_TRANSACTION
	while diff > 0:
		randIndex = random.randint(0,NO_OF_TRANSACTION - 1)
		if nums[randIndex] >= upperbound:
			continue
		nums[randIndex] += 1
		diff -= 1
	return nums
def GenerateData():
	# create Data List
	for i in range(0,NO_OF_TRANSACTION):
		dataSet.append([])
	#Generate Random Index
	RandomIndex = random.sample(range(0, NO_OF_TRANSACTION), FREQ_COUNT)
	
	# Gererate Random MaxFreqItemSet
	RandomFreqItemSet = random.sample(range(0,TOTAL_ITEMS), MAX_FREQ_ITEMSET_SIZE)
	setA = set()
	for item in RandomFreqItemSet:
		setA.add(item)
	setB = set()
	for i in range(0,TOTAL_ITEMS):
		setB.add(i)
	choiceSet = setB.difference(setA)
	choiceSet = list(choiceSet)
	# insert Item random Index
	for index in RandomIndex:
		dataSet[index].extend(RandomFreqItemSet)
	
	total_item = NO_OF_TRANSACTION * TRANSACTION_AVG_WIDTH
	itemRemaining = total_item - FREQ_COUNT * MAX_FREQ_ITEMSET_SIZE
	arr_of_item_count = gernerate_random_array(itemRemaining)

	index = 0
	Repeat = False
	while index < NO_OF_TRANSACTION:
		randomItemSet = []
		if len(dataSet[index]) == 0:
			randomItemSet = random.sample(range(0, TOTAL_ITEMS),arr_of_item_count[index])
		else:
			randomIndex = []
			try:
				randomIndex = random.sample(range(0,len(choiceSet)), arr_of_item_count[index])
			except:
				diff = arr_of_item_count[index] - len(choiceSet)
				randomIndex = random.sample(range(0,len(choiceSet)), len(choiceSet))
				if index+1 != NO_OF_TRANSACTION:
					arr_of_item_count[index+1] += diff
				else:
					arr_of_item_count[0] += diff
					Repeat = True
			for i in randomIndex:
				randomItemSet.append(choiceSet[i])
		dataSet[index].extend(randomItemSet)
		if Repeat:
			index = 0
		else:
			index += 1
			
	
	
	
	
def main():
	args = sys.argv 
	global FREQ_COUNT
	global NO_OF_TRANSACTION
	global MAX_FREQ_ITEMSET_SIZE
	global TOTAL_ITEMS
	global TRANSACTION_AVG_WIDTH
	try:
		 NO_OF_TRANSACTION = int(args[1])
		 MAX_FREQ_ITEMSET_SIZE = int(args[2])
		 TOTAL_ITEMS = int(args[3])
		 TRANSACTION_AVG_WIDTH = int(args[4])
	except:
		print('Error in Command Line Input!\nPlease Enter Format: python <No_Of_Transaction> <MaxFreqItemSize> <TotalItems> <AvgWidth>\n')
		return
	FREQ_COUNT = math.ceil(NO_OF_TRANSACTION * FREQ_RATIO)
	GenerateData()
	count = 0
	f = open("Data/DataGenerated.txt", "w")
	for trans in dataSet:
		count += len(trans)
		items = ' '.join(map(str, trans))
		items += ' ' + "\n"
		f.write(items)
	f.close()
	print('Data Set Generation done!!')
	#print(list(random_ints_with_sum(10)))
	
if __name__ == "__main__":
    main()
