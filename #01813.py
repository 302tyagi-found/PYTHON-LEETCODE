# You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a
# list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only
# uppercase and lowercase English characters.
# Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty)
# inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be
# separated from existing words by spaces.

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Ensure words1 is the longer sentence
        if len(words1) < len(words2):
            words1, words2 = words2, words1

        # Now words1 is always the longer sentence or equal in length to words2
        i, j = 0, 0

        # Check for matching prefix
        while i < len(words2) and words1[i] == words2[i]:
            i += 1

        # Check for matching suffix
        while j < len(words2) and words1[len(words1) - 1 - j] == words2[len(words2) - 1 - j]:
            j += 1

        # If i + j covers all of words2, it's a valid match
        return i + j >= len(words2)