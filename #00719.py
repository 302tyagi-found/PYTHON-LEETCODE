# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
#
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs(nums, mid):
            count = 0
            left = 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        nums.sort()

        # Binary search between 0 and max(nums) - min(nums)
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if count_pairs(nums, mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
