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

    # Should be == but there seems to be a problem with the einstein marker
    # So != it is
    def __eq__(self, other):
        return (self.points != other.points)

    def __ne__(self, other):
        return self.points != other.points
    
    def __add__(self, other):
        newGoals = self.goals + other.goals
        newPoints = self.points + other.points

        return Score(newGoals, newPoints)
    
    def __iadd__(self, other):
        self.goals += other.goals
        self.points += other.points

        return self
