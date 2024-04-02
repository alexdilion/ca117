#!/usr/bin/env python3

class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.disciplines = {}
    
    def add_time(self, d, time):
        self.disciplines[d] = time
    
    def get_time(self, d):
        return self.disciplines[d]
    
    def get_total_time(self):
        return sum(self.disciplines.values())
    
    def __str__(self):
        output = [
            f"Name: {self.name}",
            f"ID: {self.tid}",
            f"Race time: {self.get_total_time()}"
        ]
        
        return "\n".join(output)

    def __eq__(self, other):
        return self.get_total_time() == other.get_total_time()
    
    def __gt__(self, other):
        return self.get_total_time() > other.get_total_time()
    
    def __lt__(self, other):
        return self.get_total_time() < other.get_total_time()
