# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
            self, root: 'TreeNode',
            p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node or node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            return left and right and node or left or right

        return dfs(root)
