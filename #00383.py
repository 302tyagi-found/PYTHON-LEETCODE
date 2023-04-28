# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count ={}
        for char in magazine:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        for char in ransomNote:
            if char not in char_count or char_count[char] ==0:
                return False
            else:
                char_count[char] -= 1
        return True
