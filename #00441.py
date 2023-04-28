# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row
# has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
class Solution:
    def arrangeCoins(self, n: int) -> int:
        remaining = n
        row_count = 0
        while row_count < remaining:
            row_count += 1
            remaining -= row_count
        return row_count
