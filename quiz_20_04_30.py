# Hi, here's your problem today. This problem was recently asked by Google:
# A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is
# obtained by describing the previous term. An example is easier to understand:
# Each consecutive value describes the prior value.

# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.

# Your task is, return the nth term of this sequence.

import unittest
from hamcrest import assert_that, equal_to

def add(l):
    return [len(l), l[0]]

def describe(acc: list):
    res = []
    aux = [acc[0]]
    acc = acc[1:]
    for el in acc:
        if el is not aux[-1]:
            res = res + add(aux)
            aux = [el]
        else:
            aux.append(el)
    return res + add(aux)

def algo(n: int):
    res = [1]
    for _ in range(n):
        res = describe(res)
    return res


class Test(unittest.TestCase):

    def test_describe(self):
        assert_that(describe([2,1]), equal_to([1,2,1,1]))
        assert_that(describe([1, 2, 1, 1]), equal_to([1,1,1,2,2,1]))

    def test1(self):
        assert_that(algo(0), equal_to([1]))
        assert_that(algo(1), equal_to([1,1]))
        assert_that(algo(4), equal_to([1,1,1,2,2,1]))
