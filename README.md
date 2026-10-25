# pico-sonar-scanner
A rotating ultrasonic scanner with a CAD-designed, 3D-printed mount and a green sonar-style interface that highlights nearby objects in red.

## Project goal

Build a rotating ultrasonic scanner using a Raspberry Pi Pico 2
and an HC-SR04 sensor on a CAD-designed, 3D-printed mount.

The software interface will resemble a green submarine
sonar display, with a rotating sweep and detected objects
highlighted in red at their measured angle and distance.

## Current status

The replacement HC-SR04 sensor has arrived and the ultrasonic
sensor test is working. The Pico successfully triggers the
sensor and receives ECHO pulses on GP14.

The original HC-SR04 was diagnosed as faulty after systematic
debugging. See
[`tests/ultrasonic-sensor/debugging-log.md`](tests/ultrasonic-sensor/debugging-log.md)
for the full test record and diagnosis.

## Sensor test

The sensor test measures distance with an HC-SR04 connected to a Raspberry Pi Pico 2.

The following sensor-test files have been added to the repository:

- [`tests/ultrasonic-sensor/main.py`](tests/ultrasonic-sensor/main.py) sends a 10 microsecond trigger pulse and calculates distance from the ECHO pulse.
- [`tests/ultrasonic-sensor/diagram.json`](tests/ultrasonic-sensor/diagram.json) contains the Wokwi circuit, including the ECHO voltage divider.
- [`tests/ultrasonic-sensor/wokwi-project.txt`](tests/ultrasonic-sensor/wokwi-project.txt) links to the original Wokwi project.
- [`tests/ultrasonic-sensor/debugging-log.md`](tests/ultrasonic-sensor/debugging-log.md) records the fault-isolation tests and final sensor diagnosis.

## AI use

AI was used to help speed up drafting, debugging, and documentation.
All AI-generated suggestions were reviewed, tested, and adapted where
necessary. The physical testing, measurements, fault diagnosis, and final
decisions in this project were carried out by the project author.

## Next steps

- Design and add the rotating mount and sonar-style display.
- Calibrate and validate distance readings at known distances.
- Integrate the sensor test into the rotating scanner system.
