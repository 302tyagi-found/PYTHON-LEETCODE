# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:
#
# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.
#
#

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove '_' characters and check if the relative order of 'L' and 'R' is the same
        if start.replace('_', '') != target.replace('_', ''):
            return False

        # Check the relative positions of 'L' and 'R'
        start_L_positions = []
        start_R_positions = []
        target_L_positions = []
        target_R_positions = []

        for i in range(len(start)):
            if start[i] == 'L':
                start_L_positions.append(i)
            elif start[i] == 'R':
                start_R_positions.append(i)
            if target[i] == 'L':
                target_L_positions.append(i)
            elif target[i] == 'R':
                target_R_positions.append(i)

        # Check L positions (should only move to the left)
        for s_pos, t_pos in zip(start_L_positions, target_L_positions):
            if s_pos < t_pos:
                return False

        # Check R positions (should only move to the right)
        for s_pos, t_pos in zip(start_R_positions, target_R_positions):
            if s_pos > t_pos:
                return False

        return True