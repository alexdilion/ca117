#!/usr/bin/env python3

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def midpoint(self, p2):
        midX = self.x + (p2.x - self.x) / 2
        midY = self.y + (p2.y - self.y) / 2
        
        return Point(midX, midY)

    def __str__(self):
        return f"({self.x:.01f}, {self.y:.01f})"

class Circle:
    def __init__(self, centre = None, radius = 1):
        self.centre = centre or Point()
        self.radius = radius
    
    def __str__(self):
        return f"Centre: {str(self.centre)}\nRadius: {self.radius}"