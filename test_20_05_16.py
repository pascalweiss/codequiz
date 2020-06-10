# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
# whitespace and initial word order.

import unittest
from hamcrest import assert_that, equal_to


def reverse(chars, acc=""):
    if len(chars) is 0:
        return acc
    else:
        return reverse(chars[1:], chars[0]+acc)


def split(s: str):
    result = []
    word = ""
    white = [" ", "\t", "\n"]
    for c in s:
        if c not in white:
            word += c
        else:
            result.append(word)
            word = ""
    result.append(word)
    return result


def algo(s: str):
    return " ".join([reverse(word) for word in split(s)])


class Test(unittest.TestCase):

    def testReverse(self):
        assert_that(reverse(""), equal_to(""))
        assert_that(reverse("ab"), equal_to("ba"))

    def testSplit(self):
        assert_that(split(""), equal_to([""]))
        assert_that(split("ab cde fgh"), equal_to(["ab", "cde", "fgh"]))

    def testAlgo(self):
        assert_that(algo("The cat in the hat"), equal_to("ehT tac ni eht tah"))
