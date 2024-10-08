# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
#
# A string is called balanced if and only if:
#
# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
# You may swap the brackets at any two indices any number of times.
#
# Return the minimum number of swaps to make s balanced.
#
#

class Solution:
    def minSwaps(self, s: str) -> int:
        # Count of unbalanced closing brackets
        unbalanced = 0
        # Max unbalanced closing brackets at any point
        max_unbalanced = 0

        # Traverse the string to find imbalance
        for char in s:
            if char == '[':
                # A matching opening bracket reduces imbalance
                unbalanced -= 1
            else:
                # A closing bracket increases imbalance
                unbalanced += 1

            # We cannot have negative unbalance (i.e., more openings at any point),
            # so we track the maximum number of unmatched closing brackets
            max_unbalanced = max(max_unbalanced, unbalanced)

        # Minimum swaps needed is half the maximum unbalance encountered
        # Because each swap fixes two unmatched brackets (one opening, one closing)
        return (max_unbalanced + 1) // 2
