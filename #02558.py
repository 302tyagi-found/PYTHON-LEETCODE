# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
#
# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.
# Return the number of gifts remaining after k seconds.
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            # Find the index of the pile with the maximum number of gifts
            max_index = gifts.index(max(gifts))

            # Replace the pile with the floor of the square root of its current value
            gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))

        # Return the sum of all remaining gifts
        return sum(gifts)