def linear_search(L, v):
	""" (list, object) -> int

	Return the index of the first occurence of v in L, or
	return -1 if v is not in L.

	>>> linear_search([2, 3, 5, 3], 2)
	0
	>>> linear_search([2, 3, 5, 3], 5)
	2
	>>> linear_search([2, 3, 5, 3], 8)
	-1

	"""
	for i in range(len(L)):
		if L[i] == v:
			return i
	return -1

def binary_search(L, v):
	""" (list, object) -> int

	Precondition: L is sorted from smallest to largest, and
	all the items in L can be compared to v.

	Return the index of the first occurence of v in L, or
	return -1 if v is not in L.

	>>> linear_search([2, 3, 5, 3], 2)
	0
	>>> linear_search([2, 3, 5, 3], 5)
	2
	>>> linear_search([2, 3, 5, 3], 8)
	-1

	""" 
	b = 0
	e = len(L) - 1

	while b <= e:
		m = b + (e - b)//2		
		if L[m] < v:
			b = m + 1
		else:
			e = m - 1

	if b == len(L) or L[b] != v:
		return -1
	else:
		return b

if __name__ == "__main__":
    import doctest
    doctest.testmod()