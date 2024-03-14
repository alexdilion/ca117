#!/usr/bin/env python3

def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            if i != n // i:
                divisors.append(n // i)

            divisors.append(i)
    
    return sorted(divisors)
        
def get_proper_divisors(n):
    divisors = get_divisors(n)
    
    return divisors[:-1]

def is_perfect(n):
    divisors = get_proper_divisors(n)
    
    return sum(divisors) == n
