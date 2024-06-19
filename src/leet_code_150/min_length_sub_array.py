class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left_index = 0

        min_length = len(nums) + 1
        window_length = 0
        window_total = 0

        for right in nums:
            window_total += right
            window_length += 1

            while window_total >= target:
                min_length = min(min_length, window_length)
                window_total -= nums[left_index]
                window_length -= 1
                left_index += 1

        return min_length if min_length <= len(nums) else 0
