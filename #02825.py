# You are given two 0-indexed strings str1 and str2.
#
# In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.
#
# Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.
#
# Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.
#
#

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0  # Pointers for str1 and str2

        while i < len(str1) and j < len(str2):
            # Check if current character matches or if incrementing matches
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1  # Move to the next character in str2 if matched
            i += 1  # Always move to the next character in str1

        # If we have matched all characters of str2, return True
        return j == len(str2)