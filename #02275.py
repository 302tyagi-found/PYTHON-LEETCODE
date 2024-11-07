# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
#
# For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
# Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.
#
# Return the size of the largest combination of candidates with a bitwise AND greater than 0.
#
#
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # We only need 24 bits because max(candidates) <= 10^7, which is < 2^24
        bit_counts = [0] * 24

        # Count the number of times each bit position is set to 1 across all numbers
        for number in candidates:
            for i in range(24):
                if number & (1 << i):  # Check if the i-th bit is set
                    bit_counts[i] += 1

        # The result is the maximum count found in any bit position
        return max(bit_counts)