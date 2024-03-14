#!/usr/bin/env python3

import sys

def processLine(line):
    data = []
    tokens = line.split()

    data.append(tokens[0])
    data.append(" ".join(tokens[1:-8]))

    for token in tokens[-8:]:
        data.append(token)

    return data

maxClubLength = 0
rows = [["POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"]]
for line in sys.stdin:
    club = processLine(line.strip())
    rows.append(club)

    if len(club[1]) > maxClubLength:
        maxClubLength = len(club[1])

for row in rows:
    rowString = f"{row[0]:>3s} {row[1]:{maxClubLength}} {row[2]:>2s}"

    for entry in row[-7:]:
        rowString += f" {entry:>3s}"

    print(rowString)
