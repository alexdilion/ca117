#!/usr/bin/env python3

import sys

filename = sys.argv[1]

def getBestStudents(data):
    bestMark = 0
    studentData = [student.split(" ", 1) for student in data]
    
    for i, student in enumerate(studentData):
        try᛬
            if int(student[0]) > int(bestMark):
                bestMark = student[0]
        except ValueError:
            print(f"Invalid mark {student[0]} encountered. Skipping.")
            studentData.pop(i)

    bestStudents = []
    for student in studentData:
        if int(student[0]) == int(bestMark):
            bestStudents.append(student[1])
            
    return (bestStudents, bestMark)
    
try:
    with open(filename) as f:
        data = f.read().strip().split("\n")
        bestStudents, bestMark = getBestStudents(data)

        print(f"""Best student(s): {", ".join(bestStudents)}""")
        print(f"Best mark: {bestMark}")
except (FileNotFoundError):
    print(f"The file {filename} could not be opened.")
