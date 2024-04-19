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
    
    def __str__(self):
        cast = ", ".join(sorted(self.cast.keys()))
        payroll = sum([a.fee for a in self.cast.values()])
        return (
            f"Title: {self.title}\n"
            f"Duration: {self.duration} minute(s)\n"
            f"Cast: {cast}\n"
            f"Payroll: {payroll}"
        )

from movie_v2_131 import Actor, Movie

def main():
    a1 = Actor('Cillian Murphy', 'Ireland', 5000)
    a2 = Actor('Florence Pugh', 'UK', 6000)
    a3 = Actor('Matt Damon', 'USA', 9000)

    m = Movie(title='Oppenheimer', duration=180)
    
    print(m)
    m.add(a3)
    print(m)
    m.add(a1)
    print(m)
    m.add(a2)
    print(m)

    m.remove('Florence Pugh')
    print(m)
    m.remove('Matt Damon')
    print(m)
    m.remove('Cillian Murphy')
    print(m)

if __name__ == '__main__':
    main()