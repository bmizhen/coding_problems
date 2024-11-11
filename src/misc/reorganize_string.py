# https://leetcode.com/problems/reorganize-string/

from collections import Counter
from heapq import *

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-count, char) for char, count in counter.items()]

        heapify(heap)
        result = []
        last_count, last_char = None, None
        while heap:
            next_count, next_char = heappop(heap)
            result.append(next_char)
            if last_count:
                heappush(heap, (last_count, last_char))
            last_count, last_char = next_count + 1, next_char
        if last_count:
            return ''
        else:
            return ''.join(result)
