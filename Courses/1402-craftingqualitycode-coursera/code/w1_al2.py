def is_palindrome(s):

    """ (str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome('noon')
    True

    """
    n = len(s)
    return s[:n // 2] == reverse(s[n-n//2:])

def reverse(s):
    """ (str) -> str

    """
    rev = ''
    for ch in s:
        rev = ch+rev

    return rev

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
