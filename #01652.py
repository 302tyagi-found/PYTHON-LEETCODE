# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
#
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
#
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
#
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        # If k == 0, all elements should be 0
        if k == 0:
            return [0] * n

        # Double the array to simulate circular behavior
        extended_code = code * 2

        # Handle positive and negative k
        if k > 0:
            return [sum(extended_code[i + 1:i + 1 + k]) for i in range(n)]
        else:
            k = abs(k)
            return [sum(extended_code[i + n - k:i + n]) for i in range(n)]