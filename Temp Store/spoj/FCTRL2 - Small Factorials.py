# SPOJ No: 24
# SPOJ Code: FCTRL2
# Title: Small Factorials
# Status: accepted
# Time: 0.12
# Memory: 11M 	
# Language: PYTH 3.2.3
# Date: 20/01/2014

# You are asked to calculate factorials of some small positive integers.
# Input: An integer t, 1<=t<=100, denoting the number of testcases, followed by 
# t lines, each containing a single integer n, 1<=n<=100.
# Output: For each integer n given at input, display a line with the value of n!
# Sample input:
# 4
# 1
# 2
# 5
# 3
# Sample output:
# 1
# 2
# 120
# 6



def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		out = 1
		for j in range(2,n+1):
			out*=j
		print(out)

if __name__ == '__main__':
	main()