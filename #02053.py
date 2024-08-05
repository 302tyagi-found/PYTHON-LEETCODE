# A distinct string is a string that is present only once in an array.
#
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer
# than k distinct strings, return an empty string "".
#
# Note that the strings are considered in the order in which they appear in the array.


from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        test = {}
        for word in arr:
            if word in test:
                test[word] = 0
            else:
                test[word] = 1

        distinct_words = []
        for word, count in test.items():
            if count == 1:
                distinct_words.append(word)

        if k <= len(distinct_words):
            return distinct_words[k - 1]
        else:
            return ""
