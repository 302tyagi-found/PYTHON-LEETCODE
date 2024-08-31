# You are given an integer array nums.
#
# In one move, you can choose one element of nums and change it to any value.
#
# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0  # If there are 4 or fewer elements, all can be equalized

        nums.sort()

        # We can perform at most 3 moves
        return min(
            nums[-1] - nums[3],  # Change three smallest elements
            nums[-2] - nums[2],  # Change two smallest and one largest
            nums[-3] - nums[1],  # Change one smallest and two largest
            nums[-4] - nums[0]  # Change three largest elements
        )