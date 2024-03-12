#!/usr/bin/env python3

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, p2):
        return ((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2) ** 0.5

    def __str__(self):
        return f"({self.x:.01f}, {self.y:.01f})"