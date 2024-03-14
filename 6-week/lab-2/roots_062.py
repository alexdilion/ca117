#!/usr/bin/env python3

import sys

def getRoots(a, b, c):
    determinant = (b ** 2) - (4 * a * c)
    
    if determinant < 0:
        return None
    
    root1 = (-b - (determinant) ** .5) / (2 * a)
    root2 = (-b + (determinant) ** .5) / (2 * a)

    return root1, root2

for line in sys.stdin:
    a, b, c = [int(x) for x in line.strip().split()]
    roots = getRoots(a, b, c)
    
    if roots:
        print(f"{roots[0]:.1f}, {roots[1]:.1f}")
    else:
        print(None)
