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

class Circle:
    def __init__(self, centre = None, radius = 1):
        self.centre = centre or Point()
        self.radius = radius
    
    def __str__(self):
        return f"Centre: {self.centre}\nRadius: {self.radius}"

# Test code
def main():
    p1 = Point(2, 3)
    c1 = Circle(p1, 5)
    assert(c1.centre is p1)
    assert(c1.radius == 5)

    c2 = Circle()
    assert(isinstance(c2.centre, Point))
    assert(c2.radius == 1)

    c3 = Circle()
    assert(c3.centre is not c2.centre)

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()