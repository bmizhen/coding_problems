# Definition for a binary tree node.
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def isCompleteTree(self, node: Optional[TreeNode]):
        flag = False
        stack = deque()
        stack.append(node)

        while stack:
            n = stack.popleft()
            if n is None:
                if not flag:
                    flag = True
            elif flag:
                return False
            else:
                stack.append(n.left)
                stack.append(n.right)

        return True


class Solution2:
    def isCompleteTree(self, node: Optional[TreeNode]):
        self.none_level = None
        self.last_node = False
        return self.is_complete(0, node)

    def is_complete(self, level, node: Optional[TreeNode]) -> bool:
        if node is None:
            if self.none_level is None:
                self.none_level = level
                return True
            else:
                if level > self.none_level:
                    return False
                elif level < self.none_level - 1:
                    return False
                elif level == self.none_level - 1:
                    self.last_node = True
                    return True
                elif level == self.none_level:
                    if self.last_node:
                        return False
                    else:
                        return True
                else:
                    return True
        else:
            return self.is_complete(level + 1, node.left) \
                and self.is_complete(level + 1, node.right)
