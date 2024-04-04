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

# Test code
def main():
    with open('tin', 'r') as f:
        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    for v in range(g.V):
        print('Vertex {} connects to {}'.format(v, g.adj[v]))
        
    for v in range(V):
        print('Degree of vertex {} is {}'.format(v, g.degree(v)))

    print('Maximum degree is {}'.format(g.maxDegree()))
    print('Average degree is {:.2f}'.format(g.avgDegree()))

if __name__ == '__main__':
    main()