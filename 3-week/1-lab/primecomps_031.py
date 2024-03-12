#!/usr/bin/env python3

import sys

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False

    return True

for n in sys.stdin:
    primes = [v for v in range(2, int(n) + 1) if isPrime(v)]
    print(f"Primes: {primes}")
