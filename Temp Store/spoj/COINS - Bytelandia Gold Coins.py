# SPOJ No: 346
# SPOJ Code: Coins
# Title: Bytelandian gold coins
# Status: accepted
# Time: 0.11
# Memory: 11M
# Language: Python 3.2.3
# Date: 24/06/2014
# 
#  Each Bytelandian gold coin has an integer number written on it. A coin n can be 
#  exchanged in a bank into three coins: n/2, n/3 and n/4. But these numbers are all 
#  rounded down (the banks have to make a profit).
#  
#  You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. 
#  But you can not buy Bytelandian coins.
#  You have one gold coin. What is the maximum amount of American dollars you can get for 
#  it?
#  Input - The input will contain several test cases (not more than 10). Each testcase 
#  is a single line with a number n, #  0 <= n <= 1 000 000 000. It is the number written 
#  on your coin.
#  
#  Output - For each test case output a single line, containing the maximum amount of 
#  American dollars you can make.
#  
#  Example Input:
#  12
#  2
#  Output:
#  13
#  2
#  You can change 12 into 6, 4 and 3, and then change these into $6+$4+$3 = $13. If you try 
#  changing the coin 2 into 3 smaller coins, you will get 1, 0 and 0, and later you can get 
#  no more than $1 out of them. It is better just to change the 2 coin directly into $2. 

import sys
map = {}
def convert(n):
	if(n < 12):
		return n
	elif(n in map):
		return map[n]
	a = n//2
	b = n//3
	c = n//4
	result = convert(a) + convert(b) + convert(c)
	map[n] = result
	return (result)

if __name__ == '__main__':
	for line in sys.stdin:
		dollar = convert(int(line))
		print(dollar)