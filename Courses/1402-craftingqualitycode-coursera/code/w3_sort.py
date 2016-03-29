def bubble_sort(L):
	""" list -> NoneType

	Sort the items of L from smallest to largest.

	>>> L = [7, 3, 5, 2]
	>>> bubble_sort(L)
	>>> L
	[2, 3, 5, 7]
	"""

	e = len(L) - 1

	while e > 0:
		i = 0
		while i < e:
			if L[i] > L[i+1]:
				L[i], L[i+1] = L[i+1], L[i]
			i += 1
		e -= 1

def get_index_of_smallest(L, i):
	""" (list, int) -> int

	Return the index of the smallest item in L[i:]
	 
	>>> get_index_of_smallest([2, 7, 3, 5], 1)
	2
	"""
	index_small = i
	for j in range(i + 1, len(L)):
		if L[j] < L[index_small]:
			index_small = j
	return index_small


def select_sort(L):
	""" list -> NoneType

	Sort the items of L from smallest to largest.

	>>> L = [7, 3, 5, 2]
	>>> select_sort(L)
	>>> L
	[2, 3, 5, 7]
	"""
	for i in range(len(L)):
		index_small = get_index_of_smallest(L, i)
		L[index_small], L[i] = L[i], L[index_small]

def insert(L, i):
	""" (list, int) -> NoneType

	Precondition: L[:i] is sorted from smallest to largest

	Move L[i] to where it belongs in L[:i + 1]

	>>> L = [7, 3, 5, 2]
	>>> insert(L, 1)
	>>> L
	[3, 7, 5, 2]

	"""

	value = L[i]

	j = i

	while j != 0 and L[j-1] > value:
		L[j] = L[j - 1]
		j -= 1

	L[j] = value


def insert_sort(L):
	""" list -> NoneType

	Sort the items of L from smallest to largest.

	>>> L = [7, 9, 3, 5, 2]
	>>> insert_sort(L)
	>>> L
	[2, 3, 5, 7, 9]
	"""

	for i in range(len(L)):
		insert(L, i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()