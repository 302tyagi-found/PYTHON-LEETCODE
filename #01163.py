//Given a string s, return the last substring of s in lexicographical order.

class Solution:
    def lastSubstring(self, s: str) -> str:
        # Initialize the maximum suffix as an empty string
        max_suffix = ""
        # Traverse the string from right to left
        for i in range(len(s) - 1, -1, -1):
            # Get the current suffix starting at index i
            current_suffix = s[i:]
            # Update the maximum suffix if the current one is larger
            if current_suffix > max_suffix:
                max_suffix = current_suffix
        return max_suffix