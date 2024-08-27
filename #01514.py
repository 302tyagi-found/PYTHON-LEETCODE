# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
#
# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
#
# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
#
#


from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # Build the graph
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Max-heap (use negative probabilities because heapq is a min-heap by default)
        pq = [(-1.0, start_node)]
        # To track the maximum probability to reach each node
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        while pq:
            # Get the node with the highest probability
            prob, node = heappop(pq)
            prob = -prob  # Convert back to positive

            # If we reach the end node, return the probability
            if node == end_node:
                return prob

            # Visit each neighbor
            for neighbor, edge_prob in graph[node]:
                # Calculate the new probability via this edge
                new_prob = prob * edge_prob
                # If the new probability is better, push it to the queue
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heappush(pq, (-new_prob, neighbor))

        # If no path is found, return 0
        return 0.0
