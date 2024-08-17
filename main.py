from machine import Pin
import time

# Assuming LED 2 is connected to GPIO pin 2
led = Pin(2, Pin.OUT)

while True:
    led.value(1)  # Turn the LED on
    time.sleep(0.55)  # Wait for 0.5 seconds
    led.value(0)  # Turn the LED off
    time.sleep(0.5)  # Wait for 0.5 seconds
