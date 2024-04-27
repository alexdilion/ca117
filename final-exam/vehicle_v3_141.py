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
            f"Drivers: {', '.join(self.drivers)}\n"
            f"{self.service_due_in()}"
        )
    
    def add_driver(self, driver):
        self.drivers.append(driver)

    def service_due_in(self):
        m, d = self.mileage, 10000
        m_since_service = m - (m // d * d)
        
        if m_since_service == 0:
            due_in = "Service due now"
        else:
            due_in = f"Service due in {d - m_since_service} mile(s)"
        
        return due_in
