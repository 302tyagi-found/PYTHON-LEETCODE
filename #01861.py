# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
#
# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
#
# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
#
# Return an n x m matrix representing the box after the rotation described above.
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        # Process each row to simulate gravity
        for row in box:
            empty_slot = n - 1  # Start from the rightmost column

            for col in range(n - 1, -1, -1):  # Traverse the row from right to left
                if row[col] == '#':  # Stone
                    row[col], row[empty_slot] = row[empty_slot], row[col]
                    empty_slot -= 1
                elif row[col] == '*':  # Obstacle
                    empty_slot = col - 1

        # Rotate the box clockwise
        rotated_box = [[None] * m for _ in range(n)]  # Create a rotated matrix
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]

        return rotated_box