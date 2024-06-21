class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        return (self.is_interleave(s1, s2, s3)
                or self.is_interleave(s2, s1, s3))

    @staticmethod
    def is_interleave(s1, s2, s3):
        if s1 == '':
            return s2 == s3

        if s1[0] != s3[0]:
            return False

        state = [
            [False] * len(s1) for _ in range(len(s2) + 1)
        ]

        for i, c in enumerate(s1):
            if s1[i] == s3[i]:
                state[0][i] = True
            else:
                break

        for i, c in enumerate(s2):
            if s2[i] == s3[i + 1]:
                state[i + 1][0] = True
            else:
                break

        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1)):
                if s1[j] == s3[i + j] and state[i][j - 1]:
                    state[i][j] = s1[j]
                elif s2[i - 1] == s3[i + j] and state[i - 1][j]:
                    state[i][j] = s2[i - 1]

        return state[-1][-1]


print(Solution().isInterleave(s1="db", s2="b", s3="cbb"))
print(Solution().isInterleave(s1="a", s2="", s3="c"))
print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
