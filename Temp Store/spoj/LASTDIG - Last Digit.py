# SPOJ No: 3442
# SPOJ Code: LASTDIG
# Title: The Last Digit
# Status: accepted
# Time: 0.1s
# Memory: 11M
# Language: Python 3.2.3
# Date: 17/01/2014
# Problem:
# Given two integers a and b print the last digit of the number a^b. 
# 0 <= a <= 20 and 0 <= b <= 2147483000 (a and b cannot both be 0)
# Input:
# 2
# 3 10
# 6 2
# Output:
# 9
# 6


# see http://mathforum.org/library/drmath/view/55877.html for explanation of the 
# digits.
digits = {}
for i in range(21):
	digits[i]=[]
	for j in range(1, 5):
		last = str(i**j)[-1]
		digits[i].append(str(i**j)[-1])

t = int(input())
for i in range(t):
	a, b = input().split()
	a = int(a)
	b = int(b)
	if(a == 0): 
		print(0)
	elif(b == 0):
		print(1)
	else:
		print(digits[a][b%4-1])


