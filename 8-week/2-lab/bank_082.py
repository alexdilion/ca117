#!/usr/bin/env python3

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    
    def __str__(self):
        return f"Your current balance is {self.balance:.02f} euro"