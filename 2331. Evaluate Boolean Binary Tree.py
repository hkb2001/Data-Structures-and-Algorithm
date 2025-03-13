# https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root) -> bool:
        # If leaf node, return its value
        if not root.left and not root.right:
            return bool(root.val)

        # Evaluate left and right subtrees
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:  # OR operator
            return left or right
        elif root.val == 3:  # AND operator
            return left and right

        