# You are given an array of integers. Return the length of the longest increasing subsequence
# (not necessarily contiguous) in the array.

import unittest
from hamcrest import assert_that, equal_to

class Test(unittest.TestCase):

    def testFinal(self):
        data1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        # since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
        # assert_that(algo(data1), equal_to(6))

