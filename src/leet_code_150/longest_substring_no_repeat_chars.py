class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_tracker = set()
        max_substring = 0
        substring_length = 0
        left_index = 0

        for right in s:
            substring_length += 1
            if right not in char_tracker:
                char_tracker.add(right)
            else:
                while s[left_index] != right:
                    char_tracker.remove(s[left_index])
                    substring_length -= 1
                    left_index += 1
                substring_length -= 1
                left_index += 1

            max_substring = max(max_substring, substring_length)

        return max_substring
