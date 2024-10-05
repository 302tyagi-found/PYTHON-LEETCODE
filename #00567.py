# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False

        # Frequency count of s1
        s1_count = [0] * 26
        # Frequency count of the current window in s2
        window_count = [0] * 26

        # Initialize the frequency counts for s1 and the first window in s2
        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # Check if the first window is a permutation
        if s1_count == window_count:
            return True

        # Slide the window over the rest of s2
        for i in range(n, m):
            # Remove the character that goes out of the window
            window_count[ord(s2[i - n]) - ord('a')] -= 1
            # Add the new character in the window
            window_count[ord(s2[i]) - ord('a')] += 1

            # Check if the current window matches s1's character frequency
            if s1_count == window_count:
                return True

        return False