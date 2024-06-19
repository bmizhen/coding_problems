from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        target = Counter(words)
        word_len = len(words[0])
        concat_length = len(words) * word_len

        indices = []
        for i in range(0, len(s) - concat_length + 1):
            substring = s[i:i + concat_length]
            compare = Counter(
                [substring[i * word_len:(i + 1) * word_len]
                 for i in range(len(words))])
            if compare == target:
                indices.append(i)
        return indices
