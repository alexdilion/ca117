#!/usr/bin/env python3

class Meeting:
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration
    
    def __str__(self):
        time = f"{self.hour:0>2d}:{self.minute:0>2d}"
        return f"{time} ({self.duration} minutes)"

    def convertTime(self):
        return self.hour * 60 + self.minute

class Schedule:
    def __init__(self):
        self.meetings = []
    
    def add(self, meeting):
        self.meetings.append(meeting)
    
    def __str__(self):
        header = "Schedule\n--------\n"
        sortedMeetings = sorted(self.meetings, key = lambda m: m.convertTime())
        sortedMeetings = [str(m) for m in sortedMeetings]
        meetingCount = f"\nMeetings today: {len(self.meetings)}"
        
        return header + "\n".join(sortedMeetings) + meetingCount

# Test code
def main():
    schedule = Schedule()

    m = Meeting(13, 0, 15)
    schedule.add(m)

    m = Meeting(9, 5, 30)
    schedule.add(m)

    m = Meeting(16, 30, 5)
    schedule.add(m)

    print(schedule)

if __name__ == '__main__':
    main()
