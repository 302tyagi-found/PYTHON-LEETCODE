//There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

//Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
//Paste: You can paste the characters which are copied last time.
//Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

    # Initialize dp array where dp[i] will be the minimum operations for i A's
        dp = [float('inf')] * (n + 1)
        dp[1] = 0  # 0 operations to get 1 A

        # Loop over each number from 2 to n
        for i in range(2, n + 1):
            # Find all factors of i
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    # j is a factor
                    dp[i] = min(dp[i], dp[j] + (i // j))
                    # i // j is also a factor if it's different
                    if j != i // j:
                        dp[i] = min(dp[i], dp[i // j] + j)

        return dp[n]