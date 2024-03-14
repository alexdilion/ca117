#!/usr/bin/env python3

class Student:
    def __init__(self, name, studentId, marks = None):
        self.name = name
        self.id = studentId
        self.marks = marks or []
    
    def __str__(self):
        output = f"Name: {self.name}\nID: {self.id}\n"
        output += f"Modules: {', '.join(sorted([m[0] for m in self.marks]))}\n"

        average = int((sum([m[1] for m in self.marks]) / len(self.marks)) + 0.5)
        output += f"Average mark: {average}"

        return output

def main():
    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    print(s1)
    print(s2)

if __name__ == '__main__':
    main()
