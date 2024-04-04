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
