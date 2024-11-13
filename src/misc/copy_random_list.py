# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        old_to_new = {None: None}

        def get_node(old):
            if old not in old_to_new:
                old_to_new[old] = Node(old.val)
            return old_to_new[old]

        result = None
        last = None
        while head:
            node = get_node(head)
            if not last:
                result = node
                last = node
            else:
                last.next = node
                last = node
            if head.random:
                node.random = get_node(head.random)
            head = head.next

        return result
