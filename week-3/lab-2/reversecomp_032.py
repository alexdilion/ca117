#!/usr/bin/env python3

import sys

def binsearch(query, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid].lower() < query:
            low = mid + 1
        elif sorted_list[mid].lower() > query:
            high = mid - 1
        else:
            return True

    return False

words = sys.stdin.read().strip().split()
words = [w for w in words if len(w) >= 5]
palindromes = [w for w in words if binsearch(w[::-1].lower(), words)]
print(palindromes)