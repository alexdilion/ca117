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

class BFSPaths:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = [False] * g.V
        self.parent = [-1] * g.V
        self.bfs(s)
    
    def bfs(self, s):
        queue = [s]
        self.marked[s] = True
        
        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.parent[w] = v
                    self.marked[w] = True
    
    def hasPathTo(self, w):
        return self.marked[w]

    def pathTo(self, w):
        if not self.hasPathTo(w):
            return
        
        path = [w]
        currNode = self.parent[w]
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

    bfs = BFSPaths(g, 4)

    print(bfs.hasPathTo(2))
    print(bfs.pathTo(2))

if __name__ == '__main__':
    main()