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

class MovieCollection:
    def __init__(self):
        self.movies = {}

    def add(self, movie):
        self.movies[movie.title] = movie

    def get_actors(self):
        actors = set()
        for m in self.movies.values():
            for actor in m.cast:
                actors.add(actor)

        return actors

    def __str__(self):
        duration = sum([m.duration for m in self.movies.values()])
        hours, mins = divmod(duration, 60)
        return (
            f"Movies: {len(self.movies)}\n"
            f"Actors: {len(self.get_actors())}\n"
            f"Duration: {hours:01d} hour(s) {mins:02d} minute(s)"
        )

def main():
    a1 = Actor('Cillian Murphy', 'Ireland', 5000)
    a2 = Actor('Florence Pugh', 'UK', 6000)
    a3 = Actor('Franka Potente', 'Germany', 3000)
    a4 = Actor('Matt Damon', 'USA', 12000)

    m1 = Movie(title='Oppenheimer', duration=180)
    m1.add(a1)
    m1.add(a2)
    m1.add(a4)

    mc = MovieCollection()

    mc.add(m1)
    print(mc)

    m2 = Movie(title='The Bourne Identity', duration=125)
    m2.add(a3)
    m2.add(a4)

    mc.add(m2)
    print(mc)

if __name__ == '__main__':
    main()