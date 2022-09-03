# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: list[str], t: list[str]) -> bool:
        val = []
        if len(s) != len(t):
            return False
        for i in s:
            for j in t:
                if i == j:
                    if s.count(i) != t.count(j):
                        return False
                    else:
                        val.append(i)
                        break
        if len(val) == len(s):
            return True
        else:
            return False
