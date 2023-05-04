# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        output = []
        for i in s_list:
            output.append(''.join(i[::-1]))
        return ' '.join(output)
