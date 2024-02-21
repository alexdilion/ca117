 #!/usr/bin/env python3

import sys

bricks = [int(b) for b in sys.stdin.read().split()]
towers = []

tower = [bricks[0]]
for brick in bricks[1:]:
    if tower[-1] < brick:
        towers.append(tower)
        tower = [brick]
    else:
        tower.append(brick)

towers.append(tower)
print(len(towers))