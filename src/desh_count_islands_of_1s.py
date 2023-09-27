"""
A 2-D matrix of 0,1 is given. 0’s denote water and 1’s denote land.
        0 0 0 0 0 0 0 0
        0 0 1 0 0 0 1 0
        0 1 1 0 0 0 1 0
        0 0 0 0 1 0 1 0
        0 0 0 0 0 0 0 0
Write a code to count Number of islands. Islands can be of any random shape.
Any two adjacent 1’s (in any of 8 directions) are part of same island.
"""


def count_islands(the_sea_map):
    visited_island_tiles = set()

    def mark_connected_land(x, y):
        if x < 0 or y < 0 or x >= len(the_sea_map) or y >= len(the_sea_map[x]):
            return 0

        if (x, y) in visited_island_tiles or the_sea_map[x][y] == 0:
            return 0

        visited_island_tiles.add((x, y))

        neighbors_offsets = [(-1, -1), (-1, 0), (-1, 1),
                             (0, -1), (0, 1), (1, 1),
                             (1, 0), (1, -1)]

        for dx, dy in neighbors_offsets:
            mark_connected_land(x + dx, y + dy)

        return 1

    return sum(mark_connected_land(x, y)
               for x in range(0, len(the_sea_map))
               for y in range(0, len(the_sea_map[x])))


print(count_islands([[]]))
print(count_islands([[0]]))
print(count_islands([[1]]))
print(count_islands([[1, 1]]))

print(count_islands([[0, 0, 1],
                     [1, 0, 0]]))

print(count_islands([[0, 0, 1],
                     [1, 0, 1]]))

print(count_islands([[0, 0, 1],
                     [1, 1, 0]]))

print(count_islands(
    [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]))
