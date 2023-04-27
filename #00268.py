# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums_dict = {}
        for i in range(n):
            nums_dict[nums[i]] = 1
            for i in range(0, n+1):
                if i not in nums:
                    return i