# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
#
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
#
# Return the number of islands in grid2 that are considered sub-islands.
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            grid[x][y] = 0  # Mark this cell as visited
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(grid, x + dx, y + dy)

        def is_sub_island(x, y):
            stack = [(x, y)]
            is_sub = True
            while stack:
                cx, cy = stack.pop()
                if grid2[cx][cy] == 0:
                    continue
                if grid1[cx][cy] == 0:
                    is_sub = False
                grid2[cx][cy] = 0  # Mark as visited
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(grid2) and 0 <= ny < len(grid2[0]) and grid2[nx][ny] == 1:
                        stack.append((nx, ny))
            return is_sub

        sub_islands_count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:  # Found an island part in grid2
                    if is_sub_island(i, j):  # Check if it's a sub-island
                        sub_islands_count += 1

        return sub_islands_count
