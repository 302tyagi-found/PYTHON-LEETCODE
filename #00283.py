# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        initial = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[initial] = nums[initial], nums[i]
                initial += 1
        return nums
