# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
#
# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.
#
#
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Initialize a list to store the resulting characters.
        result = []

        # Pointer to iterate over the spaces array.
        space_index = 0

        # Traverse the string.
        for i, char in enumerate(s):
            # If the current index matches a space index, add a space.
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')
                space_index += 1

            # Add the current character to the result.
            result.append(char)

        # Join the result list into a single string and return it.
        return ''.join(result)