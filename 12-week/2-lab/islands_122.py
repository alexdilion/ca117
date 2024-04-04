#!/usr/bin/env python3

import sys

class Graph:
    def __init__(self, V):
        self.V = V
        self.nodes = [False] * V
        self.edges = [list() for i in range(V)]
    
    def addEdge(self, v, w):
        self.edges[v].append(w)
        self.edges[w].append(v)
    
    def dfs(self, v):
        self.nodes[v] = True
        
        for w in self.edges[v]:
            if not self.nodes[w]:
                self.dfs(w)
    
    def countIslands(self):
        count = 0
        for v in range(self.V):
            if not self.nodes[v]:
                count += 1
                self.dfs(v)
        
        return count

g = Graph(int(sys.stdin.readline()))
for edge in sys.stdin:
    v, w = [int(n) for n in edge.split()]
    g.addEdge(v, w)

print(g.countIslands())