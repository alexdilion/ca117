#!/usr/bin/env python3

from math import sqrt

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


binops = {'+': float.__add__,
          '-': float.__sub__,
          '*': float.__mul__,
          '/': float.__truediv__}

uniops = {'n': float.__neg__,
          'r': sqrt}

def calculator(line):
    line = line.split()
    terms = Stack()
    
    # Process terms
    while len(line) > 0 and line[0].replace(".", "").isnumeric():
        terms.push(float(line.pop(0)))
    
    # Perform operations
    for operator in line:
        if operator in uniops:
            x = terms.pop()
            result = uniops[operator](x)

            terms.push(result)
        elif operator in binops:
            x = terms.pop()
            y = terms.pop()
            result = binops[operator](y, x)

            terms.push(result)

    if len(terms) == 1:
        return terms.top()

    # We don't have a result
    # -> something went wrong so raise an IndexError
    raise IndexError

# Test code
tests = ['5',
'8.5 2 /',
'2 3 +',
'2 3 r +',
'1 2 3 * +',
'5 2 n *',
'1 2 3 + -',
'2 1 2 3 + - *',
'2 1 2 3 + - * n',
'2 1 2 3 + - * n r',
'6 +',
'9 r']

def main():
    for test in tests:
        try:
            a = calculator(test.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()