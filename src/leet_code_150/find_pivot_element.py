"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

# https://leetcode.com/problems/search-in-rotated-sorted-array/

def find_pivot(nums, left, right):
    if left == right:
        return 0

    mid = (left + right) // 2
    if nums[mid] > nums[mid + 1]:
        return mid + 1
    if nums[mid] > nums[right]:
        return find_pivot(nums, mid + 1, right)
    else:
        return find_pivot(nums, left, mid)


def find_target_(nums, left, right, target):
    if left == right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        return find_target_(nums, left, mid, target)
    else:
        return find_target_(nums, mid + 1, right, target)


def find_target(nums, target):
    pivot = find_pivot(nums, 0, len(nums) - 1)
    return max(
        find_target_(nums, 0, pivot, target),
        find_target_(nums, pivot, len(nums), target)
    )


print(find_pivot([1, 3], 0, 1))
print(find_pivot([3, 1], 0, 1))

print(find_target([1, 3], 0))

print(find_target([4, 5, 6, 7, 8, 0, 1, 2], 8))
print(find_target([4, 5, 6, 7, 8, 0, 1, 2], 4))

print(find_pivot([6, 7, 8, 1, 2, 3, 4, 5], 0, 7))

print(find_target([6, 7, 8, 1, 2, 3, 4, 5], 6))
