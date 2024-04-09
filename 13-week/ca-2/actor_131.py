#!/usr/bin/env python3

class Actor:
    def __init__(self, name, nationality, fee):
        self.name = name
        self.nationality = nationality
        self.fee = fee
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Nationality: {self.nationality}\n"
            f"Fee: {self.fee}"
        )

def main():
    a1 = Actor('Cillian Murphy', 'Ireland', 5000)
    a2 = Actor('Florence Pugh', 'UK', 6000)

    assert(isinstance(a1, Actor))
    assert(a1.name == 'Cillian Murphy')
    assert(a1.nationality == 'Ireland')
    assert(a1.fee == 5000)

    print(a1)
    print(a2)

if __name__ == '__main__':
    main()