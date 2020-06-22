# Hi, here's your problem today. This problem was recently asked by Apple:
# You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value,
# and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
# Write a function that takes this tree and evaluates the expression.
#
# Example:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
#
# This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.
import unittest

from hamcrest import assert_that, equal_to


class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    res_left  = None if root.left  is None else evaluate(root.left)
    res_right = None if root.right is None else evaluate(root.right)
    if   root.val is PLUS:
      return res_left + res_right
    elif root.val is MINUS:
      return res_left - res_right
    elif root.val is TIMES:
      return res_left * res_right
    elif root.val is DIVIDE:
      return res_left / res_right
    else:
      return root.val


class Test(unittest.TestCase):

    def testFinal(self):
        tree = Node(TIMES)
        tree.left = Node(PLUS)
        tree.left.left = Node(3)
        tree.left.right = Node(2)
        tree.right = Node(PLUS)
        tree.right.left = Node(4)
        tree.right.right = Node(5)
        assert_that(evaluate(tree), equal_to(45))

