# Given the root of a binary tree, return the postorder traversal of its nodes' values.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            if node is None:
                return []
            # Postorder: left, right, root
            return helper(node.left) + helper(node.right) + [node.val]

        return helper(root)
