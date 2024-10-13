from random import shuffle, seed
import string

def create_alien_alphabet(rand_seed):
    chars = list(string.ascii_lowercase)
    seed(rand_seed)
    shuffle(chars)
    print(chars)
    return {new:old 
        for new, old in zip(chars, string.ascii_lowercase)}


def sorted_by_alphabet(words: list[str], alphabet: dict[str, str]):
    def key_fn(word):
        return ''.join(alphabet[c] for c in word)

    return sorted(words, key=key_fn)

a1 = create_alien_alphabet(1)
# print(a1)

alien_words =  ["baa","abcd","abca","cab","cad"]

# print(sorted(alien_words))
# print(sorted_by_alphabet(alien_words, a1))
# print(sorted_by_alphabet(list(string.ascii_lowercase), a1))

alien_words_2 = '''
Create a directed graph g with number of vertices equal to the number of unique characters in alien language where each character represents a node and edges between nodes indicate the relative order of characters
Do following for every pair of kak vam eto vse adjacent words in given sorted array quick 
Let the current pair of words words wvords be word and word One by one compare characters of both words and find the first mismatching characters
Create an edge in g from mismatching character of word to that of word
If the graph created is DAG Directed Acyclic Grapgh then print topological sorting of the above created graph else if the graph contains a cycle then input data is inconsistent and valid order of characters does not exist and znooz
'''.lower().split()

# print(alien_words_2)
alien_sorted = sorted_by_alphabet(alien_words_2, a1)

def create_char_graph(alien_sorted):
    char_graph : dict[ str, set] = dict()

    def add_all(word):
        for c in word:
            if c not in char_graph:
                char_graph[c] = set()

    for w1, w2 in zip(alien_sorted, alien_sorted[1:]):
        add_all(w1)
        add_all(w2)
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                char_graph[c1].add(c2)
                break

    return char_graph

char_graph = create_char_graph(alien_sorted)
print(char_graph)

def topological_sort(char_graph):
    processed = set()
    result = []

    def dfs(key, cycle_detect):
        if key in processed:
            return
        if key in cycle_detect:
            raise Exception('invalid sorting contains a cycle')
        cycle_detect.add(key)
        for child in char_graph[key]:
            dfs(child, cycle_detect)
        cycle_detect.remove(key)
        processed.add(key)
        result.append(key)

    for key in char_graph.keys():
        dfs(key, set())
    
    return list(reversed(result))

print(topological_sort(char_graph))

