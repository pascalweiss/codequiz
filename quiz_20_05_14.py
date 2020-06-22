# Hi, here's your problem today. This problem was recently asked by Google:
# You are given a stream of numbers. Compute the median for each new element .
# Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
# Here's a starting point:
import math
import unittest
from hamcrest import assert_that, equal_to


def median(l):
    l.sort()
    n = len(l)
    if n % 2 is 0:
        i = int(n / 2) - 1
        return (l[i] + l[i+1]) / 2
    else:
        return l[math.floor(n/2)]


def running_median(stream):
    result = []
    l = []
    for el in stream:
        l.append(el)
        result.append(median(l))
    return result


class Test(unittest.TestCase):

    def test_median(self):
        assert_that(median([2, 3, 6]), equal_to(3))
        assert_that(median([2,3,5,7]), equal_to(4.0))

    def test(self):
        assert_that(running_median([2, 1, 4, 7, 2, 0, 5]), equal_to([2, 1.5, 2, 3.0, 2, 2.0, 2]))
