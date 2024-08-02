# A swap is defined as taking two distinct positions in an array and swapping the values in them.
#
# A circular array is defined as an array where we consider the first element and the last element to be adjacent.
#
# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the
# array together at any location.
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)

        # Edge case: If there are no 1's or all are 1's
        if total_ones == 0 or total_ones == len(nums):
            return 0

        # Step 2: Create an extended array to handle the circular nature
        extended_nums = nums + nums

        # Step 3: Use a sliding window to find the maximum number of 1's in any window of size total_ones
        max_ones_in_window = 0
        current_ones = sum(extended_nums[:total_ones])

        max_ones_in_window = current_ones

        for i in range(total_ones, len(extended_nums)):
            current_ones += extended_nums[i] - extended_nums[i - total_ones]
            max_ones_in_window = max(max_ones_in_window, current_ones)

        # Step 4: Calculate the minimum swaps
        min_swaps = total_ones - max_ones_in_window

        return min_swaps
