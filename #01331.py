# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
#
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(set(arr))

        # Step 2: Create a mapping from element to rank
        rank_map = {value: rank + 1 for rank, value in enumerate(unique_sorted)}

        # Step 3: Replace each element with its rank
        return [rank_map[num] for num in arr]