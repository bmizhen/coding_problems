# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next

        def make_tree(start, end):
            nonlocal head
            if end < start:
                return None

            mid = (start + end) // 2

            left = make_tree(start, mid - 1)
            val = head.val
            head = head.next
            right = make_tree(mid + 1, end)

            return TreeNode(val, left, right)

        return make_tree(0, count - 1)
