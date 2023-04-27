# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= nums[i] ^ i
        return missing

        # or
        
        n = len(nums)
        m = sum(nums)
        return (n*(n+1))//2 - m
