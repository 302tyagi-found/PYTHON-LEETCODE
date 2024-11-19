# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
#
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        window_set = set()
        start = 0

        for end in range(len(nums)):
            # Add the current element to the window
            while nums[end] in window_set or end - start + 1 > k:
                # If duplicate or window too big, shrink it
                window_set.remove(nums[start])
                current_sum -= nums[start]
                start += 1

            # Add the current element
            window_set.add(nums[end])
            current_sum += nums[end]

            # Check if the window is valid and update max_sum
            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)

        return max_sum