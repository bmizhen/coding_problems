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
    tile_map = dict()
    island_counter = 0

    def mark_land_tiles(x, y, island_marker):
        if x < 0 or y < 0 or x >= len(the_sea_map) or y >= len(the_sea_map[x]):
            return -1

        if the_sea_map[x][y] == 0:
            return -1

        if (x, y) in tile_map:
            return tile_map[(x, y)][0]

        tile_map[(x, y)] = island_marker

        for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1), (1, 1),
                       (1, 0), (1, -1)]:
            island_marker_value = mark_land_tiles(
                x + dx, y + dy, island_marker)
            if island_marker_value > 0:
                island_marker[0] = island_marker_value

        return island_marker[0]

    for x in range(0, len(the_sea_map)):
        for y in range(len(the_sea_map[x])):
            island_marker = [0]
            island_marker[0] = mark_land_tiles(x, y, island_marker)
            if island_marker[0] == 0:
                island_counter += 1
                island_marker[0] = island_counter

    return island_counter


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
