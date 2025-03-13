import unittest

def isPalindrome(s: str) -> bool:
    print('Check', s)
    l = len(s)
    if l == 1:
        return True
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def hasPalindrome(a: str, b: str) -> bool:
    """
    Given two strings of the same length, split both strings at the same index
    and check if combining the prefix of one string with the suffix of the other
    forms a palindrome.

    Args:
        a: a string
        b: a string, should be of the same length as `a`

    Returns:
        bool: True if a palindrome can be formed, False otherwise.

    Note:
    - This function raise ValueError if `a` and `b` have different length
    - Definition of palindrome is simplified to: a string, if spelled backward
      is identical to the string, then it's a palindrome.
    """
    if a is None or b is None or len(a) != len(b):
        raise ValueError("Two strings of equal length are required")

    for i in range(len(a)):
        if isPalindrome(a[:i+1].upper() + b[i+1:].upper()):
            return True
    return False

class TestGetStepCount(unittest.TestCase):
    def test_good_input(self):
        self.assertTrue(hasPalindrome('ab', 'ba'))
        self.assertFalse(hasPalindrome('xy', 'yz'))

    def test_length_1_is_palindrome(self):
        self.assertTrue(hasPalindrome('1', '1'))
        self.assertTrue(hasPalindrome('1', '3'))
    
    def test_mixed_cases(self):
        self.assertTrue(hasPalindrome('Edit', 'tide'))

    def test_missing_arg(self):
        with self.assertRaises(ValueError):
            hasPalindrome('ab', None)

    def test_mismatching_len(self):
        with self.assertRaises(ValueError):
            hasPalindrome('ab', 'xyz')
        with self.assertRaises(ValueError):
            hasPalindrome('', 'xyz')


if __name__ == "__main__":
    unittest.main()
