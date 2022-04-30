# 399 Evaluate Division
"""
From: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
In CS the Floyd-Warshall Algorithm is an algo for finding the shortest
paths in a directed weighted graph with positive or negative weights 
(but no negative cycles). A single execution of the algorithm will find 
the lengths (summed weights) of shortest paths between all pairs of vertices.

A single execution of the algo will find lengths (summed weights) 
of shortest paths between all pairs of vertices. Although,
it doesn't return details of the paths themselves, it is possible to
reconstruct the paths with simple modifications to the algo.
"""
class Solution:
    def calcEquation(self, equations, values, queries):
        quot = collections.defaultdict(dict)
        # Note: the code is to build all possible connections
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        for k, i, j in itertools.permutations(quot, 3):
            if k in quot[i] and j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
        return [quot[num].get(den, -1.0) for num, den in queries]