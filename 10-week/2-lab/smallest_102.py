#!/usr/bin/env python3

def smallest(arr, smallest_n = None):
    if len(arr) == 0:
        return smallest_n
    
    if not smallest_n or arr[-1] < smallest_n:
        smallest_n = arr[-1]
    
    return smallest(arr[:-1], smallest_n)

# Test code
def main():
    print(smallest([6,5,1,3,4]))
    print(smallest([6,5,11,3,4]))
    print(smallest([6,15,11,13,14]))
    print(smallest([6,15,11,13,4]))

if __name__ == '__main__':
    main()