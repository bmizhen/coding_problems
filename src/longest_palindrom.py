CACHE = set()


def is_palindrome(string, boundary):
    start, end = boundary
    while start < end:
        if string[start] != string[end - 1]:
            return False
        start += 1
        end -= 1

    return True


def find_palindrome(string, boundary):
    start, end = boundary
    if end - start == 0:
        return ''

    if boundary in CACHE:
        return ''

    CACHE.add(boundary)

    if is_palindrome(string, boundary):
        return string[start: end]

    left = find_palindrome(string, (start, end - 1))
    right = find_palindrome(string, (start + 1, end))

    return left if (len(left) >= len(right)) else right


def find_p(string):
    global CACHE
    CACHE = set()
    print('>>>', string)
    return find_palindrome(string, (0, len(string)))


if __name__ == '__main__':
    print(find_p(''))
    print(find_p('a'))
    print(find_p('ab'))
    print(find_p('bb'))
    print(find_p('aaba'))
    print(find_p('aabaa'))
