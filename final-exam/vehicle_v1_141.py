#!/bin/env python3

class Vehicle:
    def __init__(self, reg, cat, mileage, drivers=None):
        self.reg = reg
        self.cat = cat
        self.mileage = mileage
        self.drivers = drivers or []
    
    def __str__(self):
        return (
            f"Reg: {self.reg}\n"
            f"Category: {self.cat}\n"
            f"Mileage: {self.mileage}\n"
            f"Drivers: {', '.join(self.drivers)}"
        )
