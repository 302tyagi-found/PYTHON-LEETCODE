# You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more
# non-overlapping substrings such that each substring is present in dictionary.
# There may be some extra characters in s which are not present in any of the substrings.
# Return the minimum number of extra characters left over if you break up s optimally.
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)

        # dp[i] will store the minimum extra characters for the prefix of length i
        dp = [0] * (n + 1)

        # Initialize dp[0] as no characters need to be removed for an empty string
        for i in range(1, n + 1):
            # Initialize dp[i] as if all characters from 0 to i are extra
            dp[i] = dp[i - 1] + 1

            # Check every substring ending at index i - 1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]