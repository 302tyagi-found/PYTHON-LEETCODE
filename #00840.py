# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
#
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
#
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(r: int, c: int) -> bool:
            # Check if all values in the 3x3 grid are between 1 and 9
            values = set()
            for i in range(3):
                for j in range(3):
                    if grid[r + i][c + j] < 1 or grid[r + i][c + j] > 9:
                        return False
                    values.add(grid[r + i][c + j])

            if len(values) != 9:
                return False

            # Check the sum of rows, columns, and diagonals
            row1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
            row2 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2]
            row3 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]

            col1 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c]
            col2 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1]
            col3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]

            diag1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]
            diag2 = grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]

            return row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2 == 15

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                if isMagic(r, c):
                    count += 1

        return count
