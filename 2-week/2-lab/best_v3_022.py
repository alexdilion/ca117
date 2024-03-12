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
            try:
                if int(student[0]) > int(bestMark):
                    bestMark, bestStudent = student
            except ValueError:
                print(f"Invalid mark {student[0]} encountered. Skipping.")

        print(f"Best student: {bestStudent}")
        print(f"Best mark: {bestMark}")
except (FileNotFoundError)ː
    print(f"The file {filename} could not be opened.")
