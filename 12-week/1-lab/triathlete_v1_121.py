#!/usr/bin/env python3

class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
    
    def __str__(self):
        output = [
            f"Name: {self.name}",
            f"ID: {self.tid}"
        ]
        
        return "\n".join(output)
