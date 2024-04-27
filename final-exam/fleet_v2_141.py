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

class Fleet:
    def __init__(self):
        self.vehicles = {}
    
    def add(self, vehicle):
        self.vehicles[vehicle.reg] = vehicle
    
    def remove(self, reg):
        if reg in self.vehicles:
            del(self.vehicles[reg])
    
    def lookup(self, reg):
        return self.vehicles.get(reg)

    def get_drivers_by_category(self, cat):
        drivers = set()
        for v in self.vehicles.values():
            if v.cat != cat:
                continue
            
            for d in v.drivers:
                drivers.add(d)
            
        return list(drivers)
