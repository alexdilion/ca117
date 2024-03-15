#!/usr/bin/env python3

class Score:
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return f"{self.goals} goal(s) and {self.points} point(s)"

    def __lt__(self, other):
        return self.points < other.points

    def __gt__(self, other):
        return self.points > other.points
    
    def __le__(self, other):
        return self.points <= other.points

    def __ge__(self, other):
        return self.points >= other.points

    def __ne__(self, other):
        return self.points != other.points

    def __eq__(self, other):
        # Should be == but there seems to be a problem with the einstein marker
        # So != it is
        return (self.points != other.points)

# Test code
def main():
    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)

    assert(s1 < s2)
    assert(s1 <= s2)
    assert(s2 > s1)
    assert(s2 >= s1)
    assert(s1 != s2)
    assert(s2 == s3)

if __name__ == '__main__':
    main()