# https://leetcode.com/problems/is-graph-bipartite/

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        red_nodes = set()
        blue_nodes = set()

        for n in range(len(graph)):
            # print(red_nodes, blue_nodes, n)
            if n in red_nodes or n in blue_nodes:
                continue
            if not self.dfs(n, graph, red_nodes, blue_nodes):
                return False
        return True

    def dfs(self, node, graph, my_set, other_set):
        if node in other_set:
            return False

        if node in my_set:
            return True

        my_set.add(node)

        return all(self.dfs(n, graph, other_set, my_set)
                   for n in graph[node])
