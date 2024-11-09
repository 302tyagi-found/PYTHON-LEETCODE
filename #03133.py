# You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.
#
# Return the minimum possible value of nums[n - 1].

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        X = x
        N = n - 1
        ans = 0
        j = 0

        for i in range(56):  # Limit to 56 bits, as in the original C++ code
            if (X >> i) & 1:  # Check if the i-th bit in X is set
                ans |= (1 << i)  # Set the i-th bit in ans to 1
            else:
                if (N >> j) & 1:  # Use bits from N sequentially
                    ans |= (1 << i)  # Set the i-th bit in ans according to N
                j += 1  # Move to the next bit in N only if X[i] was not set

        return ans