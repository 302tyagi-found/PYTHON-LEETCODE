# Given a string s consisting of words and spaces, return the length of the last word in the string.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0
        for i in s[::-1]:
            if i != ' ':
                count += 1
            elif i == ' ' and count == 0:
                continue
            else:
                break
        return count
