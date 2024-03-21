#!/usr/bin/env python3

def biggest(arr, biggest_n = None):
    if len(arr) == 0:
        return biggest_n
    
    if not biggest_n or arr[-1] > biggest_n:
        biggest_n = arr[-1]
    
    return biggest(arr[:-1], biggest_n)

# Test code
def main():
    print(biggest([6,5,1,3,4]))
    print(biggest([6,5,11,3,4]))
    print(biggest([6,15,11,13,14]))
    print(biggest([6,15,11,13,4]))

if __name__ == '__main__':
    main()