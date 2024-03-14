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