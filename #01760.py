# You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.
#
# You can perform the following operation at most maxOperations times:
#
# Take any bag of balls and divide it into two new bags with a positive number of balls.
# For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
# Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.
#
# Return the minimum possible penalty after performing the operations.
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Helper function to determine if a penalty is feasible
        def canAchievePenalty(penalty):
            operations = 0
            for balls in nums:
                # Count how many splits are required to make balls <= penalty
                if balls > penalty:
                    operations += (balls - 1) // penalty
            return operations <= maxOperations

        # Binary search for the minimum penalty
        left, right = 1, max(nums)  # Penalty can range from 1 to max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid  # Try for a smaller penalty
            else:
                left = mid + 1  # Increase the penalty
        return left