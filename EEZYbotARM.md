---
title: "EEZYbotARM"
source: "https://www.instructables.com/EEZYbotARM/"
author:
  - "[[Instructables]]"
published: 2015-10-04
created: 2026-05-31
description: "EEZYbotARM: This ia a 3DPrinted robotic arm.The design intent was to make something \"easy\" to build and quite cheapIt uses MG90S small servos for driving the kinematics linkage and a Pololu mini maestro 12 to control the servos (but this is my choice any ot…"
tags:
  - "clippings"
---

The design intent was to make something "easy" to build and quite cheap

It uses MG90S small servos for driving the kinematics linkage and a Pololu mini maestro 12 to control the servos (but this is my choice any other methods are valid)

All the pieces are 3DPrinted in ABS but any other material like PLA can be used

3D models in stl format can be downloaded for free at Thingiverse: [http://www.thingiverse.com/thing:1015238](http://www.thingiverse.com/thing:1015238)

video:

![](https://www.youtube.com/watch?v=N55W8TdMfCo)

ramp loop test:

![](https://www.youtube.com/watch?v=qovZKW0DxWk)

preliminary tests video:

![](https://www.youtube.com/watch?v=x9C_3WHr1G0)

![](https://www.youtube.com/watch?v=0OFL6MxbPIM)

Part list:

n° 20 3D printed parts

· n°1 EBA\_01.00.001.STL

· n°1 EBA\_01.00.002\_vertical\_drive\_arm.STL

· n°3 EBA\_01.00.003\_link.STL

· n°1 EBA\_01.00.004\_forward\_drive\_arm.STL

· n°1 EBA\_01.00.005\_horizontal\_arm.STL

· n°1 EBA\_01.00.006\_triangular\_link.STL

· n°2 EBA\_01.00.009\_servo\_plate.STL

· n°1 EBA\_01.00.010\_basement.STL

· n°1 EBA\_01.00.011\_round\_plate.STL

· n°1 EBA\_01.00.012\_R01\_claw\_support.STL

· n°1 EBA\_01.00.013\_R01\_right\_finger.STL

· n°1 EBA\_01.00.014\_R01\_left\_finger.STL

· n°1 EBA\_01.00.015\_drive\_gear.STL

· n°1 EBA\_01.00.016\_R01\_driven\_gear.STL

· n°1 EBA\_01.00.017\_R01\_ramp.STL (optional)

· n°1 EBA\_01.00.018\_maestro\_holder.STL (optional)

· n°1 EBA\_01.00.019\_ball.STL (optional)

n\* 3 Tower Pro MG90S servos

n\* 1 SG90 servo (gripper) + 1 optional for the loop ramp

n° 7 M4 self locking nuts

n° 15 M4 washers

n° 7 M3 nuts

n° 1 M3 x 30 screw

n° 2 M3 washers

n° 4 M3 x 12 hex screw

n° 2 M3 x 12 TCEI screw

n° 2 M3 x 20 TCEI screw

n° 5 M4 x 20 round hed hex recess screw

n° 1 brass pipe 4 x 3 x 22 + n°1 4 x 3 x 26

ELECTRONICS

The Arm can be driven in several different ways: sketches, potentiometers, joystick, WII nunchuck …. after several trials I found very "easy" to use a controller from Pololu: Mini Maestro USB Servo Controller. You can attach up to 6 – 12 – 24 servos depend of the controller type. It is provided with a free configuration and control program for Windows and Linux that give you the power to drive the servo in manual moving slides; in the mean time you are able to set the values of speed and acceleration for any singular item. You can also build sequences of servo movements and run scripts stored in the internal script memory that can be automatically played back without any computer or external microcontroller connected.

here the link of the Pololu servo controller: [https://www.pololu.com/product/1352](https://www.pololu.com/product/1352)

\------- UPDATE ------

add an instructables to drive it with Arduino, bluetooth module and Android APP made wit MIT app inventor

[https://www.instructables.com/id/Android-APP-to-Con...](https://www.instructables.com/id/Android-APP-to-Control-a-3DPrinted-Robot/)

## Step 1:

[![step 1.png](https://content.instructables.com/FJO/RRCX/IF9TAJA2/FJORRCXIF9TAJA2.png?frame=true&width=963&height=1024&fit=bounds)](https://content.instructables.com/FJO/RRCX/IF9TAJA2/FJORRCXIF9TAJA2.png)

Connect two link arms (003) to the Triangular link (006).

Keep the M4 round heads screws to the inner side like shown on image and selflocking nuts to the outer side.

IMPORTANT

I design all the holes of joints quite exact to allow to make them more precise using a drill bit

The nuts are to be tightened till the locking of the joint, then consequently you must loose them until you obtain a smooth movement with the lower clearance between components. This rule is valid and is to be applied also for the following joint that involve use of self locking nuts.

## Step 2:

[![step 2.png](https://content.instructables.com/FWT/GU7J/IF9TAJJU/FWTGU7JIF9TAJJU.png?frame=true&width=963&height=1024&fit=bounds)](https://content.instructables.com/FWT/GU7J/IF9TAJJU/FWTGU7JIF9TAJJU.png)

Connect link (003) to the rear joint of the horizontal arm (005).

The lower part of the link (003) is to be connected with the vertical drive arm (002) as shown.

Between the two links interpose three M4 washer, this to better align them with the vertical arm

Keep the M4 round heads screws to the inner side and self locking nuts outside

## Step 3:

[![step 3.png](https://content.instructables.com/FCD/LJJZ/IF9TAKI4/FCDLJJZIF9TAKI4.png?frame=true&width=963&height=1024&fit=bounds)](https://content.instructables.com/FCD/LJJZ/IF9TAKI4/FCDLJJZIF9TAKI4.png)

Connect now the two preassembled links to the forward drive arm (004).

Punt in position horizontal arm (005) and triangular link (006) aligned with the upper connection of the forward drive arm (004). Insert the Ø4 mm brass pipe crossing all the parts and fix it with the M3x30 screw, locked by the nut on the other side.

Verify the freedom of movement and If everything is ok, proceed to the next step.

## Step 4: Base Assembly

[![Base Assembly](https://content.instructables.com/FU1/7DLV/IF9TAKL3/FU17DLVIF9TAKL3.png?frame=true&width=624&height=1024&fit=bounds)](https://content.instructables.com/FU1/7DLV/IF9TAKL3/FU17DLVIF9TAKL3.png)

Part list:

· n° 1 EBA\_01.00.001\_base.stl

· n° 1 EBA\_01.00.011\_round plate.stl

· n° 1 EBA\_01.00.010\_basement.stl

· n° 1 TowerPro metal gear MG90S servo with double arm horn

· n° 1 servo horn fixing screw

· n° 2 M3 x 15 screw (VTCEI)

· n° 3 M3 nuts

## Step 5:

![Immagine 5 2.png](https://content.instructables.com/F67/QN51/IF9TAKSD/F67QN51IF9TAKSD.png?width=270&auto=webp) ![Immagine 4 3.png](https://content.instructables.com/F5H/6RFY/IF9TAKSE/F5H6RFYIF9TAKSE.png?width=270&auto=webp)

[![Immagine 5 2.png](https://content.instructables.com/F67/QN51/IF9TAKSD/F67QN51IF9TAKSD.png?frame=true&width=1024&height=1024&fit=bounds)](https://content.instructables.com/F67/QN51/IF9TAKSD/F67QN51IF9TAKSD.png)

[![Immagine 4 3.png](https://content.instructables.com/F5H/6RFY/IF9TAKSE/F5H6RFYIF9TAKSE.png?frame=true&width=1024&height=1024&fit=bounds)](https://content.instructables.com/F5H/6RFY/IF9TAKSE/F5H6RFYIF9TAKSE.png)

Be sure that the servo is in the neutral position than install the double arm horn on the splined shaft keeping the arms parallel to the servo body

Insert the horn inside the housing below the round plate and fix the servo to the plate using one of the two long screw supplied with the servo (the small one in too short due to the thickness of round plate)

## Step 6:

![Immagine 7.png](https://content.instructables.com/FF3/VWTW/IF9TAKWH/FF3VWTWIF9TAKWH.png?width=270&auto=webp) ![Immagine 8.png](https://content.instructables.com/FTQ/WJUE/IF9TAKWM/FTQWJUEIF9TAKWM.png?width=270&auto=webp)

[![Immagine 7.png](https://content.instructables.com/FF3/VWTW/IF9TAKWH/FF3VWTWIF9TAKWH.png?frame=true&width=1024&height=1024&fit=bounds)](https://content.instructables.com/FF3/VWTW/IF9TAKWH/FF3VWTWIF9TAKWH.png)

[![Immagine 8.png](https://content.instructables.com/FTQ/WJUE/IF9TAKWM/FTQWJUEIF9TAKWM.png?frame=true&width=1024&height=1024&fit=bounds)](https://content.instructables.com/FTQ/WJUE/IF9TAKWM/FTQWJUEIF9TAKWM.png)

Put in position the base between the two shoulder on the plate and attach together using the two M3 screws and nuts. There two hexagonal housing below, so nuts will be kept in position during tightening

## Step 7:

![Immagine 10 2.png](https://content.instructables.com/FGU/53VS/IF9TAL28/FGU53VSIF9TAL28.png?width=270&auto=webp) ![Immagine 9.png](https://content.instructables.com/FRF/872J/IF9TAL23/FRF872JIF9TAL23.png?width=270&auto=webp) ![Immagine 11.png](https://content.instructables.com/FT9/C35L/IF9TAL84/FT9C35LIF9TAL84.png?width=270&auto=webp)

[![Immagine 10 2.png](https://content.instructables.com/FGU/53VS/IF9TAL28/FGU53VSIF9TAL28.png?frame=true&width=1024&height=1024&fit=bounds)](https://content.instructables.com/FGU/53VS/IF9TAL28/FGU53VSIF9TAL28.png)

[![Immagine 9.png](https://content.instructables.com/FRF/872J/IF9TAL23/FRF872JIF9TAL23.png?frame=true&width=345&height=1024&fit=bounds)](https://content.instructables.com/FRF/872J/IF9TAL23/FRF872JIF9TAL23.png)

[![Immagine 11.png](https://content.instructables.com/FT9/C35L/IF9TAL84/FT9C35LIF9TAL84.png?frame=true&width=345&height=1024&fit=bounds)](https://content.instructables.com/FT9/C35L/IF9TAL84/FT9C35LIF9TAL84.png)

Align the servo and introduce the wiring in the central part of the basement. Gently pull the wire to make it straight while continue to push in it housing the servo

The wire is then kept in position making it pass through a frontal hole

## Step 8: Gripper Assembly

[![Gripper Assembly](https://content.instructables.com/FF5/K2ZA/IF9UABSK/FF5K2ZAIF9UABSK.png?frame=true&width=711&height=1024&fit=bounds)](https://content.instructables.com/FF5/K2ZA/IF9UABSK/FF5K2ZAIF9UABSK.png)

Part list:

· n° 1 TowerPro metal gear MG90S servo (or SG90) with single arm horn

· n° 1 servo horn fixing screw

· n° 1 EBA\_01.00.012\_claw support.stl

· n° 1 EBA\_01.00.015\_drive gear.stl

· n° 1 EBA\_01.00.014\_left finger.stl

· n° 1 EBA\_01.00.016\_driven gear.stl

· n° 1 EBA\_01.00.013\_right finger.stl

· n° 2 M3 x 20 screw (TCEI)

· n° 3 M3 selflocking nuts

## Step 9:

[![Immagine 2.png](https://content.instructables.com/FQM/8P6M/IF9UABWP/FQM8P6MIF9UABWP.png?frame=true&width=1024&height=1024&fit=bounds)](https://content.instructables.com/FQM/8P6M/IF9UABWP/FQM8P6MIF9UABWP.png)

Attach the servo to the claw support using the two fixing screws supplied  
with the servo

Keep the output shaft forward

## Step 10:

![Immagine 7.png](https://content.instructables.com/FNW/7GAY/IF9UAC00/FNW7GAYIF9UAC00.png?width=270&auto=webp) ![Immagine 9.png](https://content.instructables.com/FKU/Q29G/IF9UAC01/FKUQ29GIF9UAC01.png?width=270&auto=webp) ![Immagine 10.png](https://content.instructables.com/FZI/ZZA3/IF9UAC16/FZIZZA3IF9UAC16.png?width=270&auto=webp)

[![Immagine 7.png](https://content.instructables.com/FNW/7GAY/IF9UAC00/FNW7GAYIF9UAC00.png?frame=true&width=1024&height=1024&fit=bounds)](https://content.instructables.com/FNW/7GAY/IF9UAC00/FNW7GAYIF9UAC00.png)

[![Immagine 9.png](https://content.instructables.com/FKU/Q29G/IF9UAC01/FKUQ29GIF9UAC01.png?frame=true&width=249&height=1024&fit=bounds)](https://content.instructables.com/FKU/Q29G/IF9UAC01/FKUQ29GIF9UAC01.png)

[![Immagine 10.png](https://content.instructables.com/FZI/ZZA3/IF9UAC16/FZIZZA3IF9UAC16.png?frame=true&width=249&height=1024&fit=bounds)](https://content.instructables.com/FZI/ZZA3/IF9UAC16/FZIZZA3IF9UAC16.png)

Insert the horn in the driven gear then attach the horn at the servo shaft using the supplied screw  
  
The horn has to be aligned forward with the servo in neutral position. Cut the exceeding part of the horn from gear using a cutter  

## Step 11:

[![Immagine 3.png](https://content.instructables.com/FRG/A3YF/IF9UACC0/FRGA3YFIF9UACC0.png?frame=true&width=567&height=1024&fit=bounds)](https://content.instructables.com/FRG/A3YF/IF9UACC0/FRGA3YFIF9UACC0.png)

Insert an M3 screw in the central hole connect it to the claw support then tight the self locking nut checking the freedom of movement

## Step 12:

![Immagine 11.png](https://content.instructables.com/F89/2FM5/IF9UACN6/F892FM5IF9UACN6.png?width=270&auto=webp) ![Immagine 12.png](https://content.instructables.com/FSY/6YAH/IF9UACPE/FSY6YAHIF9UACPE.png?width=270&auto=webp) ![Immagine 5.png](https://content.instructables.com/F07/EQL4/IF9UACPF/F07EQL4IF9UACPF.png?width=270&auto=webp) ![Immagine 4.png](https://content.instructables.com/F5X/COHG/IF9UACPL/F5XCOHGIF9UACPL.png?width=270&auto=webp)

[![Immagine 11.png](https://content.instructables.com/F89/2FM5/IF9UACN6/F892FM5IF9UACN6.png?frame=true&width=456&height=1024&fit=bounds)](https://content.instructables.com/F89/2FM5/IF9UACN6/F892FM5IF9UACN6.png)

[![Immagine 12.png](https://content.instructables.com/FSY/6YAH/IF9UACPE/FSY6YAHIF9UACPE.png?frame=true&width=193&height=1024&fit=bounds)](https://content.instructables.com/FSY/6YAH/IF9UACPE/FSY6YAHIF9UACPE.png)

[![Immagine 5.png](https://content.instructables.com/F07/EQL4/IF9UACPF/F07EQL4IF9UACPF.png?frame=true&width=193&height=1024&fit=bounds)](https://content.instructables.com/F07/EQL4/IF9UACPF/F07EQL4IF9UACPF.png)

[![Immagine 4.png](https://content.instructables.com/F5X/COHG/IF9UACPL/F5XCOHGIF9UACPL.png?frame=true&width=193&height=1024&fit=bounds)](https://content.instructables.com/F5X/COHG/IF9UACPL/F5XCOHGIF9UACPL.png)

Insert the two pin of the driven gear into the dedicated holes on the left finger The driven gear has also a shoulder that has to be aligned with the lateral side of the finger. If you find difficulties coupling them, reduce interference using a file.

Once coupled insert an M3 screw in the central hole and attach the finger to the claw support

Now the gripper is ready to be installed on the horizontal arm of the EEzybot

Verify freedom of movement of the gripper manually or using a servo tester

## Step 13: Final Assembly

[![Final Assembly](https://content.instructables.com/FAS/4SE5/IFCDDYQ4/FAS4SE5IFCDDYQ4.png?frame=true&width=963&height=1024&fit=bounds)](https://content.instructables.com/FAS/4SE5/IFCDDYQ4/FAS4SE5IFCDDYQ4.png)

Now we have the three main sub assembly ready to be connected each other.

Next step we will join the base with the main arms

## Step 14:

![Immagine 5.png](https://content.instructables.com/F4B/IOZG/IFCDDZ53/F4BIOZGIFCDDZ53.png?width=270&auto=webp) ![Immagine 7.png](https://content.instructables.com/FN3/LJHW/IFCDDZ54/FN3LJHWIFCDDZ54.png?width=270&auto=webp)

[![Immagine 5.png](https://content.instructables.com/F4B/IOZG/IFCDDZ53/F4BIOZGIFCDDZ53.png?frame=true&width=560&height=1024&fit=bounds)](https://content.instructables.com/F4B/IOZG/IFCDDZ53/F4BIOZGIFCDDZ53.png)

[![Immagine 7.png](https://content.instructables.com/FN3/LJHW/IFCDDZ54/FN3LJHWIFCDDZ54.png?frame=true&width=640&height=1024&fit=bounds)](https://content.instructables.com/FN3/LJHW/IFCDDZ54/FN3LJHWIFCDDZ54.png)

To join the base with the main arms align the axis of the parts and insert from one side the brass pipe 24mm long.

Also the short arm of the servo that drive the vertical movement has to be supported by the brass pipe as shown on the pictures.

Check the freedom of movement

## Step 15:

![Immagine 10.png](https://content.instructables.com/FR5/Y9RD/IFCDES0B/FR5Y9RDIFCDES0B.png?width=270&auto=webp) ![Immagine 11.png](https://content.instructables.com/F4B/QHEA/IFCDE9KK/F4BQHEAIFCDE9KK.png?width=270&auto=webp)

[![Immagine 10.png](https://content.instructables.com/FR5/Y9RD/IFCDES0B/FR5Y9RDIFCDES0B.png?frame=true&width=600&height=1024&fit=bounds)](https://content.instructables.com/FR5/Y9RD/IFCDES0B/FR5Y9RDIFCDES0B.png)

[![Immagine 11.png](https://content.instructables.com/F4B/QHEA/IFCDE9KK/F4BQHEAIFCDE9KK.png?frame=true&width=600&height=1024&fit=bounds)](https://content.instructables.com/F4B/QHEA/IFCDE9KK/F4BQHEAIFCDE9KK.png)

Is time now to install the servo that drive the vertical movement of the arm. Put in the dedicate receptacles two M3x10 hex screw. The servo has to be in the neutral position with the horn at 90 degrees on the right side with the press plate (009) installed (Make the wiring pass through the dedicated enlargment).

Introduce the servo angled in the square seat on the base plate and slide the horn in the shaped housing of the arm that drives the vertical movement. Fixt the press plate against the servo using two M3 nuts

## Step 16: Fwd/bckw Drive Servo

[![Fwd/bckw Drive Servo](https://content.instructables.com/FXC/7BHE/IFCDESJ5/FXC7BHEIFCDESJ5.png?frame=true&width=600&height=1024&fit=bounds)](https://content.instructables.com/FXC/7BHE/IFCDESJ5/FXC7BHEIFCDESJ5.png)Sequence for the forward&backward driving servo is similar to the previous. In this case the servo horn has to be installed with the servo in neutral condition aligned vertically.

## Step 17: Last Link

[![Last Link](https://content.instructables.com/FHS/M7TQ/IFCDESMO/FHSM7TQIFCDESMO.png?frame=true&width=963&height=1024&fit=bounds)](https://content.instructables.com/FHS/M7TQ/IFCDESMO/FHSM7TQIFCDESMO.png)

attach the latest link to the fixed arm on the rear side of the base using a M4x20 a washer and a selflocking nut

## Step 18: Attaching the Gripper

[![Attaching the Gripper](https://content.instructables.com/FN9/XT1X/IFCDESTT/FN9XT1XIFCDESTT.png?frame=true&width=963&height=1024&fit=bounds)](https://content.instructables.com/FN9/XT1X/IFCDESTT/FN9XT1XIFCDESTT.png)

The last assembly step is to join the gripper to the horizontal arm as shown on the picture.

## Step 19: Making It Works

[![Making It Works](https://content.instructables.com/FSK/DBJN/IFCDFC3H/FSKDBJNIFCDFC3H.jpg?frame=true&width=525&height=1024&fit=bounds)](https://content.instructables.com/FSK/DBJN/IFCDFC3H/FSKDBJNIFCDFC3H.jpg)At the end of the last step the ARM is ready to work.  
  
As an optional, In the 3D model downodable from Thinghiverse, I add a round ramp that allow to easy obtain a loop test with a ball (3D printed, obviously!). In the video linked on first page is shown what I mean.  
  
To make this tool to work you have to attach another servo (cheap SG90) to the end of the ramp. I keep th ramp center at a distance of about 180mm from the base vertical axis.  
  
There is also a 3D model of a support dedicated to the Pololu USB servo.  
  
The way to drive the servo are several. I tried them pretty all. To explain it will take to much and this instructable is big enough..... probably I'll make a new instructables dedicated, If I get time. Anyway if you want to explore there are quite enough material around the web.  
  
As told at the beginning, I found very easy using a Pololu USB servo Mini Maestro, it is not very cheap but solve a lot of problems. You have to install drivers, a software and when connected to usb you're are immediately able to drive the servos choosing their speed and acceleration also. You can store the servo position to a sequence and when ready it can be played once or in a loop. Can also be stored in the internal script memory and it can be automatically played without computer connected.