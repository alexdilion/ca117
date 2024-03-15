#!/usr/bin/env python3

class Point:
    def set_attributes(self, x, y): 
        self.x = x
        self.y = y
    
    def print_attributes(self):
        print(f"x: {self.x:.02f}")
        print(f"y: {self.y:.02f}")
    
    def reflect(self):
        self.x = -self.x
        self.y = -self.y

# Test code
def main():
    p1 = Point()
    p2 = Point()

    p1.set_attributes(5, 5)
    p2.set_attributes(4.2, 3.8)

    p1.print_attributes()
    p2.print_attributes()

    assert(p1.x == 5)
    assert(p1.y == 5)

    p1.reflect()
    p1.print_attributes()

    assert(p1.x == -5)
    assert(p1.y == -5)

if __name__ == '__main__':
    main()