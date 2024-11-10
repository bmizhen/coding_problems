# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node'],
                   visited=set(), old_new_map={}) -> Optional['Node']:
        if not node:
            return None
        if node in visited:
            return node

        visited.add(node)

        if node not in old_new_map:
            old_new_map[node] = Node(node.val, [])
        new_node = old_new_map[node]

        for n in node.neighbors:
            if n not in old_new_map:
                old_new_map[n] = Node(n.val, [])
            new_n = old_new_map[n]
            new_node.neighbors.append(new_n)
            self.cloneGraph(n, visited, old_new_map)

        return new_node

    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stack = deque()
        stack.append(node)

        visited = set()
        old_new_map = {}

        def get_new_node(old_node):
            if old_node not in old_new_map:
                old_new_map[old_node] = Node(old_node.val, [])
            return old_new_map[old_node]

        while stack:
            old_node = stack.pop()

            if not old_node or old_node in visited:
                continue
            else:
                visited.add(old_node)

            new_node = get_new_node(old_node)

            for n in old_node.neighbors:
                stack.append(n)
                new_node.neighbors.append(get_new_node(n))

        return old_new_map[node]
