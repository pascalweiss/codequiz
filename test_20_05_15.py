# Hi, here's your problem today. This problem was recently asked by Google:
# You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be
# overlapping. Return the number of rooms that are required.


import unittest
from hamcrest import assert_that, equal_to


class Event:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end


def shouldAddToRoom(room, event: Event):
    for ev in room:
        if   event.end > ev.begin and event.begin < ev.begin:
            return False
        elif event.begin < ev.end and event.end > ev.begin:
            return False
    return True

def eventuallyAddToRooms(rooms, event):
    for room in rooms:
        if shouldAddToRoom(room, event):
            room.append(event)
            return True
    return False

def getNoRooms(events):
    if len(events) is 0: return 0
    rooms= [[events[0]]]
    events = events[1:]
    for event in events:
        added = eventuallyAddToRooms(rooms, event)
        if not added:
            rooms.append([event])
    return len(rooms)


class Test(unittest.TestCase):
    room1 = [Event(60, 150), Event(250, 300)]

    def testAddRoom1(self):
        assert_that(shouldAddToRoom(self.room1, Event(10, 20)), equal_to(True))

    def testAddRoom2(self):
        assert_that(shouldAddToRoom(self.room1, Event(50, 70)), equal_to(False))

    def testAddRoom3(self):
        assert_that(shouldAddToRoom(self.room1, Event(310, 350)), equal_to(True))

    def testAddRoom4(self):
        assert_that(shouldAddToRoom(self.room1, Event(140, 200)), equal_to(False))

    def testAddRoom5(self):
        assert_that(shouldAddToRoom(self.room1, Event(50, 160)), equal_to(False))

    def testAddRoom6(self):
        assert_that(shouldAddToRoom(self.room1, Event(0, 1000)), equal_to(False))

    def testGetNoRooms1(self):
        assert_that(getNoRooms([]), equal_to(0))

    def testGetNoRooms2(self):
        assert_that(getNoRooms([Event(0,1)]), equal_to(1))

    def testGetNoRooms3(self):
        assert_that(getNoRooms([Event(0, 1), Event(2,3)]), equal_to(1))

    def testGetNoRooms4(self):
        assert_that(getNoRooms([Event(30, 75), Event(0, 50), Event(60, 150)]), equal_to(2))

