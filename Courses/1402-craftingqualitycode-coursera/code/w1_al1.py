def is_palindrome(s):

    """ (str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome('noon')
    True

    """

    if reverse(s) == s:
        return True
    else:
        return False

def reverse(s):
    """ (str) -> str
    
    Return a reversed version of s.

    """

    rev = ''

    for ch in s:
        rev = ch + rev

    return rev
