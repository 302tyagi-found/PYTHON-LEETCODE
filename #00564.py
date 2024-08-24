# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
#
# The closest is defined as the absolute difference minimized between two integers.

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)

        # The case when n is '1', the closest palindrome is '0'.
        if num == 1:
            return "0"

        # List to store all possible candidates.
        candidates = []

        # 1. Generate palindrome by reflecting the first half
        prefix = n[:(length + 1) // 2]  # Get the prefix that will be reflected
        prefix_num = int(prefix)

        # Generate three main cases by decrementing, keeping the same, or incrementing the prefix.
        for diff in [-1, 0, 1]:
            new_prefix = str(prefix_num + diff)
            # Generate the palindrome
            if length % 2 == 0:
                palindrome = new_prefix + new_prefix[::-1]
            else:
                palindrome = new_prefix + new_prefix[:-1][::-1]
            candidates.append(int(palindrome))

        # 2. Edge cases with different number of digits
        candidates.append(10 ** (length - 1) - 1)  # One less digit (e.g., 999 -> 1001)
        candidates.append(10 ** length + 1)  # One more digit (e.g., 999 -> 1001)

        # Remove the original number itself from the candidates
        candidates = [c for c in candidates if c != num]

        # Find the closest palindrome by absolute difference
        closest = min(candidates, key=lambda x: (abs(x - num), x))

        return str(closest)