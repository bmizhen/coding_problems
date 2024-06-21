class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        state = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(0, len(word1) + 1):
            state[i][0] = i

        for j in range(0, len(word2) + 1):
            state[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    state[i][j] = state[i - 1][j - 1]
                else:
                    state[i][j] = 1 + min(
                        state[i][j - 1], state[i - 1][j], state[i - 1][j - 1])

        return state[-1][-1]


print(Solution().minDistance('abc', 'de'))
print(Solution().minDistance('abc', 'abc'))
print(Solution().minDistance('abc', 'de'))
print(Solution().minDistance('abc', 'ca'))
print(Solution().minDistance('abc', 'ac'))
