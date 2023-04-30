# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
# A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        count = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                count += i + num // i
        if num == count:
            return True
        else:
            return False
