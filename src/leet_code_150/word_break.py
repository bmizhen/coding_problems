class Solution:
    def wordBreak(self, s: str, word_dict: list[str]) -> bool:
        state = [False] * (len(s) + 1)
        state[0] = True

        for i in range(len(state)):
            if not state[i]:
                continue
            for word in word_dict:
                if i + len(word) <= len(s):
                    if word == s[i:i + len(word)]:
                        state[i + len(word)] = True

        return state[-1]
