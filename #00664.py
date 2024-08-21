//There is a strange printer with the following two special properties:

//The printer can only print a sequence of the same character each time.
//At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
//Given a string s, return the minimum number of turns the printer needed to print it.

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]

        # Base case: single character substrings
        for i in range(n):
            dp[i][i] = 1

        # Fill the DP table
        for length in range(2, n + 1):  # length ranges from 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                # Initial case: split at every possible point
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                
                # Optimize by checking if the entire segment can be covered
                # in fewer turns if there's a way to merge segments
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] - 1)

        return dp[0][n - 1]