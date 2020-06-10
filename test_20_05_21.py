# Hi, here's your problem today. This problem was recently asked by Microsoft:
# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

import unittest
from hamcrest import equal_to, assert_that


def calc_hour(h, m):
    hour_add = 5.0 / 60 * m * 6
    return hour_add + (h % 12) * 30


def calc_minute(m):
    return m * 6


def calc_angle(h, m):
  deg_hour = calc_hour(h,m)
  deg_minu = calc_minute(m)
  return abs(deg_hour - deg_minu)


class Test(unittest.TestCase):

    def test_hour(self):
        assert_that(calc_hour(0,0), equal_to(0))
        assert_that(calc_hour(0,30), equal_to(6 * 2.5))
        assert_that(calc_hour(6,30), equal_to(180 + 6 * 2.5))

    def test_minute(self):
        assert_that(calc_minute(0), equal_to(0))
        assert_that(calc_minute(30), equal_to(180))
        assert_that(calc_minute(15), equal_to(90))

    def test_1(self):
        assert_that(calc_angle(0, 30), equal_to(180 - 6 * 2.5))

    def testFinal1(self):
        assert_that(calc_angle(3, 30), equal_to(75))

    def testFinal2(self):
        assert_that(calc_angle(12, 30), equal_to(165))
