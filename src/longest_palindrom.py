def find_max_pal_at(string, left, right):
    while (left >= 0 and right < len(string)
           and string[left] == string[right]):
        left -= 1
        right += 1

    return left + 1, right - 1


def find_palindrome_2(string):
    if not string:
        return string

    left = 0
    right = 0

    def update_bounds(bounds):
        nonlocal left, right
        l, r = bounds
        if right - left < r - l:
            left, right = l, r

    for i in range(len(string)):
        # odd length
        update_bounds(find_max_pal_at(string, i - 1, i + 1))
        # even length
        update_bounds(find_max_pal_at(string, i - 1, i))

    return string[left:right + 1]


def find_p(string):
    result = find_palindrome_2(string)
    print('>>>', result)
    return result


if __name__ == '__main__':
    assert find_p('') == ''
    assert find_p('ac') == 'a'
    assert find_p('a') == 'a'
    assert find_p('aaba') == 'aba'
    assert find_p('aabaa') == 'aabaa'
    assert find_p('abaa') == 'aba'
    assert find_p('1234567890') == '1'

    assert find_p('ab') == 'a'
    assert find_p('bb') == 'bb'
