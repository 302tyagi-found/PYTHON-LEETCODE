# Given the string s, return the size of the longest substring containing each vowel an even number of times.
# That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        # Initialize the bitmask to 0 (all vowels even)
        bitmask = 0
        # Dictionary to store the first occurrence of each bitmask
        first_occurrence = {0: -1}
        max_length = 0

        for i, char in enumerate(s):
            if char in vowel_to_bit:
                # Toggle the bit corresponding to the vowel
                bitmask ^= (1 << vowel_to_bit[char])

            # If the bitmask has been seen before, we can form a valid substring
            if bitmask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[bitmask])
            else:
                # Store the first occurrence of this bitmask
                first_occurrence[bitmask] = i

        return max_length
