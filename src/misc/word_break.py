# https://leetcode.com/problems/word-break/description/

from bisect import bisect_left
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = sorted(wordDict)
        return self.can_construct(s, 0, wordDict, dict())

    def can_construct(self, s, start, words_sorted, cache):
        if start == len(s):
            return True
        if start in cache:
            return cache[start]

        for i in range(start, len(s)):
            potential_word = s[start:i + 1]
            dict_index = bisect_left(words_sorted, potential_word)
            if dict_index == len(words_sorted):
                break
            if words_sorted[dict_index] == potential_word:
                if self.can_construct(s, i + 1, words_sorted, cache):
                    cache[start] = True
                    return True
            if not words_sorted[dict_index].startswith(potential_word):
                break

        cache[start] = False
        return False
