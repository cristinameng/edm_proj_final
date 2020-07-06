from utime import ticks_ms
from machine import Pin

class Led:
    def __init__(self, pin, active_high=True):
        self.active_high = active_high
        self.led = Pin(pin, Pin.OUT)
        self.state(False)
        self.period = 0
        self.last = 0

    def logic(self, value):
        return value if self.active_high else not value

    def state(self, value=None):
        if value is not None:
            self.led.value(self.logic(value))
        return self.logic(self.led.value())

    def on(self):
        self.period = 0
        self.state(True)

    def off(self):
        self.period = 0
        self.state(False)

    def blink(self, period):
        self.period = period
        self.last = ticks_ms()

    def proc(self):
        if self.period != 0:
            if ticks_ms() - self.last >= self.period:
                self.state(not self.state())
                self.last = ticks_ms()
                