# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            if current * 10 <= n:
                current *= 10
            else:
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                current += 1

        return result
