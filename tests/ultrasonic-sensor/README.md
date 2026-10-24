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

Physical assembly and validation are ongoing. Retain the ECHO voltage divider in the physical build; the direct ECHO connection was a simulation-only diagnostic test. Record the final resistor values and wiring before powering the completed circuit.

## Files to add

- `main.py`: the actual MicroPython test code exported from Wokwi.
- `diagram.json`: the actual Wokwi circuit diagram.

These files have not been uploaded here yet.

## Next steps

1. Add the Wokwi project files.
2. Check physical wiring and resistor values.
3. Compare readings with ruler measurements at several distances.
4. Record repeatability and measurement error.

## Acknowledgements

The initial MicroPython script and troubleshooting guidance were developed with AI assistance.
