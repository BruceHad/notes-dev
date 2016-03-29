def is_palindrome(s):

    """ (str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome('noon')
    True

    """
    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j - i]:
            return False

    return True
