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

class Triathlon:
    def __init__(self):
        self.triathletes = {}
    
    def add(self, t):
        self.triathletes[t.tid] = t
    
    def remove(self, tid):
        del(self.triathletes[tid])
    
    def lookup(self, tid):
        return self.triathletes.get(tid)

    def __str__(self):
        output = sorted([str(t) for t in self.triathletes.values()])

        return "\n".join(output)
