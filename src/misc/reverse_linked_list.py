# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        result_head = None
        while head:
            next_head = head.next
            head.next = result_head
            result_head = head
            head = next_head

        return result_head
