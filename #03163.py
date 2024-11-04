# Given a string word, compress it using the following algorithm:
#
# Begin with an empty string comp. While word is not empty, use the following operation:
# Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)

        while i < n:
            # Get the current character
            char = word[i]
            # Count the number of consecutive chars up to 9
            count = 0
            while i < n and word[i] == char and count < 9:
                count += 1
                i += 1
            # Append the count and character to the result string
            comp += str(count) + char

        return comp