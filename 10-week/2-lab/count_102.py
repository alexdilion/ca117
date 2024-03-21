#!/usr/bin/env python3

def count(s, char_count = 0):
    if s == "":
        return char_count

    return count(s[:-1], char_count + 1)

# Test code
def main():
    print(count('cat'))
    print(count('catastrophe'))
    print(count(''))

if __name__ == '__main__':
    main()