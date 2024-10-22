# You are given the root of a binary tree and a positive integer k.
#
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
#
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
#
# Note that two nodes are on the same level if they have the same distance from the root.
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        # Level order traversal to compute the sum of each level
        level_sums = []
        queue = deque([root])

        while queue:
            level_sum = 0
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)

        # Sort the sums in descending order
        level_sums.sort(reverse=True)

        # Check if we have enough levels
        if k > len(level_sums):
            return -1

        # Return the kth largest sum
        return level_sums[k - 1]