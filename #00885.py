# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row
# and column in the grid, and the southeast corner is at the last row and column.
#
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's
# boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all
# rows * cols spaces of the grid.
#
# Return an array of coordinates representing the positions of the grid in the order you visited them.
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        result = []
        r, c = rStart, cStart
        direction_index = 0
        steps = 1

        result.append([r, c])

        while len(result) < rows * cols:
            for _ in range(2):  # We need to walk `steps` times in two directions before increasing steps
                for _ in range(steps):
                    r += directions[direction_index][0]
                    c += directions[direction_index][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    if len(result) == rows * cols:
                        return result
                direction_index = (direction_index + 1) % 4
            steps += 1  # Increase the step count after two directions have been walked

        return result
