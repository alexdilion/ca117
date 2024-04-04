#!/usr/bin/env python3

class MP3Track:
    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists
    
    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"By: {', '.join(self.artists)}\n"
            f"Duration: {self.duration}"
        )

class MP3Collection:
    def __init__(self):
        self.tracks = {}
    
    def add(self, track):
        self.tracks[track.title] = track
    
    def remove(self, track_title):
        if track_title in self.tracks:
            del(self.tracks[track_title])
    
    def lookup(self, title):
        return self.tracks.get(title)
    
    def __add__(self, other):
        new_collection = MP3Collection()
        
        for track in self.tracks.values():
            new_collection.add(track)
        
        for track in other.tracks.values():
            new_collection.add(track)
        
        return new_collection
