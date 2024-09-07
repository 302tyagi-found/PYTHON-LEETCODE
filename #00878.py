// A positive integer is magical if it is divisible by either a or b.

// Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.


import math

MOD = 10**9 + 7

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def countMagicalNumbers(x: int, a: int, b: int) -> int:
            lcm_ab = (a * b) // math.gcd(a, b)
            return (x // a) + (x // b) - (x // lcm_ab)
        
        # Binary search for the nth magical number
        left, right = min(a, b), n * min(a, b)
        
        while left < right:
            mid = (left + right) // 2
            if countMagicalNumbers(mid, a, b) < n:
                left = mid + 1
            else:
                right = mid
        
        return left % MOD
