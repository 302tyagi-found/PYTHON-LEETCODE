# You are given an integer array nums, an integer k, and an integer multiplier.
#
# You need to perform k operations on nums. In each operation:
#
# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.
#
#

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            # Find the index of the minimum value. If there are multiple, pick the first one.
            min_index = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[min_index]:
                    min_index = i

            # Update the minimum value by multiplying it with the multiplier
            nums[min_index] *= multiplier

        return nums