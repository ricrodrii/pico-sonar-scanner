from machine import Pin, time_pulse_us
import time

trig = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)

while True:
    trig.value(0)
    time.sleep_us(5)

    # Send the required 10 microsecond trigger pulse
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Wait for ECHO to go HIGH, then measure how long it stays HIGH
    pulse_time = time_pulse_us(echo, 1, 30000)

    if pulse_time < 0:
        print("No echo received")
    else:
        # Convert pulse duration to distance in centimetres
        distance_cm = pulse_time * 0.0343 / 2
        print("Distance: {:.1f} cm".format(distance_cm))

    time.sleep_ms(500)