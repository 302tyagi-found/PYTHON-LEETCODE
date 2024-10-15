# There are n balls on a table, each ball has a color black or white.
#
# You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
#
# In each step, you can choose two adjacent balls and swap them.
#
# Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
#
#

class Solution:
    def minimumSteps(self, s: str) -> int:
        ones_positions = []  # Stores the indices of all '1's

        # Collect the positions of all '1's
        for i, char in enumerate(s):
            if char == '1':
                ones_positions.append(i)

        # Calculate minimum swaps
        min_steps = 0
        total_ones = len(ones_positions)

        # For each '1', calculate how many steps it needs to move to its target
        for i, pos in enumerate(ones_positions):
            target_position = len(s) - total_ones + i  # The target position for this '1'
            min_steps += target_position - pos  # Count how many swaps are needed

        return min_steps