# Ultrasonic Sensor Component Test

## Purpose

Test the HC-SR04 independently before integrating it into the rotating Pico sonar scanner and its green sonar-style interface. This folder is for component testing, not the final scanner implementation.

## Test setup

- Microcontroller: Raspberry Pi Pico 2
- Sensor: HC-SR04
- TRIG: GP15
- ECHO: GP14
- Sensor and Pico share a common ground.

## Simulation observations

Initial Wokwi testing occasionally produced 0.1 cm readings. These stopped after bypassing the simulated voltage divider. The precise cause has not been confirmed.

Reported stable readings:

| Wokwi setting | Displayed distance |
| --- | --- |
| 50 cm | 50.4 cm |
| 100 cm | 100.9 cm |

These are simulation results, not measurements of physical accuracy.

## Physical build

The physical circuit uses the ECHO voltage divider. The direct ECHO connection was a simulation-only diagnostic test.

The original HC-SR04 sensor was found to be faulty after systematic debugging. A replacement sensor was installed, and the existing test program and circuit then worked: the Pico triggered the sensor and received ECHO pulses on GP14.

See [`debugging-log.md`](debugging-log.md) for the full fault-isolation record and diagnosis.

## Files

The following files have been added to this folder:

- [`main.py`](main.py): MicroPython test code exported from Wokwi.
- [`diagram.json`](diagram.json): Wokwi circuit diagram.
- [`wokwi-project.txt`](wokwi-project.txt): link to the original Wokwi project.
- [`debugging-log.md`](debugging-log.md): fault-isolation tests and final sensor diagnosis.

## Next steps

1. Compare readings with ruler measurements at several distances.
2. Record repeatability and measurement error.
3. Integrate the sensor into the rotating scanner system.

## Acknowledgements

The initial MicroPython script and troubleshooting guidance were developed with AI assistance.
