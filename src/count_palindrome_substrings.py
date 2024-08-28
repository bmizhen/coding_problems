# https://leetcode.com/problems/palindromic-substrings/
def count_pal_at(string, left, right):
    count = 0
    while (left >= 0 and right < len(string)
           and string[left] == string[right]):
        left -= 1
        right += 1
        count += 1

    return count


def find_palindrome_2(string):
    if not string:
        return 0

    count = 0

    for i in range(len(string)):
        # odd length
        count += 1 + count_pal_at(string, i - 1, i + 1)
        # even length
        count += count_pal_at(string, i - 1, i)

    return count
