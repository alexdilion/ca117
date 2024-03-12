#!/usr/bin/env python3

import sys

filename = sys.argv[1]

try:
    with open(filename) as f:
        data = f.read().strip().split("\n")

        bestMark = 0
        bestStudent = ""
        studentData = [student.split(" ", 1) for student in data]
        for student in studentData:
            if int(student[0]) > int(bestMark):
                bestMark, bestStudent = student
        
        print(f"Best student: {bestStudent}")
        print(f"Best mark: {bestMark}")
except (FileNotFoundError):
    print(f"The file {filename} could not be opened.")
