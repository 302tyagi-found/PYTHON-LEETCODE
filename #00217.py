# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        length = len(nums)
        j = 0
        i = j - 1
        nums.sort()
        if length <= 1:
            return False
        for j in nums:
            if j == nums[i]:
                return True
            i += 1
        return False
