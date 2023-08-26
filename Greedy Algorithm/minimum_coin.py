from os import *
from random import randint
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):

	# Write your code here
	res = 0
	i = len(denominations) - 1
	while amount>0 and i>=0:
		if amount%denominations[i]!=amount:
			factor = amount//denominations[i]
			amount -= factor*denominations[i]
			res += factor
		i -= 1
	return res
print(findMinimumCoins(93))		

            
		