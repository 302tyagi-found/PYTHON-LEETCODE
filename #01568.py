# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
#
# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
#
# In one day, we are allowed to change any single land cell (1) into a water cell (0).
#
# Return the minimum number of days to disconnect the grid.



from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def is_connected(grid):
            visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

            def dfs(x, y):
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == 0:
                    return
                visited[x][y] = True
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    dfs(x + dx, y + dy)

            island_count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and not visited[i][j]:
                        if island_count == 1:
                            return False  # Already found an island, so more than one is present
                        dfs(i, j)
                        island_count += 1

            return island_count == 1

        if not is_connected(grid):
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected(grid):
                        return 1
                    grid[i][j] = 1

        return 2