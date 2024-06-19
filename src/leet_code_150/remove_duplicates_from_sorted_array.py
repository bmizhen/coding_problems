from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        deduplicated_index = 2

        for current_index in range(2, len(nums)):
            e = nums[current_index]
            if e > nums[deduplicated_index - 1] or e > nums[deduplicated_index - 2]:
                nums[deduplicated_index] = e
                deduplicated_index += 1

        return deduplicated_index
