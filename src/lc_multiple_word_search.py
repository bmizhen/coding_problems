"""
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example 1:
Input:
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']],
words = ['oath','pea','eat','rain']
Output: ['eat','oath']

Example 2:

Input:
board = [
    ['a','b'],
    ['c','d']],
words = ['abcb']
Output: []

"""

import trie_implementation as trie


def find_words(board, words):
    root = trie.make_trie(words)
    result = set()

    def find_words_from(i, j, root, word_so_far, visited):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
            return

        if (i, j) in visited:
            return
        else:
            visited.add((i, j))

        char = board[i][j]

        if char not in root:
            return

        if 'EOS' in root[char]:
            result.add(word_so_far + char)

        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            find_words_from(
                i + di,
                j + dj,
                root[char],
                word_so_far + char,
                visited)

    for i in range(len(board)):
        for j in range(len(board[i])):
            find_words_from(
                i, j,
                root,
                '',
                set())

    return result


assert find_words(
    board=[
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']],
    words=['oath', 'pea', 'eat', 'rain']) == {'eat', 'oath'}

assert find_words(
    board=[
        ['a', 'b'],
        ['c', 'd']],
    words=['a', 'ab', 'abd', 'abcd']) == {'a', 'ab', 'abd'}
