class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        longest_size = 1
        longest_start = 0

        for center in range(len(s)):
            for half in range(0, min(center, len(s) - center - 1)):
                if s[center - half - 1] == s[center + half + 1]:
                    if longest_size < 1 + 2 * (half + 1):
                        longest_size = 1 + 2 * (half + 1)
                        longest_start = center - half - 1
                else:
                    break

            for half in range(0, min(center, len(s) - center)):
                if s[center - half - 1] == s[center + half]:
                    if longest_size < 2 * (half + 1):
                        longest_size = 2 * (half + 1)
                        longest_start = center - half - 1
                else:
                    break

        return s[longest_start:longest_start + longest_size]


# abcdefghi
print(Solution().longestPalindrome('bb'))
print(Solution().longestPalindrome('bab'))
print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('cbbd'))
