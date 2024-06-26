#!/usr/bin/env python3

class Student:
    def __init__(self, name, studentId, marks):
        self.name = name
        self.id = studentId
        self.marks = {module: mark for module, mark in marks}
    
    def getAverage(self):
        return round(sum(self.marks.values()) / len(self.marks) + 0.01)

    def __str__(self):
        output = f"Name: {self.name}\nID: {self.id}\n"
        output += f"Modules: {', '.join(sorted(self.marks.keys()))}\n"
        output += f"Average mark: {self.getAverage()}"

        return output

def main():
    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    print(s1)
    print(s2)

if __name__ == '__main__':
    main()
