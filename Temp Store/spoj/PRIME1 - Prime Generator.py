# SPOJ No: 2
# SPOJ Code: PRIME1
# Title: Prime Generator
# Status: accepted
# Time: 2.08
# Memory: 3.8M 	
# Language: PYTH 2.7
# Date: 13/03/2012
# Problem: Peter wants to generate some prime numbers for his cryptosystem. 
# Help him! Your task is to generate all prime numbers between two given 
# numbers! Input: The input begins with the number t of test cases in a 
# single line (t<=10). In each of the next t lines there are two numbers m and n 
# (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.
# Output: For every test case print all prime numbers p such that 
# m <= p <= n, one number per line, test cases separated by an empty line.
# Input:
# 2
# 1 10
# 3 5
# Output:
# 2
# 3
# 5
# 7
# 3
# 5

import math

def rwh_primes2(n):
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


primes = rwh_primes2(32000)

count = input()
 
for t in range(count):
	min,max = raw_input().split(' ')
	min = int(min)
	if min<2: min = 2
	max = int(max)
	cap = math.sqrt(max)+1
	results = [True]*100001 # array of results initially set to True
	output = ""
	
	for i in primes:
		if(i >= cap): break
		if(i >= min):
			start = i*2
		else:
			start = min + ((i - min % i)%i)
		falseblock = [False] * len(results[start-min:max+1-min:i])
		results[start-min:max+1-min:i] = falseblock
		
	for i in range(min,max+1):
		if (results[i-min] == True):
			output += str(i) + "\n"
	print output
	print ""