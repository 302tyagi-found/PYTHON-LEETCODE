# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Implement KthLargest class:
#
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
#

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        # Build the min-heap with at most k elements
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new value to the min-heap
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The root of the min-heap is the kth largest element
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)