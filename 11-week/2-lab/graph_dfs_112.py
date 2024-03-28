#!/usr/bin/env python3

import sys

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [list() for i in range(V)]
    
    def addEdge(self, v, w):
        # Add nodes to each other's adjacency list
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return len(max(self.adj, key=lambda l: len(l)))
    
    def avgDegree(self):
        return sum([len(l) for l in self.adj]) / self.V
    
class DFSPaths:
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
    
    def hasPathTo(self, w):
        return self.visited[w]

    def pathTo(self, w):
        if not self.hasPathTo(w):
            return
        
        path = []
        currNode = w
        while currNode != -1:
            path.append(currNode)
            currNode = self.parent[currNode]
        
        return path[::-1]

# Test code
def main():
    with open('tin', 'r') as f:
        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    dfs = DFSPaths(g, 4)

    print(dfs.hasPathTo(2))
    print(dfs.pathTo(2))

if __name__ == '__main__':
    main()
