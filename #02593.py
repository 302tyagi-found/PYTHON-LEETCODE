# You are given an array nums consisting of positive integers.
#
# Starting with score = 0, apply the following algorithm:
#
# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(nums)):
            if not stk or nums[i] < stk[-1]:
                # maintain a decreasing stack
                stk.append(nums[i])
            else:
                # when the current element is larger we can choose previous element since it's smaller than current and its previous
                while stk:
                    res += stk.pop()
                    if stk:
                        # if there is previous element skip that too
                        stk.pop()
        while stk:
            res += stk.pop()
            if stk:
                stk.pop()

        return res