#!/usr/bin/env python3

class Student:
    def __init__(self, name, studentId, marks = None):
        self.name = name
        self.id = studentId
        self.marks = marks or []

    def getAverage(self):
        markSum = sum([m[1] for m in self.marks])
        return round(markSum / len(self.marks) + 0.01)

    def __str__(self):
        output = f"Name: {self.name}\nID: {self.id}\n"
        output += f"Modules: {', '.join(sorted([m[0] for m in self.marks]))}\n"
        output += f"Average mark: {self.getAverage()}"

        return output

class Classlist:
    def __init__(self):
        self.students = {}
    
    def add(self, student):
        self.students[student.id] = student
    
    def __str__(self):
        sortedStudents = sorted(self.students.values(), key = lambda s: s.getAverage())
        output = [str(s) for s in sortedStudents[::-1]]

        return "\n".join(output)

# Test code
def main():
    cl = Classlist()

    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    cl.add(s1)
    cl.add(s2)

    print(cl)

if __name__ == '__main__':
    main()
