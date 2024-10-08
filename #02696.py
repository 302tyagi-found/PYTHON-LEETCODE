# You are given a string s consisting only of uppercase English letters.
#
# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.
#
# Return the minimum possible length of the resulting string that you can obtain.
#
# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if stack:
                # Check if the top of the stack and the current char form "AB" or "CD"
                if (stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D'):
                    stack.pop()  # Remove the matching pair
                else:
                    stack.append(char)  # Otherwise, add the char to the stack
            else:
                stack.append(char)  # If stack is empty, just push the char

        # The size of the stack is the minimum length of the resulting string
        return len(stack)
