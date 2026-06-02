---
title: "MiniKame Quadruped Robot - A Desktop Robot Building Tutorial from Scratch"
source: "https://projecthub.arduino.cc/aplux/minikame-quadruped-robot-a-desktop-robot-building-tutorial-from-scratch-439e7e"
author:
published:
created: 2026-05-31
description: "This project is featured in the Robotics Hub.This document is a complete tutorial for building a MiniKame quadruped robot from scratch, designed to help robotics enthusiasts, university students, and maker educators create their own desktop quadruped robot. The tutorial covers everything from design philosophy, hardware assembly, principle analysis to software programming, with both easy-to-understand explanations and in-depth mathematical derivations."
tags:
  - "clippings"
---
## This project is featured in the Robotics Hub.This document is a complete tutorial for building a MiniKame quadruped robot from scratch, designed to help robotics enthusiasts, university students, and maker educators create their own desktop quadruped robot. The tutorial covers everything from design philosophy, hardware assembly, principle analysis to software programming, with both easy-to-understand explanations and in-depth mathematical derivations.

•

17093 views

•

11 respects

•

Apache-2.0

[Robots](#)

[Audio](#)

Devices & Components

1

![](https://cdn.shopify.com/s/files/1/0438/4735/2471/files/ABX00173_00.front.jpg?v=1768837006)

Arduino® UNO™ Q 4GB

Software & Tools

Arduino App Lab

Project description

![](https://www.youtube.com/watch?v=a0tMchg5zXc)

### Part 1: Getting to Know MiniKame

**1.1 What is MiniKame?**

MiniKame is an 8-degree-of-freedom (8-DOF) miniature quadruped robot based on the Arduino UNO Q (with built-in WiFi). The name "Kame" comes from the Japanese word "亀" (turtle), symbolizing stability and vitality like a turtle. This robot's design is inspired by classic spider robot forms, but with a more compact and cute appearance, perfect for desktop demonstrations and experiments.

![kame_robot](https://projects.arduinocontent.cc/d3bfd036-1230-4481-9c46-3659cc10b790.jpg)

kame\_robot

**Analogy** : If we compare the robot to a small animal:

1. **Arduino** is its brain, responsible for thinking and processing information
2. **8 servos** are its muscles, enabling movement
3. **WiFi module** is its senses, receiving external commands
4. **Battery** is its energy source, providing power

**Core Specifications:**

1. **Dimensions** : 150mm length × 120mm width × 100mm height (slightly larger than an adult's palm)
2. **Weight** : Approximately 300g (about the weight of an apple)
3. **DOF** : 8 (each leg has 2 joints, like human thighs and calves)
4. **Control Core** : Arduino UNO Q (with built-in WiFi)
5. **Actuation** : 8 35Kg.cm servos
6. **Power** : 12V Lithium battery
7. **Control Method** : Browser Web Interface (mobile/computer both available)

**1.2 Design Philosophy: Simple but Not Simplistic**

Unlike many complex quadruped robot projects, MiniKame's design philosophy is " **simple but not simplistic** ". It doesn't rely on expensive sensors or complex control algorithms, but instead uses an elegant mathematical model—the sine oscillator—to simulate the biological Central Pattern Generator (CPG), achieving natural and fluid movement.

**What is CPG?** Imagine when you walk, you don't consciously think "lift left foot, then step with right foot..."—these actions are automatically completed by your spinal cord. This neural system that automatically generates rhythmic movements is the CPG. MiniKame uses mathematical formulas to simulate this mechanism.

**Three-Layer Separation Architecture:**

`   	Web Frontend (Browser) ←→ Python Middleware ←→ Arduino Firmware                        ` `   	  (HTML/CSS/JS)          (Command Routing)      (Servo Control)                        `

This architecture is like a restaurant:

1. **Web Frontend** is the menu and ordering interface (what customers see and operate)
2. **Python Middleware** is the waiter (receiving orders, conveying to kitchen)
3. **Arduino Firmware** is the chef (actually preparing the dishes)

Advantages of this architecture:

1. **Human-Machine Separation** : Control interface decoupled from underlying hardware, like the menu being separate from the kitchen
2. **Cross-Platform** : Any device with a browser can control, like any customer can view the menu
3. **Real-Time** : Socket.IO enables bidirectional communication, like a waiter keeping customers updated on order status
4. **Easy to Extend** : New features can be added without affecting the bottom layer, like adding new dishes to the menu without redesigning the kitchen

**1.3 Application Scenarios**

1. **Robotics Enthusiast Entry Project** : Learn servo control, gait generation principles, experience the complete building process
2. **University Course Projects/Graduation Designs** : Can serve as practical projects for mechatronics, embedded systems, web control courses
3. **ROS/AI Frontend Platform** : Can add sensors for obstacle avoidance, line following, or target tracking
4. **Maker Education/STEAM Teaching** : As a demonstration project to stimulate students' interest in robotics technology
5. **Remote Laboratory** : Control physical robots remotely through web interface

**1.4 Project Features**

1. **Pure Mathematics-Driven Motion Control** : No reliance on complex sensor feedback, generates natural gaits through sine oscillators
2. **Parametric Design** : All actions defined by four parameters: amplitude, period, phase, offset
3. **Rich Action Library** : 11 preset actions (walk, turn, dance, moonwalk, etc.)
4. **Web Remote Control** : Control through browser, no app installation required
5. **Real-Time Parameter Adjustment** : Steps (1-20) and speed (200-3000ms) sliders for real-time adjustment
6. **Cyberpunk UI** : Dark theme responsive interface, adaptive for mobile portrait mode
7. **Complete Calibration Mechanism** : Compensate mechanical assembly errors through trim and reverse parameters

### Part 2: Mechanical Structure Design

![Image](https://projects.arduinocontent.cc/7974bb37-a3db-4d7c-84ce-eece43b93f88.gif) [Previous](#) [Next](#)

**2.1 Leg Joint Design**

MiniKame uses a typical quadruped robot leg structure, with each leg consisting of two joints, totaling 8 degrees of freedom. We can imagine each leg like a human leg:

![](https://projects.arduinocontent.cc/5d679810-e88d-4a8f-a3d2-392e88216cee.png)

**2.1.1 Biological Insights in Joint Configuration**

Observing four-legged animals in nature, their leg structures follow a common principle: **thighs generate forward power, calves adjust ground clearance.**

**Real-life Examples:**

1. Thigh (Hip Joint): Like rowing a boat, arms swinging back and forth generate forward momentum
2. Calf (Knee Joint): Like lifting your foot when stepping over a threshold to avoid tripping

**2.1.2 Unified Coordinate System Convention**

For easy programming and control, we uniformly stipulate:

1. **Increasing thigh angle → Leg swings forward**
2. **Decreasing thigh angle → Leg swings backward**
3. **Increasing calf angle → Leg lowers (body lowers)**
4. **Decreasing calf angle → Leg lifts (body raises)**
`   **	Analogy                  **   ``   : This is like agreeing that "nodding" means "yes" and "shaking head" means "no". If someone (a servo) is installed backwards and nodding becomes shaking head, we need a "translator"—this is what the reverse[] array does later.                     `![](https://projects.arduinocontent.cc/25df53f9-8fc4-4b68-b0af-e4bbeaa091ac.jpg)

**2.2 Complete Assembly Guide**

**Assembly Steps Overview:**

**Step 1** : Servo Initialization Before installation, all servos need to be set to 90 degrees (neutral position). This is like setting all clock hands to 12 o'clock before installation.

`   	// Servo zeroing test program                    ` `   #include <Servo.h>                    ` `   Servo testServo;                    ``   int servoPins[] = {4,5,6,7,8,9,10,11};                    ``   void setup() {                    ` `   	   for(int i=0; i<8; i++) {                    ` `   	       testServo.attach(servoPins[i]);                    ``   	       testServo.write(90);                    ``   	       delay(500);  // Give servo time to reach 90 degrees                    ` `   	   }                    ` `   }                    ` `   void loop() {                    ` `   	   // Stay still                    ` `   }                    ` ![](https://projects.arduinocontent.cc/85e0f2b1-bff8-4def-aa3e-3f8a5b430748.jpg) ![](https://projects.arduinocontent.cc/53aa5f47-00d7-4659-af5e-40aa17e8e012.jpg)

**Why zero before installation?** If servos aren't zeroed before installing mechanical parts, it's like installing clock hands when they're not at 12 o'clock—all times will be wrong. This can lead to:

1. Asymmetrical leg positions after installation
2. Servos stressed at extreme positions, potentially damaging gears
3. Extremely difficult calibration

**Step 2** : **Body Frame Assembly** The body frame consists of upper and lower 3D printed plates connected, housing the Arduino board and battery in between. Servos are mounted on both sides of the body, connected to leg components through U-shaped brackets.

**Step 3** : Leg Assembly Each leg consists of two servos (thigh and calf) and two 3D printed connecting rods. Assembly notes:

1. Servo mounting direction must correspond to the reverse\[\] settings in code
2. Connecting rod length directly affects movement range
3. All screws should be tightened firmly but not excessively, avoiding damage to plastic parts

### Part 3: Hardware System Design

**3.1 Core Hardware List**

![](https://projects.arduinocontent.cc/deaa3d76-d7b6-423b-ab2f-9baf8067ac87.png)

![Image](https://projects.arduinocontent.cc/6ff73340-c100-42af-a99e-b95875253447.jpg) [Previous](#) [Next](#)

**3.2 Power System Design**

**3.2.1 Power Requirements Analysis**

MiniKame's power system needs to meet two requirements simultaneously:

**Servo Power** Supply: When 8 servos work simultaneously, current requirements are:

1. Idle current: ~10mA each, total 80mA (equivalent to a small LED)
2. Normal operation: 100-200mA each, total 0.8-1.6A (equivalent to charging a phone)
3. Stall peak: up to 500-800mA each, total 4-6.4A (equivalent to a hair dryer!)

**Main Controller Power** : Arduino UNO Q requires 5V or 7-12V input, current ~50mA (equivalent to a small light bulb)

**3.2.2 Power Solution Comparison**

![](https://projects.arduinocontent.cc/b4edde40-e681-4e27-a0c3-87fb0f7e4cbf.png)

**Recommended Solution** : Use 12V lithium battery, step down to 5V via voltage regulator module for servos, while also supplying Arduino's Vin pin directly.

**3.2.3 Key Power Design Points**

1\. Current Capability: Servos draw high current at startup, like a car consuming most fuel when starting. Power supply needs to provide peak current above 3A.

2\. Voltage Regulation Accuracy: Voltage fluctuation shouldn't exceed ±0.3V, otherwise servos may jitter. This is like people feeling dizzy with unstable blood pressure.

3\. Filter Capacitor: Connect a large capacitor (1000μF+) in parallel at servo power input to absorb transient currents. This is like adding a large water tank to a water system—when a large amount of water is suddenly needed, the tank provides buffer.

4\. Power Separation: It's recommended to separate servo power and Arduino power:

1. Servos: 12V battery + 5V step-down module
2. Arduino: Take power from servo supply (if step-down module has sufficient capacity)

**3.3 Circuit Connection Diagram**

**3.3.1 Servo Pin Assignment**

![](https://projects.arduinocontent.cc/96b8d5cf-f0f8-4260-b902-294b7061f9a9.png)

**3.3.2 Power Connection**

`   	12V Lithium Battery (+) ──┬── Step-down Module Input(+) ── Step-down Output(5V) ──┬── Servo VCC Bus                 ` `   	                         │                                                       │                 ` `   	                         └── Arduino Vin                                          └── Servo GND Bus                 ` `   	                                                                                        │                 ` `   12V Lithium Battery (-) ──┴── Step-down Module Input(-) ── Step-down Output(GND) ──┴── Arduino GND                 `

**3.3.3 Key Considerations**

1. **Common Ground** : All power GND must be connected together, otherwise control signals can't form a complete circuit. This is like two people needing a common language to communicate.
2. **Signal Wires** : Servo signal wires connect directly to Arduino digital pins, no pull-up resistors needed.
3. **Large Capacitor** : Connect 1000μF electrolytic capacitor between servo power positive and negative (positive to VCC, negative to GND).
4. **Wire Gauge** : Servo power wires should use 22AWG or thicker, like thicker pipes allowing more water flow.

### Part 4: From Biological Inspiration to Mathematical Modeling

**4.1 Biological Central Pattern Generator (CPG)**

In nature, quadruped walking appears simple but is extremely complex. When we watch a cat strolling leisurely, its four legs coordinate so naturally and smoothly.

**An Interesting Experiment** : Scientists discovered that even when cutting spinal cord connection to the brain, animals can still produce rhythmic walking movements. This shows that basic walking patterns aren't directly controlled by the brain, but autonomously generated by a neural circuit in the spinal cord—the Central Pattern Generator (CPG).

**Simple Analogy for CPG:**

1. CPG is like an automatic metronome that keeps beat without a conductor
2. The brain just needs to say "start walking" or "walk faster," and CPG automatically coordinates all limbs
3. This is why we can think about other things while walking, without consciously controlling each step

CPG characteristics:

1. Autonomous Rhythmicity: Generates periodic signals without external input
2. Adjustability: Frequency and amplitude can be changed with simple commands
3. Coordination: Multiple CPGs coordinate through phase coupling

**4.2 Mathematical Model Construction**

MiniKame's design philosophy is to use mathematical models to simulate biological CPG working principles. We use a **sine oscillator network** to let the robot autonomously generate rhythmic movements.

**What is a Sine Wave?** Imagine swinging on a swing:

1. From the highest point to the lowest, then to the highest on the other side—this is one period
2. The higher you swing, the larger the amplitude
3. The faster you swing, the shorter the period
4. Two swings swinging together, one ahead of the other—this is phase difference
5. The lowest point might not be exactly in the middle—this is offset

**4.2.1 Mathematical Definition of a Single Oscillator**

A sine oscillator's output can be expressed as:

`   	output(t) = A × sin(2π × t / T + φ) + O               `

Let's explain each parameter with real-life examples:

1. **A (Amplitude)** : Like how high the swing goes. Larger A means larger leg swing range, longer stride.
2. **T (Period)** : Like how long one complete swing cycle takes. Smaller T means faster movement; larger T means slower movement.
3. **φ (Phase)** : Like the start time difference between two swings. If two swings start simultaneously, phase difference is 0°; if one starts while the other is already mid-swing, there's phase difference.
4. **O (Offset)** : Like the swing's pivot point might not be exactly centered. Offset determines the leg's resting position.

**4.2.2 Oscillator Network Coupling**

8 oscillators couple through phase relationships, forming a CPG network:

`   	Leg1: output₁(t) = A₁ × sin(ωt + φ₁) + O₁               ` `   Leg2: output₂(t) = A₂ × sin(ωt + φ₂) + O₂               ``   ...               ``   Leg8: output₈(t) = A₈ × sin(ωt + φ₈) + O₈               `

These oscillators share the same angular frequency ω (determined by period T), but coordinate through phase φ. This is like an orchestra:

1. All musicians play at the same rhythm (ω)
2. But different instruments enter at different times (φ)
3. Some instruments are louder (larger A), some softer (smaller A)
4. Some instruments have higher pitch (larger O), some lower (smaller O)

**4.3 From Model to Code Mapping**

Now let's see how this mathematical model is implemented in code.

**4.3.1 Oscillator Class Implementation**

The Oscillator class defined in Octosnake.h:

`   class Oscillator{               ` `   private:               ``   	   int _period;          // Period T: time for one complete oscillation (milliseconds)               ` `   	   int _amplitude;       // Amplitude A: swing range (degrees)               ` `   	   int _phase;           // Phase φ: starting position in the period (degrees)               ` `   	   int _offset;          // Offset O: movement center point (degrees)               ` `   	   float _output;        // Currently calculated angle               ` `   	   bool _stop;           // Stop flag               ` `   	   unsigned long _ref_time; // Reference time: when oscillator started               ` `   	   float _delta_time;    // Current time offset from reference               ` `   public:               ``   	   float refresh();      // Calculate current output               ` `   	   void setPeriod(int period);               ``   	   void setAmplitude(int amplitude);               ``   	   void setPhase(int phase);               ``   	   void setOffset(int offset);               ``   	   // ... other methods               ` `   };               `

Each member variable directly corresponds to a parameter in the mathematical model, implementing clear mapping from math to code.

**4.3.2 refresh() Function Mathematical Implementation**

`   float Oscillator::refresh(){               ` `   	   if (!_stop){               ` `   	       // Calculate current position in the period (0 to T-1)               ` `   	       _delta_time = (millis() - _ref_time) % _period;               ``   	       // Sine wave formula:               ``   	       // output = A * sin(2π * t/T + φ) + O               ` `   	       _output = (float)_amplitude *                ` `   	                 sin(time_to_radians(_delta_time) +                ` `   	                     degrees_to_radians(_phase)) +                ` `   	                 _offset;               ``   	   }               ` `   	   return _output;               ``   }               `

**Line-by-line explanation with real-life analogies:**

**if (!\_stop)** : Only calculate when oscillator is active, like only paying attention to the swing's position when it's actually swinging.

(millis() - \_ref\_time) % \_period:

1. millis() is current time
2. \_ref\_time is when swinging started
3. Difference is how long we've been swinging
4. Modulo period means "no matter how many cycles completed, we only care where we are in the current cycle"

**time\_to\_radians(...)** : Convert time to radians. Why radians? Because trigonometric functions in math use radians, like thermometers using Celsius.

**degrees\_to\_radians(\_phase)** : Convert phase from degrees to radians.

**Sine wave calculation** : This is the swing's motion formula; the computer calculates where the swing should be at this moment.

**4.4 Physical Meaning of Four Core Parameters**

**4.4.1 Amplitude A — Determines Movement Range**

**Mathematical Definition** : Amplitude is the maximum deviation of a sine wave, determining vertical stretch degree.

**Physical Meaning** : In robot motion, amplitude determines the servo's maximum swing angle. Larger amplitude means:

1. Larger thigh amplitude → longer stride, faster forward speed
2. Larger calf amplitude → higher leg lift, less ground friction

Analogy: Like walking—striding with large leg swings (large amplitude) vs. small steps with small swings (small amplitude).

**Code Representation:**

`   **	int x_amp = 15;  // Thigh swings 15 degrees          **   ` `   **int z_amp = 20;  // Calf lifts 20 degrees          **   `

**4.4.2 Period T — Determines Movement Speed**

**Mathematical Definition** : Period is time for one complete oscillation, determining waveform compression/expansion on the time axis.

**Physical Meaning** : Period determines the robot's movement rhythm. Shorter period = faster movement; longer period = slower movement.

**Analogy** : Like music—allegro (short period) vs. adagio (long period).

**Code Representation:**

`   	int period[] = {T, T, T/2, T/2, T, T, T/2, T/2};             `

Here's an interesting detail: calf period is half of thigh period. This means calves move twice as fast as thighs. Why? Because lifting needs to be quick (fast lift to avoid ground drag), while forward/backward swinging can be relatively slower.

**4.4.3 Phase φ — Determines Movement Coordination**

**Mathematical Definition** : Phase represents the sine wave's time-axis offset, determining waveform starting position.

**Physical Meaning** : Phase is the most critical parameter in gait generation. It describes time offset relationships between multiple oscillators.

Analogy:

1. If four legs are dancers, phase is the choreography determining when each jumps and lands
2. If all dancers jump simultaneously, phase difference is 0°
3. If they jump sequentially like a wave, there are different phase differences

**Code Representation:**

`   int phase[] = {90, 90, 270, 90, 270, 270, 90, 270};             `

**Important Phase Relationships:**

1. **0° difference** : Movements completely synchronized
2. **90° difference** : One peaks while the other crosses zero
3. **180° difference** : Movements completely opposite (one forward while other backward)

**4.4.4 Offset O — Determines Neutral Position**

**Mathematical Definition** : Offset is vertical translation of the entire waveform, determining the sine wave's center line.

**Physical Meaning** : Offset determines the servo's resting position. In home(), different legs have different offsets because the robot's body needs to stay level while leg installation angles naturally vary.

**Analogy** : Like chair legs on uneven ground—you need to put shims under shorter legs (offset) to keep the chair balanced.

**Code Representation:**

`   	int offset[] = {            ` `   	   90 + ap - front_x,  // Left front thigh: needs more forward extension            ` `   	   90 - ap + front_x,  // Right front thigh: also needs forward extension            ` `   	   90 - hi,            // Left front calf: needs lifting            ` `   	   90 + hi,            // Right front calf: needs lowering            ` `   	   // ...            ``   };            `

### Part 5: Firmware Detailed Explanation

**5.1 MiniKame Class Architecture**

`   	class MiniKame{            ` `   private:            ``   	   Oscillator oscillator[8];  // 8 oscillator instances            ` `   	   Servo servo[8];            // 8 servo objects            ` `   	   int board_pins[8];         // Servo pin mapping            ` `   	   int trim[8];               // Calibration values, compensating mechanical errors            ` `   	   bool reverse[8];           // Direction reversal flags            ` `   	   unsigned long _init_time;  // Initialization timestamp            ` `   	   unsigned long _final_time; // End timestamp            ` `   	   float _servo_position[8];  // Current servo position record            ` `   public:            ``   	   void init();            ``   	   void walk(float steps, int period);            ``   	   void turnL(float steps, int period);            ``   	   void turnR(float steps, int period);            ``   	   void dance(float steps, int period);            ``   	   void moonwalkL(float steps, int period);            ``   	   void pushUp(float steps, int period);            ``   	   void hello();            ``   	   void home();            ``   	   void zero();            ``   	   // ... other methods            ` `   };            `

**Roles of Each Class Component:**

1. **oscillator\[8\]** : 8 mathematical calculators, each responsible for calculating where one leg should be
2. **servo\[8\]** : 8 physical actuators, each controlling one servo
3. **board\_pins\[8\]** : Wiring map, telling the program which pin each servo connects to
4. **trim\[8\]** : Fine-tuning knobs, compensating assembly errors
5. **reverse\[8\]** : Direction conversion switches, solving servo orientation issues

**5.2 Initialization Function init()**

`   **void MiniKame::init() {         **   ` `   **	   // 1. Configure pin mapping (telling program where each servo connects)         **   ` `   **	   board_pins[0] = 4;  // Left front thigh connected to D4         **   ` `   **	   board_pins[1] = 5;  // Right front thigh connected to D5         **   ` `   **	   board_pins[2] = 6;  // Left front calf connected to D6         **   ` `   **	   board_pins[3] = 7;  // Right front calf connected to D7         **   ` `   **	   board_pins[4] = 8;  // Left rear thigh connected to D8         **   ` `   **	   board_pins[5] = 9;  // Right rear thigh connected to D9         **   ` `   **	   board_pins[6] = 10; // Left rear calf connected to D10         **   ` `   **	   board_pins[7] = 11; // Right rear calf connected to D11         **   ` `   **	   // 2. Set calibration values (adjust based on actual assembly)         **   ` `   **	   trim[0] = -5;    // Left front thigh needs -5° counterclockwise adjustment         **   ` `   **	   trim[1] = -5;    // Right front thigh needs -5° counterclockwise adjustment         **   ` `   **	   trim[2] = -20;   // Left front calf needs -20° counterclockwise adjustment         **   ` `   **	   trim[3] = 10;    // Right front calf needs +10° clockwise adjustment         **   ` `   **	   trim[4] = -3;    // Left rear thigh needs -3° counterclockwise adjustment         **   ` `   **	   trim[5] = -3;    // Right rear thigh needs -3° counterclockwise adjustment         **   ` `   **	   trim[6] = -15;   // Left rear calf needs -15° counterclockwise adjustment         **   ` `   **	   trim[7] = -13;   // Right rear calf needs -13° counterclockwise adjustment         **   ` `   **	   // 3. Default no direction reversal         **   ` `   **	   for (int i = 0; i < 8; i++) reverse[i] = false;         **   ``   **	   // 4. Start oscillators, attach servos         **   ` `   **	   for (int i = 0; i < 8; i++) {         **   ` `   **	       oscillator[i].start();        // Start mathematical calculators         **   ` `   **	       servo[i].attach(board_pins[i]); // Connect physical servos         **   ` `   **	       delay(50);  // Connect one by one to avoid current surge         **   ` `   **	   }         **   ` `   **	   // 5. Initial position zeroing         **   ` `   **	   zero();         **   ``   **}         **   `

**Initialization Sequence Logic:**

1. **Configure mapping first** : Ensure physical connections match code (like confirming sockets are plugged correctly)
2. **Set calibration values** : Prepare for subsequent movement (like tuning instruments first)
3. **Start one by one** : Avoid current surge from starting all 8 servos simultaneously (like not turning on all appliances at once)
4. **Zero last** : Ensure robot initial posture determined (like setting pointers to zero first)

**5.3 Servo Control Bottom Layer Implementation**

`   void MiniKame::setServo(int id, float target) {            ` `   	   float final_angle = target + trim[id];  // First add calibration value            ` `   	   if (reverse[id]) {            ` `   	       // If reversal needed, subtract target angle from 180 degrees            ` `   	       final_angle = 180 - final_angle;            ``   	   }            ` `   	   // Convert angle to pulse width, send to servo            ` `   	   servo[id].writeMicroseconds(angToUsec(final_angle));            ``   	   // Record current position            ` `   	   _servo_position[id] = target;            ``   }            ` `   int MiniKame::angToUsec(float value) {            ` `   	   // Linear mapping: 0° -> 544μs, 180° -> 2400μs            ` `   	   // Like temperature: 0°C corresponds to 32°F, 100°C to 212°F            ` `   	   return value / 180 * (MAX_PULSE_WIDTH - MIN_PULSE_WIDTH) + MIN_PULSE_WIDTH;            ``   }            `

**The Elegance of This Function:**

**Calibration Value Addition** : Adding trim\[id\] before output is like putting small shims under each leg to compensate mechanical assembly errors

**Direction Handling** : Implementing reversal through 180 - angle

**Mathematical principle** : If original direction increases clockwise, reversal increases counterclockwise

1. Example: Original 90° stays 90°, 120° becomes 60°, implementing direction reversal
2. This is like a translator turning "nodding" into "shaking head"

**Angle to Pulse Width Conversion:** Servos don't understand "angles," only "how long the high level lasts." This function is like a translator, converting angles into a language servos understand.

**5.4 Unified Gait Execution Interface**

`   **void MiniKame::execute(float steps, int period[8], int amplitude[8],          **   ``   **	                      int offset[8], int phase[8]) {         **   ` `   **	   // Step 1: Configure 8 oscillators         **   ` `   **	   for (int i = 0; i < 8; i++) {         **   ` `   **	       oscillator[i].setPeriod(period[i]);         **   ``   **	       oscillator[i].setAmplitude(amplitude[i]);         **   ``   **	       oscillator[i].setPhase(phase[i]);         **   ``   **	       oscillator[i].setOffset(offset[i]);         **   ``   **	   }         **   ` `   **	   // Step 2: Synchronize all oscillator start times         **   ` `   **	   unsigned long global_time = millis();         **   ``   **	   for (int i = 0; i < 8; i++)          **   ` `   **	       oscillator[i].setTime(global_time);         **   ``   **	   // Step 3: Execute specified number of steps         **   ` `   **	   _final_time = millis() + period[0] * steps;         **   ``   **	   while (millis() < _final_time) {         **   ` `   **	       for (int i = 0; i < 8; i++) {         **   ` `   **	           setServo(i, oscillator[i].refresh());         **   ``   **	       }         **   ` `   **	       delay(1);  // Tiny delay to avoid too frequent refreshes         **   ` `   **	   }         **   ` `   **}         **   `

**Three Key Steps of This Function:**

1. **Configure Parameters** : Like giving each musician sheet music, telling them how to play
2. **Synchronize Time** : This is crucial! All oscillators use the same global\_time as reference, ensuring they start simultaneously. Like a conductor's downbeat, all musicians start playing together.
3. **Loop Execution:** Continuously calculate new positions and update servos until specified steps completed. Like musicians continuously playing according to the score until the piece ends.

**5.5 Main Program and Bridge Communication**

sketch.ino is Arduino's main program, responsible for receiving commands from Python middleware and executing corresponding actions:

`   **#include "Arduino_RouterBridge.h"         **   ` `   **#include <Servo.h>         **   ` `   **#include "minikame.h"         **   ` `   **MiniKame robot;         **   ``   **// Command queue         **   ` `   **volatile int pending_cmd = 0;   // 0 = no command         **   ` `   **volatile int cmd_steps = 5;     // Default steps         **   ` `   **volatile int cmd_period = 800;  // Default period (ms)         **   ` `   **void setup() {         **   ` `   **	   Serial.begin(9600);         **   ``   **	   pinMode(LED_BUILTIN, OUTPUT);         **   ``   **	   robot.init();         **   ``   **	   delay(1000);         **   ``   **	   robot.home();         **   ``   **	   delay(1000);         **   ``   **	   // Initialize Bridge, register callback functions         **   ` `   **	   Bridge.begin();         **   ``   **	   Bridge.provide("action",  set_action);         **   ``   **	   Bridge.provide("steps",   set_steps);         **   ``   **	   Bridge.provide("period",  set_period);         **   ``   **	   Serial.println("🤖 Kame Robot Ready!");         **   ``   **}         **   ` `   **void loop() {         **   ` `   **	   Bridge.update();  // Check for new commands         **   ` `   **	   if (pending_cmd != 0) {         **   ` `   **	       int cmd = pending_cmd;         **   ``   **	       pending_cmd = 0;         **   ``   **	       digitalWrite(LED_BUILTIN, LOW); // LED ON = executing         **   ` `   **	       // Execute corresponding action based on command ID         **   ` `   **	       switch (cmd) {         **   ` `   **	           case 1:  robot.walk(cmd_steps, cmd_period);      break;         **   ``   **	           case 3:  robot.turnL(cmd_steps, cmd_period);     break;         **   ``   **	           case 4:  robot.turnR(cmd_steps, cmd_period);     break;         **   ``   **	           case 5:  robot.moonwalkL(cmd_steps, cmd_period); break;         **   ``   **	           case 6:  robot.dance(cmd_steps, cmd_period);     break;         **   ``   **	           case 7:  robot.upDown(cmd_steps, cmd_period);    break;         **   ``   **	           case 8:  robot.pushUp(cmd_steps, cmd_period);    break;         **   ``   **	           case 9:  robot.hello();                          break;         **   ``   **	           case 11: robot.frontBack(cmd_steps, cmd_period); break;         **   ``   **	           case 12: robot.home();                           break;         **   ``   **	           case 13: robot.init();                           break;         **   ``   **	       }         **   ` `   **	       // Return home after action completion (except home and init)         **   ` `   **	       if (cmd != 12 && cmd != 13) {         **   ` `   **	           robot.home();         **   ``   **	       }         **   ` `   **	       digitalWrite(LED_BUILTIN, HIGH); // LED OFF = idle         **   ` `   **	   }         **   ` `   **	   delay(10);         **   ``   **}         **   ` `   **// Bridge callback functions         **   ` `   **void set_action(int action) { pending_cmd = action; }         **   ` `   **void set_steps(int steps)   { cmd_steps  = constrain(steps, 1, 20); }         **   ` `   **void set_period(int period)  { cmd_period = constrain(period, 200, 5000); }         **   `

**Code Analysis:**

1. **Bridge Communication** : Arduino\_RouterBridge library implements communication with Python middleware, like a mail carrier delivering letters
2. **Command Queue:** Using volatile variables ensures interrupt safety, like having a dedicated inbox
3. **Parameter Constraints:** Steps limited to 1-20, period limited to 200-5000ms, like safety rails preventing parameters from going out of reasonable range
4. **Automatic Return Home:** All actions (except home/init) automatically return home after execution, like taking a bow after performance
5. **LED Indicator:** LED on indicates action execution, like a "working" indicator light

**5.6 Action Mapping Table**

![](https://projects.arduinocontent.cc/6bde7e3c-329a-476f-9672-14709dc21d4c.png)

### Part 6: Python Middleware Detailed Explanation

Python middleware is the "bridge" of the entire system, receiving Socket.IO messages from the web frontend and converting them to Bridge commands for Arduino.

**Restaurant Analogy:**

1. **Web Frontend** is the menu and ordering interface (what customers see)
2. **Python Middleware** is the waiter (receiving orders, conveying to kitchen)
3. **Arduino Firmware** is the chef (actually preparing dishes)

**6.1 Overall Architecture**

`   Web Frontend (Socket.IO) → Python Middleware (main.py) → Bridge → Arduino Firmware           ` `   	       ↑                       ↓                          ↓           ` `   	       └──────────────── Status Feedback ────────────────┘           `

**6.2 main.py Complete Code Analysis**

`   # main.py: Python Middleware Server           ` `   from arduino.app_utils import App, Bridge           ` `   from arduino.app_bricks.web_ui import WebUI           ` `   ui = WebUI()           ` `   # === Action Mapping Table ===           ` `   # Like a menu: Customer orders "steak", kitchen knows to make "dish #1"           ` `   ACTION_MAP = {           ` `   	   'walk':      1,           ``   	   'turnL':     3,           ``   	   'turnR':     4,           ``   	   'moonwalk':  5,           ``   	   'dance':     6,           ``   	   'upDown':    7,           ``   	   'pushUp':    8,           ``   	   'hello':     9,           ``   	   'frontBack': 11,           ``   	   'home':      12,           ``   	   'init':      13,           ``   }           ` `   # === Default Parameters ===           ` `   current_steps = 5      # Default steps           ` `   current_period = 800   # Default period (ms)           ` `   # === Callback Functions ===           ` `   def on_action(sid, cmd):           ``   	   """           ` `   	   Handle action commands from frontend           ` `   	   sid: Socket.IO session ID           ` `   	   cmd: action name, e.g., 'walk'           ` `   	   """           ` `   	   action_id = ACTION_MAP.get(cmd, 0)           ` `   	   if action_id > 0:           ``   	       print(f"🎮 Action: {cmd} (id={action_id}, steps={current_steps}, period={current_period})", flush=True)           ` `   	       # Call Arduino's action function via Bridge           ` `   	       Bridge.call("action", action_id)           ` `   	       # Send status feedback to frontend           ` `   	       ui.send_message("status", {"msg": f"Executing: {cmd}", "busy": True})           ` `   	   else:           ``   	       print(f"⚠️ Unknown action: {cmd}", flush=True)           ` `   def on_steps(sid, value):           ``   	   """           ` `   	   Handle steps slider changes           ` `   	   value: step value (1-20)           ` `   	   """           ` `   	   global current_steps           ` `   	   try:           ``   	       # Constrain step range, like safety rails           ` `   	       current_steps = max(1, min(20, int(value)))           ` `   	       # Call Arduino's steps function via Bridge           ` `   	       Bridge.call("steps", current_steps)           ` `   	       print(f"⚙️ Steps: {current_steps}", flush=True)           ` `   	   except:           ``   	       pass           ` `   def on_period(sid, value):           ``   	   """           ` `   	   Handle speed slider changes           ` `   	   value: period value (200-3000ms)           ` `   	   """           ` `   	   global current_period           ` `   	   try:           ``   	       # Constrain period range           ` `   	       current_period = max(200, min(5000, int(value)))           ` `   	       # Call Arduino's period function via Bridge           ` `   	       Bridge.call("period", current_period)           ` `   	       print(f"⚙️ Period: {current_period}ms", flush=True)           ` `   	   except:           ``   	       pass           ` `   # === Register Events ===           ` `   # Tell the waiter: when hearing "action", find on_action to handle           ` `   ui.on_message('action', on_action)           ` `   # When hearing "steps", find on_steps to handle           ` `   ui.on_message('steps', on_steps)           ` `   # When hearing "period", find on_period to handle           ` `   ui.on_message('period', on_period)           ` `   print("🤖 Kame Robot Web Controller Ready", flush=True)           ` `   # Start the application, open for business           ` `   App.run()           `

**6.3 Middleware Workflow**

**Startup Phase:**

1. Initialize WebUI components (waiter reports for duty)
2. Register message handling callbacks (remember who handles what)
3. Wait for frontend connection (wait for customers to arrive)

**Receive Commands:**

1. Frontend sends messages via Socket.IO (customers order)
2. Call corresponding callback based on message type (waiter categorizes orders)
3. Parameter validation and range constraint (check if customer requirements are reasonable)

**Forward Commands:**

1. Convert action name to ID ("walk"→1, like "steak"→"dish #1")
2. Call corresponding Arduino function via Bridge.call() (shout "make dish #1" to kitchen)
3. Arduino executes actual action (chef starts cooking)

**Status Feedback:**

1. Send status to frontend via ui.send\_message() (waiter tells customer "your dish is being prepared")
2. Frontend updates UI display (customer sees status update)

**6.4 Key Design Points**

**1\. Action Mapping Table:**

`   	ACTION_MAP = {          ` `   	   'walk': 1,      # Frontend uses 'walk', Arduino uses 1          ` `   	   'dance': 6,     # Decouple frontend and backend naming, like menu and kitchen using different numbers          ` `   }          `

**2\. Parameter Constraints:**

`   current_steps = max(1, min(20, int(value)))  # Ensure steps between 1-20          ` `   current_period = max(200, min(5000, int(value)))  # Period between 200-5000ms          ` `   # Like safety rails preventing parameters from going out of reasonable range          `

**3\. Status Feedback:**

`   ui.send_message("status", {"msg": f"Executing: {cmd}", "busy": True})          ` `   # Frontend receives and updates status display, like "your order has been received"          `

**4\. Debug Output:**

`   print(f"🎮 Action: {cmd} (id={action_id})", flush=True)          ` `   # flush=True ensures immediate output, convenient for debugging, like waiter loudly repeating orders          `

### Part 7: Web Frontend Detailed Explanation

The web frontend provides the graphical user interface for human-robot interaction, with responsive design supporting both mobile and desktop.

**Restaurant Analogy:**

1. **HTML** is the menu structure (what dishes, how categorized)
2. **CSS** is the menu styling (colors, fonts, layout)
3. **JavaScript** is the ordering logic (button clicks, sending orders)

**7.1 File Structure**

`   	assets/          ` `   ├── index.html          # Main page skeleton          ` `   ├── style.css           # Cyberpunk stylesheet          ` `   ├── script.js           # Interaction logic          ` `   └── socket.io.min.js    # Socket.IO library (local file, supports offline use)          `

**7.2 HTML Structure (index.html)**

`   <!DOCTYPE html>          ` `   <html lang="en">          ` `   <head>          ` `   	   <meta charset="UTF-8">          ` `   	   <meta name="viewport" content="width=device-width, initial-scale=1.0">          ` `   	   <title>Kame Robot Controller</title>          ` `   	   <link rel="stylesheet" href="style.css">          ` `   	   <script src="socket.io.min.js"></script>          ` `   </head>          ` `   <body>          ` `   	   <header>          ` `   	       <div class="app-title">🤖 Kame Robot</div>          ` `   	       <div class="status-badge">          ` `   	           <div id="dot" class="dot"></div>          ` `   	           <span id="stat">Connecting...</span>          ` `   	       </div>          ` `   	   </header>          ` `   	   <main class="dashboard">          ` `   	       <!-- Left side parameter panel -->          ` `   	       <section class="panel-side" id="panel-params">          ` `   	           <!-- Steps slider -->          ` `   	           <div class="control-group">          ` `   	               <div class="group-title">          ` `   	                   <span>Steps</span>          ` `   	                   <span id="steps-val" class="val-display">5</span>          ` `   	               </div>          ` `   	               <input class="slider-speed" type="range" min="1" max="20" value="5"           ` `   	                      oninput="updateSteps(this.value)">          ` `   	           </div>          ` `   	           <!-- Speed slider -->          ` `   	           <div class="control-group">          ` `   	               <div class="group-title">          ` `   	                   <span>Period</span>          ` `   	                   <span id="period-val" class="val-display">800ms</span>          ` `   	               </div>          ` `   	               <input class="slider-gimbal" type="range" min="200" max="3000" value="800" step="100"          ` `   	                      oninput="updatePeriod(this.value)">          ` `   	               <div class="slider-label">          ` `   	                   <span>Fast</span>          ` `   	                   <span>Slow</span>          ` `   	               </div>          ` `   	           </div>          ` `   	           <!-- Status panel -->          ` `   	           <div class="control-group status-panel">          ` `   	               <div class="group-title"><span>Status</span></div>          ` `   	               <div id="status-text" class="status-text">READY</div>          ` `   	           </div>          ` `   	       </section>          ` `   	       <!-- Center action buttons area -->          ` `   	       <section class="panel-center" id="panel-actions">          ` `   	           <div class="action-grid">          ` `   	               <!-- Movement category -->          ` `   	               <div class="action-category">          ` `   	                   <div class="category-title">🦿 Movement</div>          ` `   	                   <div class="action-buttons cols-3">          ` `   	                       <button class="action-btn btn-move" onclick="doAction('walk')">          ` `   	                           <span class="btn-icon">🚶</span>          ` `   	                           <span class="btn-label">Walk</span>          ` `   	                       </button>          ` `   	                       <!-- More buttons... -->          ` `   	                   </div>          ` `   	               </div>          ` `   	               <!-- More categories... -->          ` `   	           </div>          ` `   	       </section>          ` `   	   </main>          ` `   	   <script src="script.js"></script>          ` `   </body>          ` `   </html>          `

**7.3 JavaScript Interaction Logic (script.js)**

`   const socket = io();          ``   const dot = document.getElementById('dot');          ``   const stat = document.getElementById('stat');          ``   const statusText = document.getElementById('status-text');          ``   // === Connection Status Handling ===          ` `   socket.on('connect', () => {           ` `   	   dot.classList.add('online');           ``   	   stat.innerText = "ONLINE";           ``   	   stat.style.color = "#fff";          ``   	   statusText.innerText = "READY";          ``   	   statusText.className = "status-text ready";          ``   });          ``   socket.on('disconnect', () => {           ` `   	   dot.classList.remove('online');           ``   	   stat.innerText = "OFFLINE";           ``   	   stat.style.color = "#666";          ``   	   statusText.innerText = "DISCONNECTED";          ``   	   statusText.className = "status-text";          ``   });          ``   // === Receive Status Feedback ===          ` `   socket.on('status', (data) => {          ` `   	   if (data.msg) {          ` `   	       statusText.innerText = data.msg;          ``   	       statusText.className = data.busy ? "status-text busy" : "status-text ready";          ``   	   }          ` `   });          ``   // === Send Action Commands ===          ` `   function doAction(cmd) {          ` `   	   if(event && event.cancelable) event.preventDefault();          ``   	   if(navigator.vibrate) navigator.vibrate(20);  // Haptic feedback          ` `   	   socket.emit('action', cmd);  // Send to Python middleware          ` `   	   statusText.innerText = "⏳ " + cmd + "...";          ``   	   statusText.className = "status-text busy";          ``   	   // Button press animation          ` `   	   if(event && event.target) {          ` `   	       const btn = event.target.closest('.action-btn');          ``   	       if(btn) {          ` `   	           btn.classList.add('pressed');          ``   	           setTimeout(() => btn.classList.remove('pressed'), 300);          ``   	       }          ` `   	   }          ` `   }          ` `   // === Update Steps ===          ` `   function updateSteps(val) {          ` `   	   document.getElementById('steps-val').innerText = val;          ``   	   socket.emit('steps', val);  // Send to Python middleware          ` `   }          ` `   // === Update Period ===          ` `   function updatePeriod(val) {          ` `   	   document.getElementById('period-val').innerText = val + "ms";          ``   	   socket.emit('period', val);  // Send to Python middleware          ` `   }          ` `   // === Disable Right-Click Menu ===          ` `   document.oncontextmenu = (e) => e.preventDefault();          `

**7.4 CSS Style Design Points**

`   :root {          ` `   	   --bg-color: #0d0d0d;        /* Dark background, cyberpunk style */          ` `   	   --primary-cyan: #00f2ff;     /* Cyan, represents movement */          ` `   	   --primary-amber: #ffae00;    /* Amber, represents steps */          ` `   	   --primary-green: #00e676;    /* Green, represents system */          ` `   	   --primary-purple: #b388ff;   /* Purple, represents performance */          ` `   }          ` `   /* Responsive design: auto-adjust layout on mobile portrait */          ` `   @media (max-width: 900px) and (orientation: portrait) {          ` `   	   .dashboard {           ` `   	       flex-direction: column;  /* Change to vertical arrangement */          ` `   	   }          ` `   }          ` `   /* Button press animation */          ``   .action-btn:active, .action-btn.pressed {          ` `   	   transform: scale(0.95);      /* Slightly shrink, creating pressed feeling */          ` `   	   box-shadow: 0 0 20px currentColor;  /* Glow effect */          ` `   }          `

**7.5 Frontend-Backend Communication Flow**

`   1. Frontend Operation → Socket.IO Message → Python Middleware          ` `   	  └─ Click "Walk" button → doAction('walk') → socket.emit('action', 'walk')          ` `   	  (Like customer saying "I'd like to order steak")          ` `   2. Python Middleware Processing → Bridge Call → Arduino          ` `   	  └─ on_action('walk') → Bridge.call('action', 1)          ` `   	  (Waiter shouts "make one dish #1" to kitchen)          ` `   3. Arduino Execution → Completion Feedback          ` `   	  └─ robot.walk() → Automatically returns home after execution          ` `   	  (Chef starts cooking)          ` `   4. Status Feedback → Socket.IO → Frontend UI Update          ` `   	  └─ ui.send_message('status', {...}) → Frontend displays "Executing: walk"          ` `   	  (Waiter tells customer "your dish is being prepared")          `

### Part 8: Complete Action Library Detailed Explanation

Standing posture is the foundation of all actions and the default posture after action execution.

`   void MiniKame::home() {         ` `   	   int ap = 20;   // Anteroposterior offset         ` `   	   int hi = 25;   // Height offset         ` `   	   int position[] = {         ` `   	       90 + ap,    // Left front thigh: forward 20°         ` `   	       90 - ap,    // Right front thigh: backward 20°         ` `   	       90 - hi,    // Left front calf: lift 25°         ` `   	       90 + hi,    // Right front calf: lower 25°         ` `   	       90 - ap,    // Left rear thigh: backward 20°         ` `   	       90 + ap,    // Right rear thigh: forward 20°         ` `   	       90 + hi,    // Left rear calf: lower 25°         ` `   	       90 - hi     // Right rear calf: lift 25°         ` `   	   };         ``   	   for (int i = 0; i < 8; i++) setServo(i, position[i]);         ``   }         `

**8.1.1 Posture Analysis**

Let's use a table to understand each leg's initial position:

![](https://projects.arduinocontent.cc/4a47b334-f5df-4ef0-b2f9-a0994dd0edbb.png)

**8.1.2 Why This Design?**

**1\. Diagonal Balance Principle**

Observing that left front and right rear form one group (both forward, up), right front and left rear form another (both backward, down). This is classic diagonal balance in quadruped robots:

1. Left front-right rear diagonal: legs extend forward, body raised
2. Right front-left rear diagonal: legs retract backward, body lowered

This design centers the robot's center of gravity, like a table with four legs being stable.

**2\. Significance of Offset Values**

ap = 20 and hi = 25 aren't chosen randomly:

1. ap controls front-back posture: 20° gives legs natural front-back separation
2. hi controls body height: 25° lifts body about 2-3cm off ground—not too high to be unstable, not too low to drag

**Analogy** : Like standing with legs slightly apart and knees slightly bent—most stable. Standing with legs together and straight is actually more prone to falling.

**8.1.3 zero(): Complete Zeroing**

`   void MiniKame::zero() {         ` `   	   for (int i = 0; i < 8; i++) setServo(i, 90);         ``   }         `

zero() sets all servos to 90°, the physical neutral position. Main uses:

1. Verify all servos working correctly during initial debugging
2. Benchmark for all movements
3. Re-zero after replacing servos or reassembly

**8.2 Walking Gait (walk)**

Walking is the most basic and important action for quadruped robots. Let's deeply understand its implementation.

`   void MiniKame::walk(float steps, int T = 500) {         ` `   	   int x_amp = 15;      // Forward/backward swing amplitude         ` `   	   int z_amp = 20;      // Up/down leg lift amplitude         ` `   	   int ap = 20;         // Anteroposterior offset         ` `   	   int hi = 30;         // Height offset         ` `   	   int front_x = 12;    // Extra forward extension for front legs         ` `   	   int period[] = {T, T, T/2, T/2, T, T, T/2, T/2};         ``   	   int amplitude[] = {x_amp, x_amp, z_amp, z_amp, x_amp, x_amp, z_amp, z_amp};         ``   	   int offset[] = {         ` `   	       90 + ap - front_x,  // Left front thigh         ` `   	       90 - ap + front_x,  // Right front thigh         ` `   	       90 - hi,            // Left front calf         ` `   	       90 + hi,            // Right front calf         ` `   	       90 - ap - front_x,  // Left rear thigh         ` `   	       90 + ap + front_x,  // Right rear thigh         ` `   	       90 + hi,            // Left rear calf         ` `   	       90 - hi             // Right rear calf         ` `   	   };         ``   	   int phase[] = {90, 90, 270, 90, 270, 270, 90, 270};         ``   	   // Execution logic         ` `   	   for (int i = 0; i < 8; i++) {         ` `   	       oscillator[i].reset();         ``   	       oscillator[i].setPeriod(period[i]);         ``   	       oscillator[i].setAmplitude(amplitude[i]);         ``   	       oscillator[i].setPhase(phase[i]);         ``   	       oscillator[i].setOffset(offset[i]);         ``   	   }         ` `   	   _final_time = millis() + period[0] * steps;         ``   	   _init_time = millis();         ``   	   bool side;         ``   	   while (millis() < _final_time) {         ` `   	       side = (int)((millis() - _init_time) / (period[0] / 2)) % 2;         ``   	       // Thighs always move         ` `   	       setServo(0, oscillator[0].refresh());         ``   	       setServo(1, oscillator[1].refresh());         ``   	       setServo(4, oscillator[4].refresh());         ``   	       setServo(5, oscillator[5].refresh());         ``   	       // Calves alternate movement         ` `   	       if (side == 0) {         ` `   	           setServo(3, oscillator[3].refresh());         ``   	           setServo(6, oscillator[6].refresh());         ``   	       } else {         ` `   	           setServo(2, oscillator[2].refresh());         ``   	           setServo(7, oscillator[7].refresh());         ``   	       }         ` `   	       delay(1);         ``   	   }         ` `   }         `

8.2.1 Parameter Detailed Explanation

**1\. Amplitude**

![](https://projects.arduinocontent.cc/147bce74-db29-4e26-bbd0-d4ead3272ea7.png)

Why larger calf amplitude? Because lifting requires overcoming gravity, needing larger angles to ensure feet completely clear ground.

**2\. Period**

![](https://projects.arduinocontent.cc/8f74504a-0996-44c9-96bd-70536159d6a1.png)

**3\. Offset**

Let's analyze each offset value line by line:

`   Left front thigh: 90 + ap - front_x = 90 + 20 - 12 = 98°         `

Left front thigh extends 8° forward from neutral, because front legs bear more propulsion tasks.

`   Right front thigh: 90 - ap + front_x = 90 - 20 + 12 = 82°         `

Right front thigh swings 8° backward from neutral, symmetrical with left front.

`   Left front calf: 90 - hi = 90 - 30 = 60°         `

Left front calf lifts 30°, lifting foot off ground.

`   Right front calf: 90 + hi = 90 + 30 = 120°         `

Right front calf lowers 30°, supporting body.

**4\. Phase**

This is the most critical parameter. Let's rearrange the phase table:

![](https://projects.arduinocontent.cc/acea812c-41bd-4856-95f6-2056eec33859.png)

**8.2.2 Gait Analysis**

**1\. Diagonal Coordination**

Left front and right rear form one pair, right front and left rear another. When left front leg swings forward, right rear also swings forward, forming diagonal support. This is the classic trot gait of quadruped animals.

**2\. Calf Alternation Logic**

`   	side = (int)((millis() - _init_time) / (period[0] / 2)) % 2;        `

This formula determines whether it's the first or second half of the period:

1. side = 0: first half, activate right front calf (3) and left rear calf (6)
2. side = 1: second half, activate left front calf (2) and right rear calf (7)

**3\. Complete Walking Cycle**

A complete walking cycle has two phases:

**Phase 1 (First Half):**

1. Left front thigh swings forward, left front calf lifts (preparing to land)
2. Right rear thigh swings forward, right rear calf lifts (preparing to land)
3. Right front thigh swings backward, right front calf lowers (supporting)
4. Left rear thigh swings backward, left rear calf lowers (supporting)

**Phase 2 (Second Half):**
1. Left front thigh swings backward, left front calf lowers (supporting)
2. Right rear thigh swings backward, right rear calf lowers (supporting)
3. Right front thigh swings forward, right front calf lifts (preparing to land)
4. Left rear thigh swings forward, left rear calf lifts (preparing to land)

This creates stable forward movement.

**Analogy** : Like when walking, when left leg moves forward, right arm also moves forward (diagonal coordination). If left leg and left arm both move forward together, that's walking awkwardly.

**8.3 Turning Gaits**

**8.3.1 Turn Left (turnL)**

`   void MiniKame::turnL(float steps, int T = 600) {        ` `   	   int x_amp = 15;        ``   	   int z_amp = 15;        ``   	   int ap = 15;        ``   	   int hi = 23;        ``   	   int period[] = {T, T, T, T, T, T, T, T};        ``   	   int amplitude[] = {x_amp, x_amp, z_amp, z_amp, x_amp, x_amp, z_amp, z_amp};        ``   	   int offset[] = {90 + ap, 90 - ap, 90 - hi, 90 + hi,         ``   	                   90 - ap, 90 + ap, 90 + hi, 90 - hi};        ``   	   int phase[] = {180, 0, 90, 90, 0, 180, 90, 90};        ``   	   execute(steps, period, amplitude, offset, phase);        ``   }        `

**8.3.2 Parameter Analysis**

**Phase Table (Turn Left):**

![](https://projects.arduinocontent.cc/29b05fb2-912e-44e8-8fd4-d77c33471bf6.png)

**Turning Mechanics Principle:**

**Left-Right Phase Opposition:**

1. When left side legs move forward (near 0° phase), right side legs move backward (near 180° phase)
2. This creates torque causing counterclockwise rotation

**Front-Rear Relationship:**
1. Left front (180°) and left rear (0°) have 180° phase difference
2. This means front legs move backward while rear move forward, further enhancing the rotation effect

**Consistent Calf Phases:**

1. All calves have phases around 90°
2. Ensures legs can still lift and lower during rotation

**Analogy** : This is like paddling only on the left side of a boat—the boat turns right. Here, left side legs moving forward (paddling) while right side moves backward (resistance) creates rotational torque.

**8.3.3 Turn Right (turnR)**

`   void MiniKame::turnR(float steps, int T = 600) {        ` `   	   // ... same parameters ...        ``   	   int phase[] = {0, 180, 90, 90, 180, 0, 90, 90};        ``   	   execute(steps, period, amplitude, offset, phase);        ``   }        `

Compared to turn left, only the left-right leg phases are swapped:

1. Left leg phase 0°, right leg phase 180° (completely opposite to turn left)
2. This creates clockwise rotation

**8.4 Dance Mode (dance)**

`   void MiniKame::dance(float steps, int T = 600) {        ` `   	   int x_amp = 0;        // Thighs don't swing        ` `   	   int z_amp = 40;       // Calves swing largely        ` `   	   int ap = 30;          // Larger offset        ` `   	   int hi = 20;        ``   	   int period[] = {T, T, T, T, T, T, T, T};        ``   	   int amplitude[] = {x_amp, x_amp, z_amp, z_amp, x_amp, x_amp, z_amp, z_amp};        ``   	   int offset[] = {90 + ap, 90 - ap, 90 - hi, 90 + hi,         ``   	                   90 - ap, 90 + ap, 90 + hi, 90 - hi};        ``   	   int phase[] = {0, 0, 0, 270, 0, 0, 90, 180};        ``   	   execute(steps, period, amplitude, offset, phase);        ``   }        `

**8.4.1 Parameter Analysis**

**1\. Special Amplitude Settings**

1. x\_amp = 0: Thighs completely stationary
2. z\_amp = 40: Calf amplitude double that of walking

**2\. Exaggerated Offsets**

1. ap = 30: Larger than walking's 20°
2. Body posture more exaggerated, presenting twisting state

**3\. Chaotic Phases**

![](https://projects.arduinocontent.cc/3f517e15-3309-4a29-b639-3e977df7db7f.png)

**8.4.2 Source of Dance Effect**

When phases no longer follow patterns, the robot presents twisting, swaying effects:

1. Chaotic Phases: No diagonal coordination, each leg acts independently
2. Large Calf Swings: Create exaggerated leg movements
3. Exaggerated Posture: Body twists with large amplitude

**Design Philosophy** : Order creates patterns, patterns create function; breaking patterns creates variation, variation creates interest.

**8.5 Moonwalk (moonwalkL)**

`   void MiniKame::moonwalkL(float steps, int T = 5000) {        ` `   	   int z_amp = 45;       // Calves swing largely        ` `   	   int period[] = {T, T, T, T, T, T, T, T};        ``   	   int amplitude[] = {0, 0, z_amp, z_amp, 0, 0, z_amp, z_amp};        ``   	   int offset[] = {90, 90, 90, 90, 90, 90, 90, 90};        ``   	   int phase[] = {0, 0, 0, 120, 0, 0, 180, 290};        ``   	   execute(steps, period, amplitude, offset, phase);        ``   }        `

**8.5.1 Moonwalk Principle**

**Key Design:**

1. Fixed Thighs: All thigh amplitudes 0, remain stationary
2. Calf Movement Only: Only calves swing
3. Staggered Phases: Calf phases vary (0°, 120°, 180°, 290°)

**Visual Effect:**

1. Fixed thighs mean body position basically unchanged
2. Alternating calf movement creates wave-like visual effect
3. Looks like sliding on smooth ground

**Analogy** : This is like Michael Jackson's moonwalk, where the body moves forward but the feet appear to slide backward. Here it's the opposite—body stationary while legs move, creating a visual illusion.

**8.6 Up and Down (upDown)**

`   void MiniKame::upDown(float steps, int T = 5000) {        ` `   	   int x_amp = 0;        // Thighs don't swing        ` `   	   int z_amp = 25;       // Calf amplitude        ` `   	   int ap = 20;        ``   	   int hi = 25;        ``   	   int front_x = 0;        ``   	   int period[] = {T, T, T, T, T, T, T, T};        ``   	   int amplitude[] = {x_amp, x_amp, z_amp, z_amp, x_amp, x_amp, z_amp, z_amp};        ``   	   int offset[] = {90 + ap - front_x, 90 - ap + front_x, 90 - hi, 90 + hi,        ``   	                   90 - ap - front_x, 90 + ap + front_x, 90 + hi, 90 - hi};        ``   	   int phase[] = {0, 0, 90, 270, 180, 180, 270, 90};        ``   	   execute(steps, period, amplitude, offset, phase);        ``   }        `

**8.6.1 Movement Analysis**

**Phase Relationships:**

![](https://projects.arduinocontent.cc/afd92e96-99de-423c-a5e2-63c6a21526a5.png)

**Movement Effect:**

1. Front calves have 180° phase difference, so one lifts while the other lowers
2. Rear calves are the same, but opposite phase from front
3. Result is body rising and falling as a whole

**8.7 Push-up (pushUp)**

`   void MiniKame::pushUp(float steps, int T = 600) {       ` `   	   int z_amp = 30;       // Calf amplitude 30°       ` `   	   int x_amp = 60;       // Rear thighs extend backward 60°       ` `   	   int hi = 20;       ``   	   int period[] = {T, T, T, T, T, T, T, T};       ``   	   int amplitude[] = {0, 0, z_amp, z_amp, 0, 0, 0, 0};       ``   	   int offset[] = {       ` `   	       90, 90,           // Front thighs fixed       ` `   	       90 - hi, 90 + hi, // Front calves move up/down       ` `   	       90 - x_amp,       // Left rear thigh extends backward       ` `   	       90 + x_amp,       // Right rear thigh extends backward       ` `   	       90 + hi, 90 - hi  // Rear calves fixed       ` `   	   };       ``   	   int phase[] = {0, 0, 0, 180, 0, 0, 0, 170};       ``   	   execute(steps, period, amplitude, offset, phase);       ``   }       `

**8.7.1 Action Breakdown**

**1\. Rear Leg Setup:**

1. Rear thighs set to 30° and 150°, lowering rear of body
2. Like feet position when doing push-ups

**2\. Front Calf Movement:**

1. Only servos 2 and 3 (front calves) move
2. Amplitude 30°, swinging within 30° range
3. 180° phase difference, alternating lift and lower

**3\. Body Posture:**

1. Front legs remain upright
2. Rear legs extended backward, body leaning forward
3. Forms push-up ready posture

**8.7.2 Movement Effect**

This perfectly simulates push-up action:

1. Preparation: Body leans forward, center of gravity shifts forward
2. Lowering: Front calves bend, body lowers
3. Rising: Front calves straighten, body rises
4. Repeat: Alternating

**8.8 Greeting (hello)**

`   void MiniKame::hello() {       ` `   	   // Step 1: Sit down       ` `   	   float sentado[] = {       ` `   	       90 + 15,  // Left front thigh forward       ` `   	       90 - 15,  // Right front thigh backward       ` `   	       90 - 10,  // Left front calf slightly lifted       ` `   	       90 + 60,  // Right front calf largely bent       ` `   	       90 + 10,  // Left rear thigh forward       ` `   	       90 - 10,  // Right rear thigh backward       ` `   	       90 + 10,  // Left rear calf lowered       ` `   	       90 - 10   // Right rear calf lifted       ` `   	   };       ``   	   moveServos(150, sentado);       ``   	   delay(300);       ``   	   // Step 2: Wave       ` `   	   int T = 550;       ``   	   int period[] = {T, T, T, T, T, T, T, T};       ``   	   int amplitude[] = {0, 50, 0, 50, 0, 0, 0, 0};       ``   	   int offset[] = {       ` `   	       90 + 15,  // Left front thigh       ` `   	       40,       // Right front thigh largely forward       ` `   	       90 - 30,  // Left front calf       ` `   	       90,       // Right front calf       ` `   	       90 + 20,  // Left rear thigh       ` `   	       90 - 20,  // Right rear thigh       ` `   	       90 + 10,  // Left rear calf       ` `   	       90 - 10   // Right rear calf       ` `   	   };       ``   	   int phase[] = {0, 0, 0, 90, 0, 0, 0, 0};       ``   	   execute(4, period, amplitude, offset, phase);       ``   	   // Step 3: Stand up       ` `   	   float goingUp[] = {       ` `   	       90,       // Left front thigh back to normal       ` `   	       70,       // Right front thigh backward       ` `   	       90,       // Left front calf back to normal       ` `   	       90,       // Right front calf back to normal       ` `   	       90 - 20,  // Left rear thigh backward       ` `   	       90 + 20,  // Right rear thigh forward       ` `   	       90 + 10,  // Left rear calf       ` `   	       90 - 10   // Right rear calf       ` `   	   };       ``   	   moveServos(500, goingUp);       ``   	   delay(200);       ``   }       `

**8.8.1 Action Sequence Design**

hello() demonstrates combining multiple basic actions to create expressive behavior:

**Phase 1: Sit Down**

1. Right front calf largely bent (90+60=150°), this is key
2. Other legs fine-tuned to maintain balance
3. Entire robot center of gravity lowers, presenting "sitting" posture

**Phase 2: Wave**

1. Only right front leg moves (servos 1 and 3)
2. Amplitude 50°, letting leg swing largely
3. Execute 4 oscillations, creating "waving" action
4. Other legs remain fixed, maintaining sitting posture

**Phase 3: Stand Up**

1. Return to standing posture
2. Right front thigh returns to 70° (further back than standard posture)
3. All legs adjust to final positions

**8.8.2 Behavior Design Philosophy**

This function shows important principles of robot behavior design:

1. Preparation: Sit down, attract attention
2. Main Action: Wave, convey information
3. Conclusion: Stand up, return to normal

This "prepare-execute-conclude" structure makes robot behavior more natural and expressive.

**8.9 Front and Back Swing (frontBack)**

`   void MiniKame::frontBack(float steps, int T = 600) {       ` `   	   int x_amp = 30;       // Larger front-back amplitude       ` `   	   int z_amp = 25;       // Medium up-down amplitude       ` `   	   int ap = 20;       ``   	   int hi = 30;       ``   	   int period[] = {T, T, T, T, T, T, T, T};       ``   	   int amplitude[] = {x_amp, x_amp, z_amp, z_amp, x_amp, x_amp, z_amp, z_amp};       ``   	   int offset[] = {90 + ap, 90 - ap, 90 - hi, 90 + hi,       ``   	                   90 - ap, 90 + ap, 90 + hi, 90 - hi};       ``   	   int phase[] = {0, 180, 270, 90, 0, 180, 90, 270};       ``   	   execute(steps, period, amplitude, offset, phase);       ``   }       `

**8.9.1 Movement Characteristics**

**1\. Large Amplitude: x\_amp = 30 is double walking's 15°, creating large front-back swings**

**2\. Phase Relationships:**

1. Front and rear legs have same phase (front 0°, rear 0°)
2. Left and right legs have opposite phase (left 0°, right 180°)

**3\. Movement Effect:**

1. All legs swing forward simultaneously, then backward simultaneously
2. Robot as a whole sways front and back, like rocking

**8.10 Difference Between init() and home()**

Although we've analyzed home() in detail, it's worth explaining the difference between init() and home():

**init():**

1. Called only once at program start
2. Sets pin mapping, trim values, reverse directions
3. Initializes oscillators and servos
4. Equivalent to "system boot"

**home():**

1. Can be called multiple times
2. Sets robot to standard standing posture
3. Automatically called after action execution
4. Equivalent to "return to home position"

**8.11 Action Design Summary**

**8.11.1 Application of Four Core Parameters**

Through analyzing all actions, we can see how different combinations of four parameters produce different effects:

![](https://projects.arduinocontent.cc/0436a219-aba8-4722-a76a-914583938ac9.png)

**8.11.2 Action Classification**

Based on movement characteristics, actions can be classified into several categories:

1\. Movement Class: walk, turnL, turnR

1. Characterized by generating displacement
2. Requires diagonal coordination

2\. Performance Class: dance, moonwalk, hello

1. Characterized by strong visual appeal
2. Can break conventional patterns

3\. Stunt Class: pushUp, upDown, frontBack

1. Characterized by specific part movement
2. Other parts remain fixed

4\. System Class: init, home, zero

1. Used for initialization and reset
2. Doesn't involve oscillatory movement

**8.11.3 Method for Designing New Actions**

If you want to create new actions, you can follow this process:

**Determine Action Intent** : What do you want the robot to do? (e.g., nod, shake head, lift leg)

**Decompose Movement Elements:**

1. Which legs need to move?
2. What direction of movement?
3. How large the movement range?
4. How fast the movement speed?

**Set Parameters:**

1. Stationary legs: set amplitude to 0
2. Moving legs: set amplitude and period based on requirements
3. Set phase to achieve coordination
4. Adjust offset to maintain balance

**Test and Adjust:**

1. First test each leg individually
2. Then test overall effect
3. Fine-tune parameters until satisfied

**Combine Sequences:**

1. Multiple basic actions can be combined into complex behaviors
2. Ensure smooth transitions between actions

**Example** : Creating a "nod" action

`   void MiniKame::nod() {      ` `   	   // Nod: front legs move up/down, rear legs fixed      ` `   	   int amplitude[] = {0, 0, 20, 20, 0, 0, 0, 0};      ``   	   int offset[] = {90, 90, 70, 110, 90, 90, 90, 90};      ``   	   int phase[] = {0, 0, 0, 180, 0, 0, 0, 0};      ``   	   int period[] = {500, 500, 500, 500, 500, 500, 500, 500};      ``   	   execute(3, period, amplitude, offset, phase);      ``   }      `

By understanding the magic of these four parameters, you can create an infinite variety of actions, allowing MiniKame to showcase rich expressiveness.

### Part 9: Deployment and Usage Guide

![](https://www.youtube.com/watch?v=VmBMdW49ng8)

**9.1 Quick Start Process**

**Step 1: Run the Program**

`   # Execute in project root directory      ` `   arduino-app-cli app start kame_robot      `

Like a restaurant opening for business, waiters are ready.

**Step 2: Connect to the Same WiFi as the Robot**

1. Connect your phone/computer to the same WiFi as the robot
2. Like entering the restaurant's exclusive area.

**Step 3: Open Control Interface**

1. Browser access http://<robot IP>:7000
2. Default IP can be viewed in serial monitor
3. Like getting the menu, ready to order.
![](https://projects.arduinocontent.cc/c6783fe8-9a0f-4d3f-b42e-0b4bb73b86fd.png)

**9.2 Interface Operation Guide**

**Parameter Adjustment Area:**

1. Steps Slider (Amber): 1-20 steps, controls repetition count for each action
2. Speed Slider (Cyan): 200-3000ms, smaller value = faster action
3. Status Display: Shows current connection and execution status

**Action Button Area:**

1. Movement Class (Cyan): Walk, Turn Left, Turn Right
2. Performance Class (Purple): Dance, Moonwalk, Hello, Front Back
3. Stunt Class (Yellow): Push-up, Up Down
4. System Class (Green): Initialize, Return Home

**Operation Feedback:**

1. Button press provides haptic feedback (mobile)
2. Status display updates in real-time
3. LED indicator shows execution status

**9.3 Configuration File Description**

app.yaml is the Arduino App configuration file:

`   # app.yaml      ` `   name: kame_robot                    # Application name      ` `   description: "Web controlled Kame quadruped robot"  # Description      ` `   icon: 🤖                            # App icon      ` `   ports: []                           # Network ports      ` `   bricks:      ``   - arduino:web_ui: {}                # Used brick      `

**9.4 Debugging Techniques**

1\. View Serial Output

`   // Add debug output in sketch.ino      ` `   Serial.println("Executing walk...");      `

2\. View Python Logs

`   # Debug output already present in main.py      ` `   print(f"🎮 Action: {cmd}", flush=True)      `

3\. Browser Console

`   // Add in script.js      ` `   socket.onAny((event, ...args) => {      ` `   	   console.log(event, args);      ``   });      `

4\. Single-Step Debugging Add in Arduino code:

`   while(!Serial.available());  // Wait for serial input      ` `   Serial.read();               // Read and discard      `

### Part 10: Calibration and Debugging

**10.1 Mechanical Calibration (trim values)**

Trim values compensate for mechanical assembly errors. Even with all servos set to 90°, due to assembly errors, the robot may not stand level.

**Real-life Analogy:**

1. Trim values are like putting paper shims under table legs to stop wobbling
2. Each leg may need different shim thickness
3. Our goal is to find how much each leg needs

**Calibration Process:**

Step 1: Initial Observation

`   void setup() {      ` `   	   robot.init();      ``   	   delay(2000);  // Observe for 2 seconds      ` `   	   robot.home();      ``   }      `

Place the robot on a level surface and observe:

1. Do all four legs touch the ground?
2. Is the body level?
3. Are any legs hanging or excessively pressed?

**Step 2: Single Leg Debugging**

`   // Debug program: adjust each leg one by one      ` `   void debugLeg(int leg) {      ` `   	   for (int offset = -30; offset <= 30; offset += 5) {      ` `   	       robot.setServo(leg, 90 + offset);      ``   	       delay(1000);      ``   	   }      ` `   }      `

Like putting different thickness shims under each leg one by one, observing which thickness works best.

Step 3: Record Calibration Values Set trim values in init():

`   trim[0] = -5;   // Left front thigh needs -5° counterclockwise adjustment      ` `   trim[1] = -5;   // Right front thigh needs -5° counterclockwise adjustment      ` `   trim[2] = -20;  // Left front calf needs -20° counterclockwise adjustment      ` `   trim[3] = 10;   // Right front calf needs +10° clockwise adjustment      ` `   trim[4] = -3;   // Left rear thigh needs -3° counterclockwise adjustment      ` `   trim[5] = -3;   // Right rear thigh needs -3° counterclockwise adjustment      ` `   trim[6] = -15;  // Left rear calf needs -15° counterclockwise adjustment      ` `   trim[7] = -13;  // Right rear calf needs -13° counterclockwise adjustment      `

Step 4: Verify Re-upload the program and observe the robot's posture. Usually, 3-5 iterations are needed for satisfactory results.

**10.2 Direction Calibration (reverse values)**

The reverse flag handles inconsistent servo installation directions:

**Determination Method:**

1. Set all reverse to false
2. Call the home() function
3. Observe each leg's movement direction:

**Observation reverse Setting**

![](https://projects.arduinocontent.cc/c25bd8c3-9327-484a-8fa0-b1d0850d33b1.png)

**Analogy** : Some people nod for "yes", some shake their head for "yes". We need to know each person's (each servo's) habit, and then "translate" accordingly.

Code Setting:

`   // Set in init()      ` `   reverse[0] = false;  // Left front thigh: normal      ` `   reverse[1] = true;   // Right front thigh: needs reversal      ` `   reverse[2] = false;  // Left front calf: normal      ` `   reverse[3] = true;   // Right front calf: needs reversal      ` `   // ...      `

**10.3 Common Problems and Solutions**

**Q1** : The robot is unstable and always leans to one side

**Possible Causes:**

1. trim values not properly calibrated
2. A leg's connecting rod installed crooked

**Solutions:**

1. Re-perform the calibration process
2. Check if all screws are tight

**Q2: Servos jitter severely**

**Possible Causes:**

1. Insufficient power supply
2. Poor ground connection

**Solutions:**

1. Replace with a higher current power supply
2. Add a 1000μF capacitor across the servo power
3. Ensure all GND connections are reliable

**Q3: Web interface cannot connect**

Possible Causes:

1. WiFi not connected
2. Python service not started
3. Firewall blocking

**Solutions:**

1. Check the robot's WiFi hotspot
2. Confirm the Python service is running
3. Check if port 7000 is open

**Q4: Action stops mid-execution**

**Possible Causes:**

1. No delay() in the while loop
2. Watchdog timeout

**Solutions:**

1. Add delay(1) in long loops
2. Use yield() to feed the watchdog

**Q5: Phase confusion, gait uncoordinated**

**Possible Causes:**

1. Oscillator time not synchronized
2. Parameter settings are wrong

**Solutions:**

1. Ensure using setTime(global\_time)
2. Check if the phase parameters are correct

### Appendix

**A.1 Project File Structure**

`   	kame_robot/     ` `   ├── sketch/                    # Arduino Firmware     ` `   │   ├── sketch.ino             # Main program     ` `   │   ├── minikame.cpp/h         # MiniKame class implementation     ` `   │   ├── Octosnake.cpp/h        # Oscillator class implementation     ` `   │   └── sketch.yaml             # Dependency configuration     ` `   ├── python/     ` `   │   └── main.py                 # Python middleware     ` `   ├── assets/                     # Web frontend resources     ` `   │   ├── index.html              # Main page     ` `   │   ├── style.css               # Stylesheet     ` `   │   ├── script.js               # Interaction logic     ` `   │   └── socket.io.min.js        # Socket.IO library     ` `   ├── app.yaml                     # Application configuration     ` `   └── README.md                    # Project documentation     `

**A.2 Pin Assignment Table**

![](https://projects.arduinocontent.cc/5413bc2b-b6cf-4c8f-8386-50ba1b7734f3.png)

**A.3 Action Mapping Table**

![](https://projects.arduinocontent.cc/a2e3af20-d457-4050-b45a-fa1ca09b92a0.png)

**A.4 Common Function Quick Reference**

`   	// Initialization     ` `   robot.init();     ``   // Basic actions     ` `   robot.walk(steps, period);     ``   robot.turnL(steps, period);     ``   robot.turnR(steps, period);     ``   robot.dance(steps, period);     ``   robot.moonwalkL(steps, period);     ``   robot.pushUp(steps, period);     ``   robot.hello();     ``   robot.home();     ``   robot.zero();     ``   // Advanced control     ` `   robot.setServo(id, target);     ``   robot.moveServos(time, target[8]);     ``   // Debugging     ` `   robot.getServo(id);     ``   robot.reverseServo(id);     `

Code

MiniKame Quadruped Robot

APLUX-Official

[APLUX-Official](https://github.com/APLUX-Official)

/

[kame\_robot](https://github.com/APLUX-Official/kame_robot)

7

1[no description/ Read More](https://github.com/APLUX-Official/kame_robot#readme)

Latest commit to the master branch on 10-03-2026

[Download as a zip](https://api.github.com/repos/APLUX-Official/kame_robot/zipball)

Documentation

MiniKame Quadruped Robot

MiniKame Quadruped Robot

MiniKame Quadruped Robot - A Desktop Robot Building Tutorial from Scratch.pdf