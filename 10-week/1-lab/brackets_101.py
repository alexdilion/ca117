#!/usr/bin/env python3

pairs = ["[]", "()", "{}"]
opening = "[({"
closing = "])}"

class Stack:
    def __init__(self):
        self.l = []
    
    def push(self, item):
        self.l.append(item)
    
    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def matcher(s):
    hits = Stack()
    
    for char in s:
        if char in opening:
            hits.push(char)
        elif char in closing:
            if hits.is_empty():
                return False

            pair = hits.pop() + char
            if pair not in pairs:
                return False
    
    return hits.is_empty()

# Test code
tests = ['()',
'(())',
'(({}))',
'(())(){}{(([]))}',
'(()',
'(()){()]',
')(()){([()])}']

def main():
    for test in tests:
        print(matcher(test.strip()))

if __name__ == '__main__':
    main()