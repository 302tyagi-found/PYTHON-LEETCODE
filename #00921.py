# A parentheses string is valid if and only if:
#
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
#
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
#
#


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        close_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            if char == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
        return open_count + close_count


sol = Solution()
s = "()))"
print(sol.minAddToMakeValid(s))
