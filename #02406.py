# You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
#
# You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.
#
# Return the minimum number of groups you need to make.
#
# Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
#
#
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []

        # Create events for each interval
        for left, right in intervals:
            events.append((left, 1))  # Start of an interval
            events.append((right + 1, -1))  # End of an interval (right+1 means closing it after right)

        # Sort events by time. If times are the same, we process starting events (+1) before ending events (-1)
        events.sort()

        max_active = 0
        current_active = 0

        # Sweep line to count active intervals
        for time, event in events:
            current_active += event
            max_active = max(max_active, current_active)

        return max_active