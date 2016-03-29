# SPOJ No: 4300
# SPOJ Code: AE00
# Title: Rectangles
# Status: accepted
# Time: 1.18s
# Memory: 11M
# Language: Python 3.2.3
# Date: 01/04/2014
# Problem:
# You are given a number n of square tiles. How many distinct rectangles can 
# you create using those tiles. (Note, 1. You don't have to use all the tiles 
# for each rectangle, 2. A square is a type of rectangle.)

import math

def countRectangles(n):
	if n==1: return 1
	total = 0
	sides = math.floor(math.sqrt(n))
	# print("Sides: ", sides)
	for i in range(1, sides+1):
		if i == 1: 
			no = n
		else: 
			no = max(n//i-i+1,0)
		total += no
		# print("No. :", i, no)
	return total
n = int(input())
print(countRectangles(n))


