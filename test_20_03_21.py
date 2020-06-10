# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Here is the function signature as a starting point (in Python):
# Definition for singly-linked list.

import unittest

from hamcrest import assert_that, equal_to


class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:

  def __init__(self):
    pass

  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    if l1 is not None and l2 is not None:
      valsum = l1.val + l2.val + c
      lnew = ListNode(valsum % 10)
      lnew.next = self.addTwoNumbers(l1.next, l2.next, valsum >= 10)
      return lnew
    else:
      return None


class Test(unittest.TestCase):
  def test(self):
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)

    assert_that(result.val, equal_to(7))
    assert_that(result.next.val, equal_to(0))
    assert_that(result.next.next.val, equal_to(8))
    assert_that(result.next.next.next, equal_to(None))


if __name__ == '__main__':
  unittest.main()

# 7 0 8