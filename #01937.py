# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
#
# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
#
# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
#
# Return the maximum number of points you can achieve.
#
# abs(x) is defined as:
#
# x for x >= 0.
# -x for x < 0.
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for r in range(1, m):
            left_dp = [0] * n
            right_dp = [0] * n

            # Compute the best score considering left to right (forward pass)
            left_dp[0] = dp[0]
            for c in range(1, n):
                left_dp[c] = max(left_dp[c-1] - 1, dp[c])

            # Compute the best score considering right to left (backward pass)
            right_dp[-1] = dp[-1]
            for c in range(n-2, -1, -1):
                right_dp[c] = max(right_dp[c+1] - 1, dp[c])

            # Update dp for the current row
            for c in range(n):
                dp[c] = points[r][c] + max(left_dp[c], right_dp[c])

        return max(dp)