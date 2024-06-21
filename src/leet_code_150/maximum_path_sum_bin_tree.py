# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max = float('-inf')

    def maxPathSum(self, root) -> int:
        self.max = float('-inf')
        self.max_path(root)
        return self.max

    def max_path(self, root):
        if not root:
            return None

        left = self.max_path(root.left)
        right = self.max_path(root.right)

        if not left and not right:
            result = root.val
            self.max = max(self.max, result)
        elif not left:
            result = max(right + root.val, root.val)
            self.max = max(self.max, result, right)
        elif not right:
            result = max(left + root.val, root.val)
            self.max = max(self.max, result, left)
        else:
            self.max = max(self.max,
                           left + root.val,
                           right + root.val,
                           left + right + root.val,
                           root.val)

            result = max(left + root.val,
                         right + root.val,
                         root.val)

        return result
