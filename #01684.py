# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
# if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        # Counter for consistent strings
        consistent_count = 0

        # Check each word in the words array
        for word in words:
            # If all characters in the word are in allowed_set, it's consistent
            if all(char in allowed_set for char in word):
                consistent_count += 1

        return consistent_count
