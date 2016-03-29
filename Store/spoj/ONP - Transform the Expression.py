# SPOJ No: 4
# SPOJ Code: ONP
# Title: Transform the Expression
# Status: accepted
# Time: 0.4
# Memory: 11M 	
# Language: PYTH 3.2.3
# Date: 16/01/2014
# Problem: Transform the algebraic expression with brackets into RPN form 
# (Reverse Polish Notation). Two-argument operators: +, -, *, /, ^ 
# (priority from the lowest to the highest), brackets ( ). Operands: only 
# letters: a,b,...,z. Assume that there is only one RPN form (no expressions 
# like a*b*c).
# Input: 
# t [the number of expressions <= 100]
# expression [length <= 400]
# [other expressions]

# Text grouped in [ ] does not appear in the input file.
# Output
# The expressions in RPN form, one per line.
# Input:
# 3
# (a+(b*c))
# ((a+b)*(z+x))
# ((a+t)*((b+(a+c))^(c+d)))
# Output:
# abc*+
# ab+zx+*
# at+bac++cd+^*
# 

import re
digit = re.compile('\w')

ops = {'^': [3, 'R'],
 '*': [2, 'L'], 
 '/': [2, 'L'], 
 '+': [1, 'L'],
 '-': [1, 'L']
 }
 
paren = ['(',')']
digits = [0,1,2,3,4,5,6,7,8,9]


	
inp = input()
for i in range(int(inp)):
	out = ''
	stack = []
	exp = input()
	for o1 in exp:
		# print(o1)
		# print (inp, stack, out)
		if digit.match(o1): 
			out += o1
		elif o1 in ops:
			if len(stack) > 0:
				while True:
					o2 = stack[-1]
					if ((o2 in ops)
						and ((ops[o1][1]=='L' and ops[o1][0] == ops[o2][0]) 
						or (ops[o1][0] < ops[o2][0]))):
							out += stack.pop()
					else: break
			stack.append(o1)
		elif o1 == '(':
			stack.append(o1)
		elif o1 == ')':
			while True:
				o2 = stack[-1]
				if o2 == '(': 
					stack.pop()
					break
				else: out += stack.pop()
		else: break
	
	while len(stack) > 0:
		o2 = stack[-1]
		if o2 in paren:
			print("error")
			break
		else:
			out += stack.pop()
			
	print(out)

