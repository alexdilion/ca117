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

# Test code
def main():
    b1 = BankAccount()

    assert(b1.balance == 0)
    b1.deposit(100)
    b1.deposit(50)
    assert(b1.balance == 150)
    b1.withdraw(200)
    assert(b1.balance == 150)
    b1.withdraw(150)
    assert(b1.balance == 0)
    print(b1)

    b2 = BankAccount(30)

    assert(b2.balance == 30)
    b2.withdraw(0.01)
    print(b2)

if __name__ == '__main__':
    main()