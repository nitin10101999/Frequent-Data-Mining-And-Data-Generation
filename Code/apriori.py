# -*- coding: utf-8 -*-
"""Apriori.ipynb

Automatically generated by Colaboratory.

Original file is located at
		https://colab.research.google.com/drive/1Aj7EkMMA5ivUDGkAQZRsqo5lVDKZj4OD
"""

#import os
#os.chdir('/content/drive/My Drive/Code')

import numpy as np
import pandas as pd
import copy 
import math
import csv
import time
import sys
import os
import psutil

# Default value
MIN_SUPPORT_COUNT = 1
FRACTION = 0.005
NO_OF_TRANSACTION = 100
MAX_FREQ_ITEMSET_SIZE = 5
NO_OF_FREQ_ITEM = 1
TRANSACTION_AVG_WIDTH = 4
TOTAL_ITEMS = 10
EXECUTION_TIME = 0
MEMORY = 0 

def find_frequent_1_itemSet(data,uniqueItems):
	L1 = []
	for item in uniqueItems:
		countItem = 0
		for transaction in data:
			for transItem in transaction:
				if transItem == item:
					countItem = countItem + 1
					break
		
		#If count>=MinSupportCount 
		if countItem >= MIN_SUPPORT_COUNT:
			newList = [item]
			L1.append(newList)
	
	return L1
def hasInFrequentSubset(L,K,c):
	isInFrequent = True
	for item in c:
		cSubset = []
		cSubset = c.copy()
		cSubset.remove(item)
		
		#	check C_subset in L
		for itemSet in L:
			if itemSet == cSubset:
				isInFrequent = False
		
	return isInFrequent


def AprioriUtil(L,K):
	C = []
	i = 0
	while i < len(L)-1:
		j = i+1
		l1 = L[i]
		while j <len(L):
			l2 = L[j]
			index = 0
			c	= []	#join List
			while index < K-1:
				if l1[index] != l2[index]:
					break
				c.append(l1[index])
				index = index + 1
			
			if index == K-1: #and l1[index] < l2[index]:
				c.append(l1[index])
				c.append(l2[index])
				#print(c)
				if not hasInFrequentSubset(L,K,c):
					C.append(c)
					#print('.',end='')
					#print(c)
			j = j+1
		i = i+1
					
	return C
		

def Apriori(data,uniqueItems):
	#print(data)
	#Find Frequent Item Set of 1 Size
	L = find_frequent_1_itemSet(data,uniqueItems)
	K = 2
	#print(AprioriUtil(L,K-1))
	pre = []
	while	len(L)>0:
		pre = L.copy()
		C = AprioriUtil(L,K-1)
		hash_Map	= [0]*len(C)
		index	= 0
		for transaction in data:
			index	= 0
			while index < len(C):
				if(set(C[index]).issubset(set(transaction))):
					hash_Map[index] = hash_Map[index] + 1
				index = index + 1
		L = []
		index = 0
		while index < len(C):
			if hash_Map[index] >= MIN_SUPPORT_COUNT:
				L.append(C[index])
			index = index + 1
		#print(L,end="\n")
		K = K +1
	global MAX_FREQ_ITEMSET_SIZE
	global NO_OF_FREQ_ITEM
	MAX_FREQ_ITEMSET_SIZE = len(pre[0])
	NO_OF_FREQ_ITEM = len(pre)
	print(pre)

def fetchtxtData(data,filename):
	# Using readlines() 
	file_read = open(filename, 'r') 
	Lines = file_read.readlines() 

	count = 0
	# Strips the newline character 
	TotalItems = 0
	UniqueItems = set()
	
	for line in Lines: 
		arr = line.split(" ")
		arr = arr[:len(arr)-1]
		UniqueItems = UniqueItems.union(set(arr))
		TotalItems = TotalItems + len(arr)
		data.append(arr)
		count = count + 1
	#set data
	global NO_OF_TRANSACTION
	global TRANSACTION_AVG_WIDTH
	global TOTAL_ITEMS

	NO_OF_TRANSACTION = count
	TRANSACTION_AVG_WIDTH = TotalItems/NO_OF_TRANSACTION
	TOTAL_ITEMS = len(UniqueItems)
	return list(UniqueItems)	

def fetchCSVdata(data,filename):
	reader = csv.reader(open(filename, 'r'), delimiter=',')
	DataSet = [list(row[1:]) for row in reader]
	DataSet = DataSet[1:]

	count = 0
	TotalItems = 0
	uniqueItems = set()
	for trans in DataSet:
		newlist = []
		for elem in trans:
			if elem == '':
				break
			newlist.append(elem)
		uniqueItems = uniqueItems.union(set(newlist))
		data.append(newlist)
		count += 1
		TotalItems += len(newlist)
	# set data
	global NO_OF_TRANSACTION
	global TRANSACTION_AVG_WIDTH
	global TOTAL_ITEMS
	NO_OF_TRANSACTION = count
	TRANSACTION_AVG_WIDTH = TotalItems/NO_OF_TRANSACTION
	TOTAL_ITEMS = len(uniqueItems)
	return list(uniqueItems)

def printData():
	print('----------------------------------------------------')
	print('Minimum support Count:',MIN_SUPPORT_COUNT)
	print('No of Transaction:',NO_OF_TRANSACTION)
	print('Avg Width of Transaction:',TRANSACTION_AVG_WIDTH)
	print('Total Items:',TOTAL_ITEMS)
	print('Max Freq Item Size:',MAX_FREQ_ITEMSET_SIZE)
	print('No of Freq Items:',NO_OF_FREQ_ITEM)
	print('Execution Time:',EXECUTION_TIME)
	print('Memory Used in Bytes',MEMORY)
def main():
	args = sys.argv 
	fileName = ''
	global FRACTION
	isCSV = True
	try:
		 fileName = args[1]
		 if fileName[-3:] == 'txt':
		 	isCSV = False
		 FRACTION = float(args[2])
	except:
		print('Error in Command Line Input!\nPlease Enter Format: python <DatafileName> <Fraction>')
		return
	start_time = time.time()
	
	data = []
	if isCSV:
		uniqueItems = fetchCSVdata(data,fileName)
	else:
		uniqueItems = fetchtxtData(data,fileName)

	global MIN_SUPPORT_COUNT
	MIN_SUPPORT_COUNT = math.ceil(NO_OF_TRANSACTION * FRACTION)
	#print(len(uniqueItems),MIN_SUPPORT_COUNT,NO_OF_TRANSACTION,FRACTION)
	Apriori(data,uniqueItems)

	end_time = time.time()
	global EXECUTION_TIME
	
	EXECUTION_TIME = end_time - start_time
	process = psutil.Process(os.getpid())
	global MEMORY
	MEMORY = process.memory_info().rss
	#print(process.memory_info().rss)  # in bytes 
	printData()

if __name__ == "__main__":
    main()
	
