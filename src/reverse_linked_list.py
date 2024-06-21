from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next_node: object = None


L1 = None
L2 = Node(2)
L3 = Node(val=1, next_node=Node(2, next_node=Node(3)))


# print(L1, L2, L3)

def reverse(head):
    temp_head = None
    current = head

    while current:
        current.next_node, current, temp_head = (
            temp_head, current.next_node, current
        )

    return temp_head


print(L3)
print(reverse(L3))
