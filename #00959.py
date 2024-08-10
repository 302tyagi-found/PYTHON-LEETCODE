# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
#
# Given the grid grid represented as a string array, return the number of regions.
#
# Note that backslash characters are escaped, so a '\' is represented as '\\'.

from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(len(grid[i])):
                root = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif grid[i][j] == '\\':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)

                # Union with adjacent cells
                if i < n - 1:
                    union(root + 2, root + 4 * n + 0)
                if j < n - 1:
                    union(root + 1, root + 4 + 3)

        return sum(parent[x] == x for x in range(4 * n * n))
