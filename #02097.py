# You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.
#
# Return any valid arrangement of pairs.
#
# Note: The inputs will be generated such that there exists a valid arrangement of pairs.
#
#
from collections import defaultdict, deque
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Step 2: Find the starting node for the Eulerian path
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        # Step 3: Hierholzer's algorithm to find the Eulerian path
        stack = [start_node]
        result = []

        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            result.append(stack.pop())

        # Step 4: Format the result in reverse order
        result.reverse()
        return [[result[i], result[i + 1]] for i in range(len(result) - 1)]
