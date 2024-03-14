#!/usr/bin/env python3

import sys
from calendar import weekday

poemLines = [
    "Monday's child is fair of face",
    "Tuesday's child is full of grace",
    "Wednesday's child is full of woe",
    "Thursday's child has far to go",
    "Friday's child is loving and giving",
    "Saturday's child works hard for a living",
    "Sunday's child is fair and wise and good in every way"
]

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

for line in sys.stdin:
    date = [int(v) for v in line.split()]
    dayOfWeek = weekday(*date[::-1])
    print(f"You were born on a {days[dayOfWeek]} and {poemLines[dayOfWeek]}.")
