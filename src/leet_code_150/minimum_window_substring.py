from collections import Counter


class Solution:
    def minWindow(self, string: str, template: str) -> str:
        '...a...b....a....b..b...' 'ab'

        template_counter = Counter(list(template))
        window_counter = Counter()
        window_missing_chars = set(list(template))

        left_index = 0
        window_size = 0

        min_matching_window_len = len(string) + 1
        min_window_result = ''

        for right in string:
            window_counter[right] += 1
            window_size += 1
            if window_counter[right] == template_counter[right]:
                window_missing_chars.remove(right)

            while not window_missing_chars:
                if min_matching_window_len > window_size:
                    min_window_result = string[left_index:left_index + window_size]
                    min_matching_window_len = window_size

                left = string[left_index]
                if left in template_counter:
                    window_counter[left] -= 1
                    if window_counter[left] < template_counter[left]:
                        window_missing_chars.add(left)
                left_index += 1
                window_size -= 1
        return min_window_result


assert Solution().minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
assert Solution().minWindow('cabwefgewcwaefgcf', 'cae') == 'cwae'
