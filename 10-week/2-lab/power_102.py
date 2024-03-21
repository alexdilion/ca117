#!/usr/bin/env python3

def power(m, n):
    if n == 0:
        return 1
    
    if n > 0:
        return m * power(m, n - 1)
    else:
        return (1 / m) * power(m, n + 1)

# Test code
def main():
    print(power(2,3))
    print(power(4,4))
    print(power(2,32))
    print(power(10,3))
    print(power(8,0))
    print(power(2, -2))
    print(power(2, -1))
    print(power(2, -0))

if __name__ == '__main__':
    main()