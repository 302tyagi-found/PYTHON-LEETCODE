# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
# 
# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)

        # Create a stack of potential `i` values in decreasing order of `nums[i]`
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_width = 0

        # Traverse from right to left to find valid `j`
        for j in range(n - 1, -1, -1):
            # While the stack is not empty and nums[i] <= nums[j], calculate width
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width