# Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where
# i < j and hours[i] + hours[j] forms a complete day.

# A complete day is defined as a time duration that is an exact multiple of 24 hours.

# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for i in range(len(hours)):
            for j in range(i+1, len(hours)):
                if i == j:
                    return count
                if (hours[i] + hours[j]) % 24 == 0:
                    count += 1

        return count
