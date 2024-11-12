# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.columns = defaultdict(list)
        self.vertical(root, 0, 0)
        return [[val for row, val in sorted(self.columns[col])]
                for col in sorted(self.columns.keys())]

    def vertical(self, node, row, col):
        if not node:
            return

        self.columns[col].append((row, node.val))

        self.vertical(node.left, row + 1, col - 1)
        self.vertical(node.right, row + 1, col + 1)
