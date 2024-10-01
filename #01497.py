# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k

        # Count the remainders when dividing by k
        for num in arr:
            remainder = num % k
            # Make sure remainder is positive
            remainder_count[remainder] += 1

        # Check the special case of remainder 0, it must have an even count
        if remainder_count[0] % 2 != 0:
            return False

        # Check the rest of the remainders
        for i in range(1, k // 2 + 1):
            if i == k - i:  # Special case for remainder k/2 when k is even
                if remainder_count[i] % 2 != 0:
                    return False
            else:
                if remainder_count[i] != remainder_count[k - i]:
                    return False

        return True