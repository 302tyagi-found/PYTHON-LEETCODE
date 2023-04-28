# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
class Solution:
    def reverseVowels(self, s: str) -> str:
        characters = list(s)
        first = 0
        last = len(characters) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while first < last:
            if characters[first] not in vowels:
                first += 1
                continue
            if characters[last] not in vowels:
                last -= 1
                continue
            characters[first], characters[last] = characters[last], characters[first]
            first += 1
            last -= 1
        return "".join(characters)