from collections import deque


# Function to find out minimum steps Knight needs to reach target position.
def minStepToReachTarget(position, target, N):
    # print(KnightPos, TargetPos, N)
    # Code here
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (-1, 2), (1, -2), (-1, -2),
    ]
    position = tuple(position)
    target = tuple(target)
    stack = deque()
    visited = set()

    stack.append((position, 0))

    while stack:
        pos, move = stack.popleft()
        if pos == target:
            return move
        if pos in visited:
            continue

        row, col = pos
        if row < 0 or col < 0 or row > N or col > N:
            continue

        visited.add(pos)

        for drow, dcol in moves:
            p2 = (row + drow, col + dcol)
            stack.append((p2, move + 1))

    return -1


print(minStepToReachTarget((4, 5), (1, 1), 8))
print(minStepToReachTarget((7, 7), (1, 1), 8))
