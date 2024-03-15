#!/usr/bin/env python3

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def midpoint(self, p2):
        midX = (self.x + p2.x) / 2
        midY = (self.y + p2.y) / 2
        
        return Point(midX, midY)

    def __str__(self):
        return f"({self.x:.01f}, {self.y:.01f})"

# Test code
def main():
    p1 = Point(2, 3)
    p2 = Point(4, 6)

    p3 = p1.midpoint(p2)

    print(p1)
    print(p2)
    print(p3)

    assert(isinstance(p3, Point))

if __name__ == '__main__':
    main()