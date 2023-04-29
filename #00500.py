# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American
# keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        output = []
        for word in words:
            chars = set(word.lower())
            if len(word) == 1:
                output.append(word)
            elif chars.issubset(rows[0]):
                output.append(word)
            elif chars.issubset(rows[1]):
                output.append(word)
            elif chars.issubset(rows[2]):
                output.append(word)

        return output
