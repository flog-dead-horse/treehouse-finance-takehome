#Question 3
##Create a function to compute N layer of a Pascal Triangle.

from math import comb

def computePascalRow(n):
	return [comb(n-1,r) for r in range(n)]

print (computePascalRow(3))

