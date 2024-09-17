# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split(' ')
        s2_words = s2.split(' ')
        uncommon_words = []
        for word in s1_words:
            if word not in s2_words:
                if s1_words.count(word) == 1:
                    uncommon_words.append(word)

        for word in s2_words:
            if word not in s1_words and word not in uncommon_words:
                if s2_words.count(word) == 1:
                    uncommon_words.append(word)

        return uncommon_words