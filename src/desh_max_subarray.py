"""
Given an array of integers, find a max(sum(subarray) for all subarray)

Kadane Algorithm with all negative numbers support.

"""


def max_subarray(integers: list[int]):
    max_element = max(integers)
    if max_element <= 0:
        return max_element

    max_ending_here = 0
    max_so_far = 0

    for next_number in integers:
        max_ending_here = max(0, max_ending_here + next_number)
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far


print(max_subarray([0]))
print(max_subarray([1]))
print(max_subarray([1, -2, 0]))
print(max_subarray([10, 3]))
print(max_subarray([-10, -3]))
print(max_subarray([-10, 1, -3]))
print(max_subarray([-10, -1, 1]))
print(max_subarray([-3, 2, 3, 4, -9, 1, -7, 19]))
