"""
Find the edit distance between two strings
https://en.wikipedia.org/wiki/Levenshtein_distance
"""
from functools import cache


@cache
def edit_distance(shorter, longer):
    if len(shorter) > len(longer):
        shorter, longer = longer, shorter

    if len(shorter) == 0:
        return len(longer)

    if shorter[0] == longer[0]:
        return edit_distance(shorter[1:], longer[1:])

    return 1 + min(
        edit_distance(shorter, longer[1:]),
        edit_distance(shorter[1:], longer),
        edit_distance(shorter[1:], longer[1:])
    )


print(edit_distance('', ''))
print(edit_distance('a', ''))
print(edit_distance('', 'b'))
print(edit_distance('a', 'b'))
print(edit_distance('a', 'a'))
print(edit_distance('ab', 'aa'))
print(edit_distance('ba', 'ab'))
print(edit_distance('cat', 'dog'))
