# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        # Step 1: Convert all time points to minutes
        minutes_list = sorted(timeToMinutes(time) for time in timePoints)

        # Step 2: Initialize the minimum difference to be large
        min_diff = float('inf')

        # Step 3: Compute the difference between consecutive time points
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])

        # Step 4: Compute the circular difference between the last and the first time point
        # Wrap-around case (24 hours = 1440 minutes)
        min_diff = min(min_diff, 1440 - (minutes_list[-1] - minutes_list[0]))

        return min_diff