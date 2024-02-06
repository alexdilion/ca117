#!/usr/bin/env python3

import sys

def convertTime(time):
    minutes, seconds = time.split(":")

    try:
        return int(minutes) * 60 + int(seconds)
    except ValueError:
        return 0

runners = {}
for runner in sys.stdin:
    name, *timeData = runner.split()
    bestTime = min([convertTime(time) for time in timeData])
    
    if bestTime != 0:
        runners[name] = f"{bestTime // 60}:{bestTime % 60:02}"

bestRunner = min(runners, key=lambda k: convertTime(runners[k]))
print(f"{bestRunner} : {runners[bestRunner]}")