"""
Given a non-empty array where each element represents a digit of a non-negative integer,
add one to the integer. The most significant digit is at the front of the array and each
element in the array contains only one digit. Furthermore, the integer does not have
leading zeros, except in the case of the number '0'.

Example:

Input: [2,3,4]
Output: [2,3,5]
"""
import unittest

from hamcrest import assert_that, equal_to


class Solution:
    def reverse(self, digits):
        i = len(digits) - 1
        res = []
        while i >= 0:
            res.append(digits[i])
            i -= 1
        return res

    def plus_one(self, digits):
        rev = self.reverse(digits)
        rev[0] = rev[0] + 1
        for i, digit in enumerate(rev):
            if digit >= 10:
                rev[i] = 0
                if i >= 0:
                    rev[i+1] += 1
        return self.reverse(rev)


class Test(unittest.TestCase):

    def test_reverse(self):
        assert_that(Solution().reverse([1, 3, 5]), equal_to([5, 3, 1]))

    def test(self):
        assert_that(Solution().plus_one([2, 9, 9]), equal_to([3, 0, 0]))
        assert_that(Solution().plus_one([0]), equal_to([1]))
