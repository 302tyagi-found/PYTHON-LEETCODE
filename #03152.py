# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#
# You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that
# subarray
#  nums[fromi..toi] is special or not.
#
# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
#
#
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        # Step 1: Compute the "special" array
        special = [0] * (n - 1)
        for i in range(n - 1):
            special[i] = (nums[i] % 2) != (nums[i + 1] % 2)

        # Step 2: Compute prefix sum of "non-special" counts
        prefix_count = [0] * n
        for i in range(1, n):
            prefix_count[i] = prefix_count[i - 1] + (0 if i > len(special) or special[i - 1] else 1)

        # Step 3: Process the queries
        result = []
        for fromi, toi in queries:
            if toi == fromi:  # A single element is always special
                result.append(True)
            else:
                # Check if there are any `False` in the subarray of `special`
                if prefix_count[toi] - prefix_count[fromi] == 0:
                    result.append(True)
                else:
                    result.append(False)

        return result