#!/usr/bin/env python3

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, p2):
        return ((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2) ** 0.5

    def __str__(self):
        return f"({self.x:.01f}, {self.y:.01f})"

# Test code
def main():
    p1 = Point()

    assert(p1.x == 0)
    assert(p1.y == 0)
    print(p1)

    p2 = Point(3, 4)

    assert(p2.x == 3)
    assert(p2.y == 4)
    print(p2)

    print('{:.1f}'.format(p1.distance(p2)))

if __name__ == '__main__':
    main()