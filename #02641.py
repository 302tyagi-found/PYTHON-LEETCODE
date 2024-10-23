# Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
#
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
# Return the root of the modified tree.
#
# Note that the depth of a node is the number of edges in the path from the root node to it.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return

            total_sum = 0
            for node in arr:
                if not node:
                    continue
                if node.left:
                    total_sum += node.left.val
                if node.right:
                    total_sum += node.right.val

            childArr = []
            for node in arr:
                curSum = 0
                if node.left:
                    curSum += node.left.val
                if node.right:
                    curSum += node.right.val

                if node.left:
                    node.left.val = total_sum - curSum
                    childArr.append(node.left)
                if node.right:
                    node.right.val = total_sum - curSum
                    childArr.append(node.right)

            dfs(childArr)

        root.val = 0
        dfs([root])
        return root
