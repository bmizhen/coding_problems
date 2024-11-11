# https://leetcode.com/problems/basic-calculator-ii/description/

class Solution:
    def tokens(self, s:str):
        buffer = []
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                buffer.append(c)
            else:
                if buffer:
                    num = int(''.join(buffer))
                    buffer = []
                    yield num
                    yield c
        yield int(''.join(buffer))


    def calculate(self, s: str) -> int:
        tokenizer = self.tokens(s.strip())
        stack = [next(tokenizer)]

        for token in tokenizer:
            if token == '+':
                stack.append(next(tokenizer))
            elif token == '-':
                stack.append(-next(tokenizer))
            elif token == '*':
                stack[-1] *= next(tokenizer)
            elif token == '/':
                stack[-1] = int(stack[-1]/next(tokenizer))
            else:
                raise Exception('should not happen' + token)

        return sum(stack)
