---
title: "okalachev/flix: Making an ESP32-based quadcopter from scratch"
source: "https://github.com/okalachev/flix"
author:
  - "[[okalachev]]"
published:
created: 2026-05-31
description: "Making an ESP32-based quadcopter from scratch. Contribute to okalachev/flix development by creating an account on GitHub."
tags:
  - "clippings"
---
[![Flix logo](https://github.com/okalachev/flix/raw/master/docs/img/flix.svg)](https://github.com/okalachev/flix/blob/master/docs/img/flix.svg)  
**Flix** (*flight + X*) — open source ESP32-based quadcopter made from scratch.

| **Version 1.1** (3D-printed frame) | **Version 0** |
| --- | --- |
| [![Flix quadcopter](https://github.com/okalachev/flix/raw/master/docs/img/flix1.1.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/flix1.1.jpg) |  |

## Features

- Dedicated for education and research.
- Made from general-purpose components.
- Simple and clean source code in Arduino (<2k lines firmware).
- Communication using MAVLink protocol over Wi-Fi or ESP-NOW.
- Control with USB gamepad, remote control or smartphone.
- Wireless command line interface and analyzing.
- Precise simulation with Gazebo.
- Python library for scripting and automatic flights.
- Textbook on flight control theory and practice ([in development](https://quadcopter.dev/)).
- *Position control (planned)*.

## It actually flies

See detailed demo video: [https://youtu.be/hT46CZ1CgC4](https://youtu.be/hT46CZ1CgC4).

[![](https://camo.githubusercontent.com/803f2ac2ff6f31c30381e1b3e24faa81944dd903725fcb8163323bcccc85b124/68747470733a2f2f69332e7974696d672e636f6d2f76692f68543436435a31436743342f6d617872657364656661756c742e6a7067)](https://youtu.be/hT46CZ1CgC4)

Version 0 demo video: [https://youtu.be/8GzzIQ3C6DQ](https://youtu.be/8GzzIQ3C6DQ).

[![](https://camo.githubusercontent.com/936934fef16d48313de03443be6cf414124c3349c34884f89123a8f61ef32f49/68747470733a2f2f69332e7974696d672e636f6d2f76692f38477a7a495133433644512f6d617872657364656661756c742e6a7067)](https://youtu.be/8GzzIQ3C6DQ)

Usage in education (RoboCamp): [https://youtu.be/Wd3yaorjTx0](https://youtu.be/Wd3yaorjTx0).

[![](https://camo.githubusercontent.com/8645fca720f506bc6ec7f8dc0b6bc0eacefa30f913f0feaaec8d0cd2733f6e63/68747470733a2f2f69332e7974696d672e636f6d2f76692f57643379616f726a5478302f736464656661756c742e6a7067)](https://youtu.be/Wd3yaorjTx0)

See the [user builds gallery](https://github.com/okalachev/flix/blob/master/docs/user.md):

[![](https://github.com/okalachev/flix/raw/master/docs/img/user/user.jpg)](https://github.com/okalachev/flix/blob/master/docs/user.md)

### PCB

The official PCB *(Flix2)* is in development now. Follow the [project's channel](https://t.me/opensourcequadcopter) to track the progress.

Outdoor flights demo video of the current prototype:

[![](https://camo.githubusercontent.com/4a6f9a37bb0a64e50db89702fe473bdcebce031014fd327307ade27ffd52ab56/68747470733a2f2f69332e7974696d672e636f6d2f76692f4b586c4e6d7655546934672f6d617872657364656661756c742e6a7067)](https://youtu.be/KXlNmvUTi4g)

## Simulation

The simulator is implemented using Gazebo and runs the original Arduino code:

[![Flix simulator](https://github.com/okalachev/flix/raw/master/docs/img/simulator1.png)](https://github.com/okalachev/flix/blob/master/docs/img/simulator1.png)

## Documentation articles

1. [Assembly instructions](https://github.com/okalachev/flix/blob/master/docs/assembly.md).
2. [Usage: build, setup and flight](https://github.com/okalachev/flix/blob/master/docs/usage.md).
3. [Simulation](https://github.com/okalachev/flix/blob/master/gazebo/README.md).
4. [Python library](https://github.com/okalachev/flix/blob/master/tools/pyflix/README.md).

Additional articles:

- [User builds gallery](https://github.com/okalachev/flix/blob/master/docs/user.md).
- [Firmware architectural overview](https://github.com/okalachev/flix/blob/master/docs/firmware.md).
- [Troubleshooting](https://github.com/okalachev/flix/blob/master/docs/troubleshooting.md).
- [Log analysis](https://github.com/okalachev/flix/blob/master/docs/log.md).

## Components

| Type                                                       | Part                                                                                                                                                                                                                                                       | Image                                                                                                                                                                                                                                                                                                                                                                                                                                    | Quantity |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Microcontroller board                                      | ESP32 Mini.   ESP32-S3/ESP32-C3 boards are also supported.                                                                                                                                                                                                 | [![](https://github.com/okalachev/flix/raw/master/docs/img/esp32.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/esp32.jpg)                                                                                                                                                                                                                                                                                                 | 1        |
| IMU (and barometer¹) board                                 | GY‑91, MPU-9265 (or other MPU‑9250/MPU‑6500 board)   ICM20948V2 (ICM‑20948)   GY-521 (MPU-6050)                                                                                                                                                            | [![](https://github.com/okalachev/flix/raw/master/docs/img/gy-91.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/gy-91.jpg)   [![](https://github.com/okalachev/flix/raw/master/docs/img/icm-20948.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/icm-20948.jpg)   [![](https://github.com/okalachev/flix/raw/master/docs/img/gy-521.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/gy-521.jpg) | 1        |
| *Boost converter (optional, for more stable power supply)* | *5V output*                                                                                                                                                                                                                                                | [![](https://github.com/okalachev/flix/raw/master/docs/img/buck-boost.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/buck-boost.jpg)                                                                                                                                                                                                                                                                                       | 1        |
| Motor                                                      | 8520 3.7V brushed motor.   Motor with exact 3.7V voltage is needed, not ranged working voltage (3.7V — 6V).   Make sure the motor shaft diameter and propeller hole diameter match!                                                                        | [![](https://github.com/okalachev/flix/raw/master/docs/img/motor.jpeg)](https://github.com/okalachev/flix/blob/master/docs/img/motor.jpeg)                                                                                                                                                                                                                                                                                               | 4        |
| Propeller                                                  | 55 mm or 65 mm                                                                                                                                                                                                                                             | [![](https://github.com/okalachev/flix/raw/master/docs/img/prop.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/prop.jpg)                                                                                                                                                                                                                                                                                                   | 4        |
| MOSFET (transistor)                                        | 100N03A or [analog](https://t.me/opensourcequadcopter/33)                                                                                                                                                                                                  | [![](https://github.com/okalachev/flix/raw/master/docs/img/100n03a.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/100n03a.jpg)                                                                                                                                                                                                                                                                                             | 4        |
| Pull-down resistor   Voltage measurement resistor          | 10 kΩ                                                                                                                                                                                                                                                      | [![](https://github.com/okalachev/flix/raw/master/docs/img/resistor10k.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/resistor10k.jpg)                                                                                                                                                                                                                                                                                     | 6        |
| 3.7V Li-Po battery                                         | LW 952540 (or any compatible by the size).   Make sure the battery has enough discharge rate — 25C or more!                                                                                                                                                | [![](https://github.com/okalachev/flix/raw/master/docs/img/battery.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/battery.jpg)                                                                                                                                                                                                                                                                                             | 1        |
| Battery connector cable                                    | MX2.0 2P female                                                                                                                                                                                                                                            | [![](https://github.com/okalachev/flix/raw/master/docs/img/mx.png)](https://github.com/okalachev/flix/blob/master/docs/img/mx.png)                                                                                                                                                                                                                                                                                                       | 1        |
| Li-Po Battery charger                                      | Any                                                                                                                                                                                                                                                        | [![](https://github.com/okalachev/flix/raw/master/docs/img/charger.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/charger.jpg)                                                                                                                                                                                                                                                                                             | 1        |
| Screws for IMU board mounting                              | M3x5                                                                                                                                                                                                                                                       | [![](https://github.com/okalachev/flix/raw/master/docs/img/screw-m3.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/screw-m3.jpg)                                                                                                                                                                                                                                                                                           | 2        |
| Screws for frame assembly                                  | M1.4x5                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                          | 4        |
| Frame main part                                            | 3D printed²: [`stl`](https://github.com/okalachev/flix/blob/master/docs/assets/flix-frame-1.1.stl) [`step`](https://github.com/okalachev/flix/blob/master/docs/assets/flix-frame-1.1.step)   Recommended settings: layer 0.2 mm, line 0.4 mm, infill 100%. | [![](https://github.com/okalachev/flix/raw/master/docs/img/frame1.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/frame1.jpg)                                                                                                                                                                                                                                                                                               | 1        |
| Frame top part                                             | 3D printed: [`stl`](https://github.com/okalachev/flix/blob/master/docs/assets/esp32-holder.stl) [`step`](https://github.com/okalachev/flix/blob/master/docs/assets/esp32-holder.step)                                                                      | [![](https://github.com/okalachev/flix/raw/master/docs/img/esp32-holder.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/esp32-holder.jpg)                                                                                                                                                                                                                                                                                   | 1        |
| Washer for IMU board mounting                              | 3D printed: [`stl`](https://github.com/okalachev/flix/blob/master/docs/assets/washer-m3.stl) [`step`](https://github.com/okalachev/flix/blob/master/docs/assets/washer-m3.step)                                                                            | [![](https://github.com/okalachev/flix/raw/master/docs/img/washer-m3.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/washer-m3.jpg)                                                                                                                                                                                                                                                                                         | 2        |
| Controller (recommended)                                   | CC2500 transmitter, like BetaFPV LiteRadio CC2500 (RC receiver/Wi-Fi).   Two-sticks gamepad (Wi-Fi only) — see [recommended gamepads](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/setup_view/joystick.html#supported-joysticks).   Other⁵     | [![](https://github.com/okalachev/flix/raw/master/docs/img/betafpv.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/betafpv.jpg) [![](https://github.com/okalachev/flix/raw/master/docs/img/logitech.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/logitech.jpg)                                                                                                                                              | 1        |
| *RC receiver (optional)*                                   | *DF500 or other³*                                                                                                                                                                                                                                          | [![](https://github.com/okalachev/flix/raw/master/docs/img/rx.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/rx.jpg)                                                                                                                                                                                                                                                                                                       | 1        |
| Wires                                                      | 28 AWG recommended                                                                                                                                                                                                                                         | [![](https://github.com/okalachev/flix/raw/master/docs/img/wire-28awg.jpg)](https://github.com/okalachev/flix/blob/master/docs/img/wire-28awg.jpg)                                                                                                                                                                                                                                                                                       |          |
| Tape, double-sided tape                                    |                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                          |          |

*¹ — barometer is not used for now.*  
*² — this frame is optimized for GY-91 board, if using other, the board mount holes positions should be modified.*  
*³ — you also may use any transmitter-receiver pair with SBUS interface.*

Tools required for assembly:

- 3D printer.
- Soldering iron.
- Solder wire (with flux).
- Screwdrivers.
- Multimeter.

Feel free to modify the design and or code, and create your own improved versions. Send your results to the [official Telegram chat](https://t.me/opensourcequadcopterchat), or directly to the author ([E-mail](mailto:okalachev@gmail.com), [Telegram](https://t.me/okalachev)).

## Schematics

### Simplified connection diagram

[![Flix version 1 schematics](https://github.com/okalachev/flix/raw/master/docs/img/schematics1.svg)](https://github.com/okalachev/flix/blob/master/docs/img/schematics1.svg)

*(Dashed elements are optional).*

Motor connection scheme:

[![MOSFET connection scheme](https://github.com/okalachev/flix/raw/master/docs/img/mosfet-connection.png)](https://github.com/okalachev/flix/blob/master/docs/img/mosfet-connection.png)

You can see a user-contributed [variant of complete circuit diagram](https://miro.com/app/board/uXjVN-dTjoo=/?moveToWidget=3458764612338222067&cot=14) of the drone.

### Notes

- Power ESP32 Mini with Li-Po battery using VCC (+) and GND (-) pins.
- Connect the IMU board to the ESP32 Mini using VSPI, power it using 3.3V and GND pins:
	| IMU pin | ESP32 pin |
	| --- | --- |
	| GND | GND |
	| 3.3V | 3.3V |
	| SCL *(SCK)* | SVP (GPIO18) |
	| SDA *(MOSI)* | GPIO23 |
	| SAO *(MISO)* | GPIO19 |
	| NCS | GPIO5 |
- Solder pull-down resistors to the MOSFETs.
- Connect the motors to the ESP32 Mini using MOSFETs, by following scheme:
	| Motor | Position | Direction | Prop type | Motor wires | GPIO |
	| --- | --- | --- | --- | --- | --- |
	| Motor 0 | Rear left | Counter-clockwise | B | Black & White | GPIO12 *(TDI)* |
	| Motor 1 | Rear right | Clockwise | A | Blue & Red | GPIO13 *(TCK)* |
	| Motor 2 | Front right | Counter-clockwise | B | Black & White | GPIO14 *(TMS)* |
	| Motor 3 | Front left | Clockwise | A | Blue & Red | GPIO15 *(TD0)* |
	Clockwise motors have blue & red wires and correspond to propeller type A (marked on the propeller). Counter-clockwise motors have black & white wires correspond to propeller type B.
- Optionally connect the RC receiver to the ESP32's UART2:
	| Receiver pin | ESP32 pin |
	| --- | --- |
	| GND | GND |
	| VIN | VCC (or 3.3V depending on the receiver) |
	| Signal (TX) | GPIO4 |
- Optionally connect the battery voltage divider for voltage monitoring to any ADC1 pin (e. g. *GPIO32* on ESP32, *GPIO3* on ESP32-S3).
	ESP32 and ESP32-S3 [can measure](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/adc.html#analogsetattenuation) up to 3.1 V and ESP32-S3/ESP32-C3 can measure up to 2.5 V, so choose the voltage divider resistors accordingly.

## Resources

- Telegram channel on developing the drone and the flight controller (in Russian): [https://t.me/opensourcequadcopter](https://t.me/opensourcequadcopter).
- Official Telegram chat: [https://t.me/opensourcequadcopterchat](https://t.me/opensourcequadcopterchat) (English / Russian).
- Detailed article on Habr.com about the development of the drone (in Russian): [https://habr.com/ru/articles/814127/](https://habr.com/ru/articles/814127/).

## Disclaimer

This is a DIY project, and I hope you find it interesting and useful. However, it's not easy to assemble and set up, and it's provided "as is" without any warranties. There's no guarantee that it will work perfectly, or even work at all.

⚠️

The author is not responsible for any damage, injury, or loss resulting from the use of this project. Use at your own risk!