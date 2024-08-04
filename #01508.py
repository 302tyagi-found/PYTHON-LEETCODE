# You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous
# subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers
#
# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the
# answer can be a huge number return it modulo 109 + 7.
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7

        subarray_sums = []

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray_sums.append(prefix[j] - prefix[i])

        subarray_sums.sort()

        result = sum(subarray_sums[left - 1:right]) % MOD

        return result
