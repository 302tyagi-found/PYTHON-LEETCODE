# Given a string s, return the maximum number of unique substrings that the given string can be split into.
#
# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
#
# A substring is a contiguous sequence of characters within a string.


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Helper function for backtracking
        def backtrack(start, unique_substrings):
            # If we have reached the end of the string, return the count of unique substrings
            if start == len(s):
                return len(unique_substrings)

            max_count = 0
            # Try all possible splits starting from 'start'
            for end in range(start + 1, len(s) + 1):
                # Current substring
                substring = s[start:end]
                if substring not in unique_substrings:
                    # Add the substring to the set and backtrack
                    unique_substrings.add(substring)
                    max_count = max(max_count, backtrack(end, unique_substrings))
                    # Backtrack by removing the last added substring
                    unique_substrings.remove(substring)

            return max_count

        # Call the backtracking function
        return backtrack(0, set())