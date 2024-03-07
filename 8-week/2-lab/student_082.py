#!/usr/bin/env python3

class Student:
    def __init__(self, sid, name, modlist = None):
        self.sid = sid
        self.name = name
        self.modlist = modlist or []

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def remove_module(self, module):
        self.modlist.remove(module)

    def __str__(self):
        return f"ID: {self.sid}\nName: {self.name}\nModules: {', '.join(sorted(self.modlist))}"