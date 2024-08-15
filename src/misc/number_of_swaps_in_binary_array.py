'''

https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/

000001111111100000000000000

Input: data = [0,0,0,1,0]
Output: 0

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.

## Extention: make it a circular array

'''


# [1,0,1,0,1]
def min_swaps(nums: list[int]):
    total_ones = sum(nums)  # 3

    start = 0
    end = total_ones  # 3
    if total_ones == 0:
        return 0

    ones_in_window = sum(nums[:total_ones])  # 2
    max_ones_in_window = ones_in_window  # 2

    while start < len(nums):  # 5 < 5
        ones_in_window -= nums[start]
        start += 1  # 2
        end += 1  # 5
        ones_in_window += nums[end % len(nums) - 1]  # 2
        max_ones_in_window = max(ones_in_window, max_ones_in_window)  # 2

    return total_ones - max_ones_in_window  # 1
