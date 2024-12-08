# You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:
#
# The chosen integers have to be in the range [1, n].
# Each integer can be chosen at most once.
# The chosen integers should not be in the array banned.
# The sum of the chosen integers should not exceed maxSum.
# Return the maximum number of integers you can choose following the mentioned rules.
#
#

class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        # Create a set of banned numbers for O(1) lookup
        banned_set = set(banned)

        # Initialize the sum and count of chosen numbers
        current_sum = 0
        count = 0

        # Iterate through numbers from 1 to n
        for num in range(1, n + 1):
            # Skip if the number is banned or if adding it would exceed maxSum
            if num in banned_set or current_sum + num > maxSum:
                continue

            # Otherwise, include this number
            current_sum += num
            count += 1

        return count