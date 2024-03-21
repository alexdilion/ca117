#!/usr/bin/env python3

def reverse(arr, curr_index = 0):
    if curr_index >= len(arr) // 2:
        return arr
    
    arr[curr_index], arr[-(curr_index + 1)] = arr[-(curr_index + 1)], arr[curr_index]
    
    return reverse(arr, curr_index + 1)

def main():
    print(reverse([1,2,3]))
    print(reverse([3,4,5,6]))
    print(reverse([1,2]))

if __name__ == '__main__':
    main()