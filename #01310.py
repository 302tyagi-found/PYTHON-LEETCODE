# You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
#
# For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
#
# Return an array answer where answer[i] is the answer to the ith query.
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)

        # Compute the prefix XORs
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        # Process each query using the prefix XOR array
        result = []
        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])

        return result
