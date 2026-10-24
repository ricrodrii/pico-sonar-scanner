# pico-sonar-scanner
A rotating ultrasonic scanner with a CAD-designed, 3D-printed mount and a green sonar-style interface that highlights nearby objects in red.

## Project goal

Build a rotating ultrasonic scanner using a Raspberry Pi Pico 2
and an HC-SR04 sensor on a CAD-designed, 3D-printed mount.

The software interface will resemble a green submarine
sonar display, with a rotating sweep and detected objects
highlighted in red at their measured angle and distance.

## Current status

The first ultrasonic sensor test is complete. Systematic debugging isolated the lack of an ECHO signal to a faulty HC-SR04 sensor rather than the Pico, wiring, GPIO configuration, or voltage-divider circuit.

See [`tests/ultrasonic-sensor/debugging-log.md`](tests/ultrasonic-sensor/debugging-log.md) for the full test record and diagnosis.

## Sensor test

The sensor test measures distance with an HC-SR04 connected to a Raspberry Pi Pico 2.

- [`tests/ultrasonic-sensor/main.py`](tests/ultrasonic-sensor/main.py) sends a 10 microsecond trigger pulse and calculates distance from the ECHO pulse.
- [`tests/ultrasonic-sensor/diagram.json`](tests/ultrasonic-sensor/diagram.json) contains the Wokwi circuit, including the ECHO voltage divider.
- [`tests/ultrasonic-sensor/wokwi-project.txt`](tests/ultrasonic-sensor/wokwi-project.txt) links to the original Wokwi project.
- [`tests/ultrasonic-sensor/debugging-log.md`](tests/ultrasonic-sensor/debugging-log.md) records the fault-isolation tests and final sensor diagnosis.

## Next steps

- Replace the faulty HC-SR04 sensor.
- Re-run the sensor test and confirm ECHO edges on GP14.
- Add the rotating mount and sonar-style display.
