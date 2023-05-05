# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s_list = list(s)
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s_list[i] in vowels:
                count += 1
        max_count = count
        for end in range(k, len(s)):
            start = end - k + 1
            if s_list[end] in vowels:
                count += 1
            if s_list[start - 1] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count
        # output = []
        # for i in range(len(s)):
        #     for j in range(i, i+k):
        #         if s_list[j] in 'aeiouAEIOU':
        #             count += 1
        #     output.append(count)
        # return max(output)

sol = Solution()
s = "abciiidef"
k = 3
print(sol.maxVowels(s, k))