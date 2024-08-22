# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
#
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
#
#
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num_counts = {}
        for i in range(len(nums)):
            if nums[i] in num_counts:
                num_counts[nums[i]] += 1
            else:
                num_counts[nums[i]] = 1
        res = []
        for j in num_counts:
            if num_counts[j] == 1:
                res.append(j)
        return res