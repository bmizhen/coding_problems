class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        last_line = []
        for line, line_size in self.get_next_line_words(words, maxWidth):
            last_line = line
            line = self.justify_line(line, line_size, maxWidth)
            line = line + ' ' * (maxWidth - len(line))
            result.append(line)

        if not last_line:
            result = result[:-1]
        else:
            last_line = ' '.join(last_line)
            last_line = last_line + ' ' * (maxWidth - len(last_line))
            result[-1] = last_line
        return result

    def get_next_line_words(self, words, maxWidth):
        line = []
        line_size = 0
        for word in words:
            line.append(word)
            line_size += len(word) + 1
            if line_size == maxWidth + 1:
                yield line, line_size - 1
                line = []
                line_size = 0
            if line_size > maxWidth + 1:
                yield line[:-1], line_size - 2 - len(word)
                line = [word]
                line_size = len(word) + 1
        yield line, line_size - 1

    def justify_line(self, line, line_size, maxWidth):
        extra_spaces = maxWidth - line_size
        gaps = len(line) - 1
        if gaps > 0:
            space_size = extra_spaces // gaps + 1
            extended_spaces_left = extra_spaces % gaps
        else:
            space_size = extra_spaces
            extended_spaces_left = 0

        result = []

        for w in line:
            result.append(w)
            result.append(' ' * space_size)
            if extended_spaces_left:
                result.append(' ')
                extended_spaces_left -= 1

        return ''.join(result[:-1])


print(Solution().fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."],
    maxWidth=16))
