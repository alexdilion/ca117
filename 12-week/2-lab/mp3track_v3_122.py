#!/usr/bin/env python3

def formatToMinutes(seconds):
    return divmod(seconds, 60)

class MP3Track:
    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists
            
    def __str__(self):
        mins, seconds = formatToMinutes(self.duration)
        
        return (
            f"Title: {self.title}\n"
            f"By: {', '.join(self.artists)}\n"
            f"Duration: {mins}:{seconds:02d}"
        )
