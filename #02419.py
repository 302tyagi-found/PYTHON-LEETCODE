# You are given an integer array nums of size n.
#
# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
#
# In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
# Return the length of the longest such subarray.
#
# The bitwise AND of an array is the bitwise AND of all the numbers in it.
#
# A subarray is a contiguous sequence of elements within an array.
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)

        # Step 2: Find the longest subarray where all elements have AND equal to max_val
        longest = 0
        current_length = 0

        for num in nums:
            if num == max_val:
                # Continue counting the length of this subarray
                current_length += 1
                longest = max(longest, current_length)
            else:
                # Reset the length when we encounter a different value
                current_length = 0

        return longest
