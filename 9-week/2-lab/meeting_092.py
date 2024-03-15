#!/usr/bin/env python3

class Meeting:
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration
    
    def __str__(self):
        time = f"{self.hour:0>2d}:{self.minute:0>2d}"
        return f"{time} ({self.duration} minutes)"

# Test code
def main():
    m = Meeting(9, 5, 30)

    assert(m.hour == 9)
    assert(m.minute == 5)
    assert(m.duration == 30)

    print(m)

if __name__ == '__main__':
    main()
