from machine import Pin, time_pulse_us
import time

trig = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)

while True:
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
        print(f"Distance: {distance_cm:.1f} cm")

    # Keep at least 60 ms between measurements
    time.sleep_ms(60)
