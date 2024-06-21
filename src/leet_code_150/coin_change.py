class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        state = list([amount + 1] * (amount + 1))
        state[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    state[i] = min(state[i], 1 + state[i - c])

        return -1 if state[-1] > amount else state[-1]


print(Solution().coinChange([1, 2, 5], 11))
