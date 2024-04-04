#!/usr/bin/env python3

class MP3Track:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Duration: {self.duration}"
        )
