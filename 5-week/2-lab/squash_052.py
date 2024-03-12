#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    
    output = ""
    i = 0
    while i < len(line):
        j = i
        while j < len(line) and line[j] == line[i]:
            j += 1
        
        output += f"{j - i}{line[i]}"
        i = j
    
    print(output)
