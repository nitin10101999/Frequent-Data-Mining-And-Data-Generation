import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def plotRelation(x,y,ylabel):
	plt.figure(figsize=(8, 6),dpi=100)
	plt.xlabel(ylabel)
	plt.ylabel('Time (Seconds)')
	#plt.figure(dpi=100)
	plt.plot(x,y[0],label = 'Apriori')
	plt.plot(x,y[1],label = 'FPTree ')
	plt.plot(x,y[2],label = 'Eclat')
	plt.legend()
	
	
yData = [
	[2.77,4.35,5.48], #Apriori
	[2.73,4.2,5.38], #FPTree
	[0.04,0.05,0.07]	 #Eclat
]

plotRelation([2000,3000,4000],yData,'No. of Transactions')
#-------------------------------------------------------------------------------
yData = [
	[3.3,4.35,39.37], #Apriori
	[3.0,4.2,9.94], #FPTree
	[0.04,0.05,0.22]	 #Eclat
]
plotRelation([8,10,13],yData,'Avg. Width of Transaction')
#-------------------------------------------------------------------------------
yData = [
	[4.35,4.3,5.72], #Apriori
	[4.2,4.11,4.23], #FPTree
	[0.052,0.05,0.053]	 #Eclat
]
plotRelation([50,60,70],yData,'Total Items')
#-------------------------------------------------------------------------------
yData = [
	[2.84,4.35,151.0], #Apriori
	[3.74,4.21,6.92], #FPTree
	[0.044,0.05,0.25]	 #Eclat
]
plotRelation([8,10,15],yData,'Max Freq ItemSet Size')
#---------------------------------------------------------------------------------
#Problem 1 plot
####Data 1
yData = [
	[41.06,38.49,38.01,37.68], #Apriori
	[38.99,41.85,42.89,46.71], #FPtree
	[1.32,1.3,1.28,1.28] #Eclat
]
plotRelation([0.05,0.06,0.08,0.1],yData,'Min Support')

####Data 2
yData = [
	[4384.9,3987.61,3256.89,2867.65], # apriori
	[3421.45,2675.25,1438.2,612.53], # Fptree
	[12.5,9.34,5.74,4.12] #Eclats
]
plotRelation([0.05,0.06,0.08,0.1],yData,'Min Support')

####data 3

yData = [
	[457.57,655.26,672.47,647.9], # apriori
	[671.95,612.7,656.9,637.03],  # Fptree
	[27.74,33.5,31.05,38.7]  #Eclat
]
plotRelation([0.05,0.06,0.08,0.1],yData,'Min Support')

#####data 4
yData = [
	[1.9,1.07,0.64,0.44], #apriori
	[1.6,1.05,0.67,0.47], # Fptree
	[0.083,0.08,0.078,0.076], #Eclat
]
plotRelation([0.05,0.06,0.08,0.1],yData,'Min Support')

