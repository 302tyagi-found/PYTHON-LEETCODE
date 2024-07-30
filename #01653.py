# You are given a string s consisting only of characters 'a' and 'b',
#
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j)
# such that i < j and s[i] = 'b' and s[j]= 'a'.
#
# Return the minimum number of deletions needed to make s balanced.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        min_deletions = 0

        for char in s:
            if char == 'b':
                b_count += 1
            else:  # char == 'a'
                min_deletions = min(min_deletions + 1, b_count)

        return min_deletions
