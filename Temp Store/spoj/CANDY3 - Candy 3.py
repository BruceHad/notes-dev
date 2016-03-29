# SPOJ No: 2148
# SPOJ Code: CANDY3
# Title: Candy III
# Status: accepted
# Time: 0.83
# Memory: 11M
# Language: Python 3.2.3
# Date: 03/04/2014
# 
# A class went to a school trip. And, as usually, all N kids have got their backpacks 
# stuffed with candy. But soon quarrels started all over the place, as some of the kids 
# had more candies than others. Soon, the teacher realized that he has to step in: 
# "Everybody, listen! Put all the candies you have on this table here!"
# Soon, there was quite a large heap of candies on the teacher's table. "Now, I will 
# divide the candies into N equal heaps and everyone will get one of them." announced 
# the teacher.
# "Wait, is this really possible?" wondered some of the smarter kids.
# Problem specification
# You are given the number of candies each child brought. Find out whether the teacher 
# can divide the candies into N exactly equal heaps. (For the purpose of this task, all 
# candies are of the same type.)
# Input specification
# The first line of the input file contains an integer T specifying the number of 
# test cases. Each test case is preceded by a blank line.
# 
# Each test case looks as follows: The first line contains N : the number of children. Each of the next N lines contains the number of candies one child brought.
# utput specification
# For each of the test cases output a single line with a single word "YES" if the candies can be distributed equally, or "NO" otherwise. 
# 

i = int(input())

for j in range(i):
	# print("Round",j)
	if(input()==''): N = int(input())
	total = 0
	for k in range(N):
		total += int(input())
	if total%N == 0: print("YES")
	else: print("NO")