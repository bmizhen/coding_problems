from typing import List


class Solution:
    @staticmethod
    def reverse_subarray(nums, start, end):
        end -= 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse_subarray(nums, 0, len(nums))
        self.reverse_subarray(nums, 0, k)
        self.reverse_subarray(nums, k, len(nums))
