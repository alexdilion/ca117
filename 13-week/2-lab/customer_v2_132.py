#!/usr/bin/env python3

class Customer:
    def __init__(self, name, number, balance = 0):
        self.name = name
        self.number = number
        self.balance = balance
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Number: {self.number}\n"
            f"Balance: {self.balance:.02f}"
        )

    def lodge(self, amount):
        if amount >= 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
