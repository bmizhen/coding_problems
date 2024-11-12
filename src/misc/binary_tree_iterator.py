# https://leetcode.com/problems/binary-search-tree-iterator/submissions/1424734151/
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_all_left(root)

    def push_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self.push_all_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)


class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iter = self._iterator(root)
        self._next = next(self.iter, None)

    def _iterator(self, node):
        if node:
            yield from self._iterator(node.left)
            yield node.val
            yield from self._iterator(node.right)

    def next(self) -> int:
        result, self._next = self._next, next(self.iter, None)
        return result

    def hasNext(self) -> bool:
        return self._next is not None


class BSTIterator3:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.stack.append((root, root.left, root.right))

    def next(self) -> int:
        while True:
            node, left, right = self.stack.pop()
            if not left:
                if right:
                    self.stack.append((right, right.left, right.right))
                return node.val
            else:
                self.stack.append((node, None, right))
                self.stack.append((left, left.left, left.right))

    def hasNext(self) -> bool:
        return len(self.stack) > 0
