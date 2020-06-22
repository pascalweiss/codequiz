# Given a string, find the length of the longest substring without repeating characters.
import unittest
from hamcrest import assert_that, equal_to


class Solution:

    def lengthOfLongestSubstring(self, s):
        m = set()
        max = 0
        i = 0
        for c in s:
            if c in m:
                i = 0
                m = set()
            i += 1
            m.update(c)
            if i > max: max = i
        return max


class Test(unittest.TestCase):
    def test(self):
        assert_that(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'), equal_to(10))