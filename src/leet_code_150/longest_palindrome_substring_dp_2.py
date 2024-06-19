class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        is_palindrome_state = [
            [i == j for j in range(len(s))]
            for i in range(len(s))
        ]

        max_palindrome_range = 0, 0

        for end in range(0, len(s)):
            for start in range(end - 1, -1, -1):
                # pprint(is_palindrome_state)
                print(start, end)
                if (s[start] == s[end]
                        and (end - start == 1
                             or is_palindrome_state[start + 1][end - 1])):
                    is_palindrome_state[start][end] = True

                    ms, me = max_palindrome_range
                    if end - start > me - ms:
                        max_palindrome_range = start, end

        ms, me = max_palindrome_range
        return s[ms:me + 1]


# abcdefghi
print(Solution().longestPalindrome('abba'))
# print(Solution().longestPalindrome('bacabab'))
# print(Solution().longestPalindrome('bb'))
# print(Solution().longestPalindrome('bab'))
# print(Solution().longestPalindrome('babad'))
# print(Solution().longestPalindrome('cbbd'))
