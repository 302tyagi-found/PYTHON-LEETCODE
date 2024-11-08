# You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:
#
# Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
# Remove the last element from the current array nums.
# Return an array answer, where answer[i] is the answer to the ith query.
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the maximum possible value for the given number of bits
        max_value = (1 << maximumBit) - 1  # Equivalent to 2^maximumBit - 1

        # Calculate the cumulative XOR of all elements in nums
        cumulative_xor = 0
        for num in nums:
            cumulative_xor ^= num

        # Prepare the result array to hold the answer for each query
        result = []

        # Process each query in reverse (removing the last element each time)
        for num in reversed(nums):
            # Find k by XORing cumulative_xor with max_value
            result.append(cumulative_xor ^ max_value)

            # Update cumulative_xor by removing the effect of the last element
            cumulative_xor ^= num

        return result