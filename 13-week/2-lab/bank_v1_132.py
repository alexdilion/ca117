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

class Bank:
    def __init__(self):
        self.customers = {}
    
    def add(self, customer):
        self.customers[customer.number] = customer
    
    def remove(self, number):
        if number in self.customers:
            del(self.customers[number])
    
    def lookup(self, number):
        return self.customers.get(number)
