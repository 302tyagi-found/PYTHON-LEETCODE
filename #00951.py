# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
# 
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
# 
# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
# 
#  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1, root2):

        def checker(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return ((checker(node1.left, node2.left) or checker(node1.left, node2.right)) and
                    (checker(node1.right, node2.right) or checker(node1.right, node2.left)))

        return checker(root1, root2)
