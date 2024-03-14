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
