def contains_item(L, s):
    """ (list, object) -> bool
    Return True if and only if s is an item of L.
    
    >>> contains_item([1, 2, 3], 1)
    True
    >>> contains_item([], 1)
    False
    >>> contains_item([1, 2, 3], 2)
    True
    >>> contains_item([1,2,3], 3)
    True
    
    """

    for item in L:
        if item == s:
            return True
        else:
            return False
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()