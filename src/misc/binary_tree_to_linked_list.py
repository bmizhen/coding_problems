class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def dfs(self, node):
    if not node:
        return None, None

    left_head, left_tail = self.dfs(node.left)
    right_head, right_tail = self.dfs(node.right)

    node.left = left_tail
    node.right = right_head

    if left_tail:
        left_tail.right = node

    if right_head:
        right_head.left = node

    return left_head or node, right_tail or node


