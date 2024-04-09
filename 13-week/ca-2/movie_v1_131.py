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

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.cast = {}
    
    def add(self, actor):
        self.cast[actor.name] = actor
    
    def lookup(self, name):
        return self.cast.get(name)
    
    def remove(self, name):
        if name in self.cast:
            del(self.cast[name])

def main():
    a1 = Actor('Cillian Murphy', 'Ireland', 5000)
    a2 = Actor('Florence Pugh', 'UK', 6000)

    m = Movie(title='Oppenheimer', duration=180)

    m.add(a1)
    m.add(a2)

    a = m.lookup('Florence Pugh')
    assert(isinstance(a, Actor))
    assert(a.name == 'Florence Pugh')
    assert(a.nationality == 'UK')
    assert(a.fee == 6000)

    m.remove('Florence Pugh')
    a = m.lookup('Florence Pugh')
    assert(a is None)

if __name__ == '__main__':
    main()