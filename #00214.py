# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.
from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def computeLPSArray(pattern: str) -> List[int]:
            n = len(pattern)
            lps = [0] * n
            length = 0  # length of the previous longest prefix suffix
            i = 1  # lps[0] is always 0, so start from i = 1

            while i < n:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        if not s:
            return s

        # Create the temporary string to apply KMP algorithm
        temp = s + '#' + s[::-1]

        # Compute the lps array for the temp string
        lps = computeLPSArray(temp)

        # The last value of lps gives us the longest palindromic prefix
        longest_palindromic_prefix_length = lps[-1]

        # Add the remaining characters (that are not part of the palindromic prefix) in reverse order
        return s[longest_palindromic_prefix_length:][::-1] + s
