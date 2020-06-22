# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.
#
# Example:
# Input: "banana"
# Output: "anana"
#
# Input: "million"
# Output: "illi"


import unittest
from hamcrest import assert_that, equal_to
from functools import reduce


class Solution:

    @staticmethod
    def get_substrings(s):
        result = []
        for s0 in range(len(s)):
            for s1 in range(s0, len(s)):
                result.append(s[s0:s1+1])
        return set(result)

    @staticmethod
    def is_palindrome(s):
        arr = [c for c in s]
        arr.reverse()
        result = "".join(arr)
        return s == result

    def longest_palindrome(self, s):
        sub = self.get_substrings(s)
        palindormes = filter(lambda s: self.is_palindrome(s), sub)
        return reduce(lambda max, el: max if len(max) > len(el) else el, palindormes, "")


class Test(unittest.TestCase):
    def test(self):
        result = str(Solution().longest_palindrome("tracecars"))
        assert_that(result, equal_to("racecar"))
