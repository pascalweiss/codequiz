# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

import unittest
from hamcrest import assert_that, equal_to


class Cons:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def to_str(self):
        return "{}->{}".format(self.begin, self.end)


def trans_f(l):
    return [c.to_str() for c in l]


def cons(l):
    if len(l) is 0:
        return []
    i = l[0]
    c = Cons(i, i)
    l = l[1:]
    result = []
    for n in l:
        if n is c.end:
            pass
        else:
            i += 1
            if i is n:
                c.end = i
            if i is not n:
                i = n
                result.append(c)
                c = Cons(i, i)
    result.append(c)
    return trans_f(result)


class Test(unittest.TestCase):

    def testEmpty(self):
        assert_that(trans_f([]), equal_to([]))

    def testTransf(self):
        assert_that(trans_f([Cons(1, 3)]), equal_to(["1->3"]))

    def testCons(self):
        assert_that(cons([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]), equal_to(["0->2", "5->5", "7->11", "15->15"]))
