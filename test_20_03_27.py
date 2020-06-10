# Hi, here's your problem today. This problem was recently asked by Google:
# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#
# Example 1:
#
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

import unittest
from hamcrest import assert_that, equal_to


def sort_nums(nums):
    res = []
    one = 0
    two = 0
    three = 0
    for n in nums:
        if n is 1: one += 1
        if n is 2: two += 1
        if n is 3: three += 1
    while one + two + three > 0:
        if one > 0:
            res.append(1)
            one -= 1
        elif two > 0:
            res.append(2)
            two -= 1
        elif three > 0:
            res.append(3)
            three -= 1
    return res


class Test(unittest.TestCase):

    def test(self):
        assert_that(sort_nums([3, 3, 2, 1, 3, 2, 1]), equal_to([1, 1, 2, 2, 3, 3, 3]))
