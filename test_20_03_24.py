# Hi, here's your problem today. This problem was recently asked by Uber:
#
# Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses
# in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate
# this using strings.
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.
#
# Example:
# Input: "((()))"
# Output: True
#
# Input: "[()]{}"
# Output: True
#
# Input: "({[)]"
# Output: False

import unittest
from hamcrest import assert_that, equal_to


class Solution:

    @staticmethod
    def is_valid(s):
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif c is brackets[stack[len(stack) - 1]]:
                stack = stack[:-1]
            else:
                return False
        return len(stack) is 0


class Test(unittest.TestCase):

    def test(self):
        s = "()(){(())"
        # should return False
        assert_that(Solution().is_valid(s), equal_to(False))

        s = ""
        # should return True
        assert_that(Solution().is_valid(s), equal_to(True))

        s = "([{}])()"
        # should return True
        assert_that(Solution().is_valid(s), equal_to(True))