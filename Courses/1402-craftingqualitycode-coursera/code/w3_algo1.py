def print_ints(n):
	""" (int) -> NoneType

	Print the integers from 1 to n, inclusive.

	>>> print_ints(3)
	1
	2
	3
	"""

	for i in range(1, n + 1):
		print(i)

def print_odd_ints(n):
	""" (int) -> NoneType

	Print the odd integers from 1 to n, inclusive
	"""

	for i in range(1, n + 1, 2):
		print(i)

def print_pairs(n):
	""" (int) -> NoneType

	Print all combinations of pairs of integers 1 to n, inclusive
	"""

	for i in range(1, n+1):
		for j in range(1, n + 1):
			print(i, j)

def print_double_step(n):
	""" (int) -> NoneType
	Print the integers from 1 to n inclusive, with an initial 
	step size of 1 and each subsequent step size being twice
	as large as it was previously.
	"""

	i = 1
	while i < n + 1:
		print(i)
		i = i * 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()