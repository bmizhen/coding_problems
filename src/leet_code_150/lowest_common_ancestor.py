# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
            self,
            root: TreeNode,
            p: TreeNode,
            q: TreeNode) -> TreeNode | None:
        if root in {p, q, None}:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        if left not in {p, q, None}:
            return left

        right = self.lowestCommonAncestor(root.right, p, q)
        if right not in {p, q, None}:
            return right

        if {left, right} == {p, q}:
            return root

        return left or right
