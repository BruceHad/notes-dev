# SPOJ No: 1
# SPOJ Code: TEST
# Title: Life, the Universe and Everything
# Status: accepted
# Time: 0.03
# Memory: 3.7M 	
# Language: PYTH 2.7
# Date: 
# Problem: Your program is to use the brute-force approach in order to 
# find the Answer to Life, the Universe, and Everything. More 
# precisely...rewrite small numbers from input to output. Stop 
# processing input after reading in the number 42. All numbers 
# at input are integers of one or two digits.
# Example:
#    Input:
#    1
#    2
#    88
#    42
#    99
#    Output:
#    1
#    2
#    88


import sys

x = sys.stdin.readlines()
for line in x:
	value = int(line.rstrip())
	if(value) == 42:
		sys.exit()
	else:
		print value