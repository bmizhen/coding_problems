from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        state = [1] * len(nums)

        for state_index in range(1, len(nums)):
            for nums_index in range(state_index - 1, -1, -1):
                if nums[state_index] > nums[nums_index]:
                    state[state_index] = max(state[state_index], 1 + state[nums_index])

        return max(state)


print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


class Solution2:
    def lengthOfLIS(self, nums: list[int]) -> int:
        result = [nums[0]]

        for num in nums[1:]:
            result_index = bisect_left(result, num)
            print(num, result_index, result)
            if result_index == len(result):
                result.append(num)
            else:
                result[result_index] = num
            print(result)

        return len(result)
