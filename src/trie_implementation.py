from pprint import pprint


def make_trie(strings: list[str]):
    root: dict[str, dict] = {}

    for s in strings:
        insert(root, s)

    return root


def insert(root, s):
    if len(s) == 0:
        root['EOS'] = True
    else:
        head = s[0]
        if head not in root:
            root[head] = {}
        insert(root[head], s[1:])


def find_in_trie(root, s, require_complete=True):
    if len(s) == 0:
        return (not require_complete) or ('EOS' in root)
    head = s[0]
    return head in root and find_in_trie(
        root[head],
        s[1:],
        require_complete=require_complete)


root = make_trie(['ab', 'adadasd', 'abracadabra', 'abbac'])
pprint(root)

print(find_in_trie(root, 'a'))
print(find_in_trie(root, 'ab'))
print(find_in_trie(root, 'abc'))
print(find_in_trie(root, 'a', require_complete=False))
print(find_in_trie(root, 'ab', require_complete=False))
print(find_in_trie(root, 'b', require_complete=False))
print(find_in_trie(root, 'b'))
