# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []

        # Helper function to perform recursive postorder traversal
        def traverse(node):
            # Recurse on each child
            for child in node.children:
                traverse(child)
            # Process the node itself
            result.append(node.val)

        traverse(root)
        return result
