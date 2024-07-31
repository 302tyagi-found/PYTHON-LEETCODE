# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple
# values have the same frequency, sort them in decreasing order.
#
# Return the sorted array.
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        sorted_array = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_items = sorted(freq.items(), key=lambda x: (x[1], -x[0]))
        for values, count in sorted_items:
            sorted_array.extend([values] * count)

        return sorted_array