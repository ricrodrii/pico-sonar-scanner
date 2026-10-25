# HC-SR04 debugging log

## Initial problem

The original HC-SR04 ultrasonic sensor did not produce a distance reading. The Raspberry Pi Pico 2 triggered the sensor, but no ECHO pulse was detected on GP14.

## Fault-isolation approach

The tests were carried out in a deliberate order to separate software, wiring, power, signal-level, and sensor faults. Each result was used to rule out a possible cause before moving to the next test.

## Test record

| # | Test | Method | Result | What it ruled out |
|---:|---|---|---|---|
| 1 | Basic distance code | Sent a 10 µs TRIG pulse and used `time_pulse_us()` on GP14 | No valid ECHO reading | Not conclusive alone |
| 2 | GPIO configuration check | Reviewed TRIG as GP15 output and ECHO as GP14 input | Pins were correctly configured | Software pin assignment |
| 3 | TRIG voltage check | Measured TRIG at the sensor while the Pico triggered it | TRIG switched between approximately 0 V and 3.3 V | Pico TRIG output and TRIG wiring |
| 4 | Sensor power check | Measured VCC and GND at the sensor | Sensor received 5 V | Missing sensor supply |
| 5 | ECHO wiring continuity | Checked the ECHO wire path with a multimeter | Continuity confirmed | Broken ECHO jumper or wire |
| 6 | Ground continuity | Confirmed sensor GND and Pico GND were connected | Common ground confirmed | Missing ground reference |
| 7 | GPIO loopback test | Connected GP15 through the ECHO path to GP14 and generated HIGH/LOW transitions | GP14 detected the transitions | Pico GPIOs, ECHO jumper, and basic divider path |
| 8 | Voltage-divider resistance test | Measured the 1 kΩ and 2 kΩ resistors | Resistor values were correct | Incorrect divider resistors |
| 9 | Divider continuity interpretation | Measured from the resistor junction to Pico GND | No beep, which was expected because the 2 kΩ resistor was in the path | False alarm; did not indicate a broken circuit |
| 10 | ECHO edge monitoring | Used MicroPython interrupts to watch GP14 for rising and falling edges during repeated triggers | No edges detected | Confirmed no ECHO signal reached GP14 |
| 11 | Repeated trigger test | Triggered the sensor 10 times and listened for ECHO edges | No ECHO response | Intermittent trigger or code-timing issue unlikely |
| 12 | Short-pulse loopback proposal | Planned a GP15-to-GP14 loopback using short pulses and `time_pulse_us()` | Not completed before the sensor fault was found | Would have validated short-pulse detection through the full path |
| 13 | Sensor VCC-to-GND resistance test | Measured directly between the disconnected sensor’s VCC and GND pins | Approximately 0 Ω | Sensor internally shorted or likely damaged |

## Interpretation

The software configuration, Pico GPIOs, TRIG signalling, sensor supply, common ground, ECHO wiring, and voltage-divider components were all verified. The GPIO loopback test showed that signals could travel from GP15 through the ECHO path to GP14.

The voltage-divider check should be interpreted using resistance mode rather than continuity mode. A continuity beep was not expected across the 2 kΩ resistor, so the absence of a beep did not indicate a fault.

Interrupt-based monitoring and repeated triggering confirmed that no ECHO transitions reached GP14. This made a software timing issue or intermittent trigger problem unlikely.

## Final diagnosis

With the original sensor disconnected, the resistance between its VCC and GND pins measured approximately 0 Ω. This indicated an internal short circuit.

**Conclusion:** the original HC-SR04 sensor was the failed component. The Pico, GPIO configuration, TRIG signalling, ground reference, ECHO wiring, and ECHO voltage divider were not identified as faults.

## Resolution

A replacement HC-SR04 sensor was installed. The existing test program and circuit then worked: the Pico triggered the sensor and received ECHO pulses on GP14.

This confirmed the original sensor was faulty and validated the Pico, wiring, GPIO configuration, and voltage-divider circuit.

## Lessons learned

- Use resistance measurements when checking paths that contain resistors; continuity mode can give misleading results.
- Isolate the sensor before measuring directly across its power pins.
- Use GPIO loopback tests to separate microcontroller and wiring faults from sensor faults.
- Monitor signal edges with interrupts when a simple pulse-width measurement returns no result.
- Test with a known-good replacement component to confirm a hardware diagnosis.

## Next actions

- Validate distance readings at known distances.
- Add the rotating mount and sonar-style display.
- Integrate the sensor test into the rotating scanner system.
