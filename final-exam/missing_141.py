#!/usr/bin/env python3

import sys

m, n = [int(x) for x in sys.stdin.readline().split()]
given_seq = sys.stdin.readline().strip()

i = m
while i <= n:
    given_num = given_seq[:len(str(i))]

    if given_num != str(i):
        print(i)
        break

    given_seq = given_seq[len(str(i)):]
    i += 1
