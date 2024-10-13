# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')

        # Fill the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list_index, element_index)
            current_max = max(current_max, nums[i][0])  # Track the current max element in the heap

        # Initialize the result range
        best_range = [-1e9, 1e9]

        while min_heap:
            # Pop the smallest element from the heap
            current_min, list_index, element_index = heapq.heappop(min_heap)

            # Update the result range if the current range is smaller
            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]

            # If we have reached the end of one of the lists, stop
            if element_index + 1 == len(nums[list_index]):
                break

            # Push the next element from the same list into the heap
            next_value = nums[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

            # Update the current maximum value
            current_max = max(current_max, next_value)

        return best_range
