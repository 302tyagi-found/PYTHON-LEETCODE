# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        values = 0
        for i in range(0, k):
            values += nums[i]
        max_av_values = values
        for end in range(k, len(nums)):
            values += nums[end] - nums[end - k]
            max_av_values = max(max_av_values, values)
        return max_av_values / k
