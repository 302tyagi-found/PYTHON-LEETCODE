# You are given an integer array nums. A subsequence of nums is called a square streak if:
#
# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        num_set = set(nums)

        longest_streak = 0

        # Check for square streak starting with each number
        for num in nums:
            streak_length = 0
            current = num

            # Continue as long as we find the square in the set
            while current in num_set:
                streak_length += 1
                current = current * current  # Square the current number

            # Update longest streak if this one is the longest so far
            if streak_length >= 2:
                longest_streak = max(longest_streak, streak_length)

        # If no streak of at least 2 was found, return -1
        return longest_streak if longest_streak >= 2 else -1