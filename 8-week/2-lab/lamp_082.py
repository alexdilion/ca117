#!/usr/bin/env python3

class Lamp:
    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        self.on = not self.on

# Test code
def main():
    lamp1 = Lamp()

    assert(not(lamp1.on))
    lamp1.turn_off()
    assert(not(lamp1.on))
    lamp1.turn_on()
    assert(lamp1.on)
    lamp1.turn_on()
    assert(lamp1.on)
    lamp1.turn_off()
    assert(not(lamp1.on))
    lamp1.toggle()
    assert(lamp1.on)
    lamp1.turn_off()
    lamp1.turn_off()
    assert(not(lamp1.on))

    lamp2 = Lamp(True)

    assert(lamp2.on)
    lamp2.toggle()
    assert(not(lamp2.on))

if __name__ == '__main__':
    main()