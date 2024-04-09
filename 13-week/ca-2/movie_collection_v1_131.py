#!/usr/bin/env python3

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

    def __str__(self):
        duration = sum([m.duration for m in self.movies.values()])
        hours, mins = divmod(duration, 60)
        return (
            f"Movies: {len(self.movies)}\n"
            f"Duration: {hours:01d} hour(s) {mins:02d} minute(s)"
        )

def main():
    m1 = Movie(title='Oppenheimer', duration=180)
    m2 = Movie(title='Dune 2', duration=165)

    mc = MovieCollection()

    mc.add(m1)
    mc.add(m2)
    print(mc)

if __name__ == '__main__':
    main()