# You are given m arrays, where each array is sorted in ascending order.
#
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
#
# Return the maximum distance.

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            # Calculate the maximum possible distance
            max_distance = max(max_distance, abs(current_max - min_val), abs(max_val - current_min))

            # Update the global minimum and maximum
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance