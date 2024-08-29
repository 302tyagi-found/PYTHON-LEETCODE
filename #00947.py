# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
#
# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
#
# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x):
            visited.add(x)
            for y in graph[x]:
                if y not in visited:
                    dfs(y)

        # Create a graph with nodes as indices of stones
        graph = defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j in range(i + 1, len(stones)):
                x2, y2 = stones[j]
                # Connect nodes if they are in the same row or column
                if x1 == x2 or y1 == y2:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        num_components = 0

        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                num_components += 1

        # The number of stones that can be removed is the total number of stones minus the number of components
        return len(stones) - num_components
