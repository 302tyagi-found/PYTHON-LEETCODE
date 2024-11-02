# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#
# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.
#
# A sentence is circular if:
#
# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.
#
# Given a string sentence, return true if it is circular. Otherwise, return false.

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        # Number of words in the sentence
        n = len(words)

        # Check the circular condition
        for i in range(n):
            # Last character of the current word
            last_char = words[i][-1]
            # First character of the next word (wrapping around using modulo)
            first_char_next = words[(i + 1) % n][0]

            # If they don't match, sentence is not circular
            if last_char != first_char_next:
                return False

        # If all pairs satisfy the condition, return True
        return True