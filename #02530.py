# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
#
# In one operation:
#
# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.
#
# The ceiling function ceil(val) is the least integer greater than or equal to val.
#
#

import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0

        # Step 2: Perform k operations
        for _ in range(k):
            # Step 2.1: Pop the largest element (note it's negative, so take -ve)
            max_element = -heapq.heappop(max_heap)
            score += max_element

            # Step 2.2: Compute ceil(max_element / 3) and push it back
            new_value = math.ceil(max_element / 3)
            heapq.heappush(max_heap, -new_value)

        # Step 3: Return the total score
        return score
