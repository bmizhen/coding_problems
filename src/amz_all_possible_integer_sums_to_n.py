"""
# Given an integer n, return a list of all possible sets of integers
that sum up to n

Example:
    1 -> [[1]]
    2 -> [[1, 1], [2]]

    7 -> [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2],
          [1, 1, 1, 1, 3], [1, 1, 1, 2, 2], [1, 1, 1, 4], [1, 1, 2, 3],
          [1, 1, 5], [1, 2, 2, 2], [1, 2, 4], [1, 3, 3],
          [1, 6], [2, 2, 3], [2, 5], [3, 4], [7]]
"""


def get_all_compositions(n):
    answers = []

    def add_composition(current_sum, current_list, lowest_term):
        if current_sum > n:
            return
        if current_sum == n:
            answers.append(current_list.copy())
            return

        for i in range(lowest_term, n - current_sum + 1):
            current_list.append(i)
            add_composition(
                current_sum + i,
                current_list,
                i)
            current_list.pop()

    add_composition(0, [], 1)

    return answers


print(get_all_compositions(0))
print(get_all_compositions(1))
print(get_all_compositions(2))
print(get_all_compositions(3))
print(get_all_compositions(4))
print(get_all_compositions(5))
print(get_all_compositions(6))
print(get_all_compositions(7))
