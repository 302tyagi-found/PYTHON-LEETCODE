# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
# A subarray is defined as a contiguous block of elements in the array.
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p

        if target == 0:
            return 0

        # Dictionary to store the latest index where a particular prefix sum % p occurs
        prefix_mod = {0: -1}
        prefix_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p

            # Find the required prefix sum that would make the sum of remaining divisible by p
            required = (prefix_sum - target) % p

            if required in prefix_mod:
                min_len = min(min_len, i - prefix_mod[required])

            # Update the latest index of the current prefix_sum % p
            prefix_mod[prefix_sum] = i

        # If min_len is still len(nums), it means no valid subarray was found
        return min_len if min_len < len(nums) else -1
