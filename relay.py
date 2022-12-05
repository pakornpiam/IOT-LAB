from machine import Pin
import time
relay = Pin(16,Pin.OUT)
def relay_on():
    relay.value(1)
    print('LED:ON')

def relay_off():
    relay.value(0)
    print('LED:off')
    