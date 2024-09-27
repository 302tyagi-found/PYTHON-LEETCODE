# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.
# A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).
# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
# Implement the MyCalendarTwo class:
# MyCalendarTwo() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.


class MyCalendarTwo:

    def __init__(self):
        self.bookings = []  # This stores all single bookings
        self.overlaps = []  # This stores all double bookings (i.e., overlaps between two events)

    def book(self, start: int, end: int) -> bool:
        # Step 1: Check if the new event would cause a triple booking
        for s, e in self.overlaps:
            if start < e and end > s:  # Check if the new event overlaps with a double booking
                return False

        # Step 2: Check for overlaps with single bookings to record new double bookings
        for s, e in self.bookings:
            if start < e and end > s:  # If there's an overlap, record it as a double booking
                self.overlaps.append((max(start, s), min(end, e)))

        # Step 3: If no triple booking, add the new event to single bookings
        self.bookings.append((start, end))
        return True