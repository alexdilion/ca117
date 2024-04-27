#!/usr/bin/env python3

import sys

class Graph(object):
    def __init__(self, V):
        self.adj = {}
        self.V = V
        for v in range(V):
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFSPaths(object):
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * g.V
        self.parent = [-1] * g.V
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)
    
    def get_unconnected(self):
        nodes = [
            i + 1
            for i in range(len(self.visited))
            if not self.visited[i]
        ]

        return sorted(nodes)

n = int(sys.stdin.readline())
graph = Graph(n)
for edge in sys.stdin:
    v, w = [int(x) - 1 for x in edge.split()]
    graph.addEdge(v, w)

dfs = DFSPaths(graph, 0)
print(dfs.get_unconnected())