#!/usr/bin/env python3

import sys

def convertTime(time):
    minutes, seconds = time.split(":")

    try:
        return int(minutes) * 60 + int(seconds)
    except ValueError:
        return 0

runners = {}
bestRunner = ""
for runner in sys.stdin:
    name, *timeData = runner.split()
    bestTime = min([convertTime(time) for time in timeData])
    
    if bestTime:
        runners[name] = f"{bestTime // 60}:{bestTime % 60:02}"

        if not bestRunner or bestTime < convertTime(runners[bestRunner]):
            bestRunner = name

print(f"{bestRunner} : {runners[bestRunner]}")