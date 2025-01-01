# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
#
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
#
# Return the largest number of chunks we can make to sort the array.
#
#
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize variables
        max_seen = 0
        chunks = 0

        # Iterate through the array
        for i, num in enumerate(arr):
            # Update the maximum value seen so far
            max_seen = max(max_seen, num)

            # If the maximum value seen so far equals the current index,
            # it means we can form a chunk up to this point.
            if max_seen == i:
                chunks += 1

        return chunks