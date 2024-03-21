#!/usr/bin/env python3

def collatz(n):
    print(n)
    
    if n == 1:
        return
    elif n % 2:
        collatz(n * 3 + 1)
    else:
        collatz(n // 2)

# Test code
def main():
    collatz(5)

if __name__ == '__main__':
    main()