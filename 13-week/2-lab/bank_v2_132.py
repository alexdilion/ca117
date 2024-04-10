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
    
    def __str__(self):
        sorted_customers = sorted(self.customers.values(), key=lambda c: c.number)
        output = ""
        total_funds = 0
        
        for customer in sorted_customers:
            output += str(customer) + "\n"
            total_funds += customer.balance
        
        output += f"Total funds: {total_funds:.02f}"
        return output

def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)
    c2 = Customer('John Squire', 54211677, 200.22)
    c3 = Customer('Ian Brown', 10145211, 1.50)

    b = Bank()

    b.add(c1)
    b.add(c2)
    b.add(c3)

    print(b)

if __name__ == '__main__':
    main()