# SPOJ No: 6
# SPOJ Code: ARITH
# Title: Simple Arithmetics
# Status: accepted
# Time: 1.2
# Memory: 11M
# Language: Python 3.2.3
# Date: 
#  One part of the new WAP portal is also a calculator computing expressions with very 
#  long numbers. To make the output look better, the result is formated the same way as 
#  is it usually used with manual calculations.Your task is to write the core part of 
#  this calculator. Given two numbers and the requested operation, you are to compute 
#  the result and print it in the form specified below. With addition and subtraction, 
#  the numbers are written below each other. Multiplication is a little bit more 
#  complex: first of all, we make a partial result for every digit of one of the 
#  numbers, and then sum the results together.
#  t
#  For each expression, print two lines with two given numbers, the second number below 
#  the first one, last digits (representing unities) must be aligned in the same column. 
#  Put the operator right in front of the first digit of the second number. After the 
#  second number, there must be a horizontal line made of dashes (-).
#  
#  For each addition or subtraction, put the result right below the horizontal line, with 
#  last digit aligned to the last digit of both operands.
#  
#  For each multiplication, multiply the first number by each digit of the second number. 
#  Put the partial results one below the other, starting with the product of the last digit 
#  of the second number. Each partial result should be aligned with the corresponding digit. 
#  That means the last digit of the partial product must be in the same column as the digit 
#  of the second number. No product may begin with any additional zeros. If a particular 
#  digit is zero, the product has exactly one digit -- zero. If the second number has more 
#  than one digit, print another horizontal line under the partial results, and then print 
#  the sum of them.
#  
#  There must be minimal number of spaces on the beginning of lines, with respect to other 
#  constraints. The horizontal line is always as long as necessary to reach the left and 
#  right end of both numbers (and operators) directly below and above it. That means it 
#  begins in the same column where the leftmost digit or operator of that two lines (one 
#  below and one above) is. It ends in the column where is the rightmost digit of that two 
#  numbers. The line can be neither longer nor shorter than specified.
#  Print one blank line after each test case, including the last one.
#  Example Sample Input:
# 4
# 12345+67890
# 324-111
# 325*4405
# 1234*4
# Sample Output:
# 
#  12345
# +67890
# ------
#  80235
#  
#  324
# -111
# ----
#  213
#  
#     325
#   *4405
#   -----
#    1625
#      0
#  1300
# 1300
# -------
# 1431625
# 
# 1234
#   *4
# ----
# 4936
# 

import re

def arith(input):
	# Get basic information
	r = re.compile('[\+\-\*]')
	pos = r.search(input).start()
	op = input[pos]
	first = input[:pos]
	second = input[pos+1:]
	answer = str(eval(first+op+second))
	width = max(len(first), len(second)+1, len(answer))

	# Build each line for result
	lines = []
	lines.append(first.rjust(width))
	lines.append((op+second).rjust(width))
	if(op == '*' and len(second) > 1):
		third = str(int(second[-1])*int(first))
		lines.append((max(len(op+second), len(third))*'-').rjust(width))
		for i in range(len(second)):
			k = -1 - i
			lines.append(str(int(second[k])*int(first)).rjust(width-i))
		lines.append((len(answer)*'-').rjust(width))
	else:
		lines.append((max(len(op+second), len(answer))*"-").rjust(width))
	lines.append(answer.rjust(width))

	# Compile Results
	result = ""
	for line in lines:
		result += line + '\n'
	return result

if __name__ == '__main__':
	for i in range(int(input())):
		result = arith(input())
		print(result)