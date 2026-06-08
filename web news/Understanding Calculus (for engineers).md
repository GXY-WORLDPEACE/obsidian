---
title: "Understanding Calculus (for engineers)"
source: "https://www.youtube.com/watch?v=C9oWXIs2g3Y"
author:
  - "[[The Efficient Engineer]]"
published: 2025-11-18
created: 2026-06-08
description: "Go to https://brilliant.org/efficientengineer/ to try out the Brilliant course on Calculus for some hands-on learning. You can use this link to get 20% of an annual membership!--This video explore"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=C9oWXIs2g3Y)

Go to https://brilliant.org/efficientengineer/ to try out the Brilliant course on Calculus for some hands-on learning. You can use this link to get 20% of an annual membership!  
  
\--  
  
This video explores one of the most powerful tools in engineering - calculus. By looking at how quantities change and how those changes accumulate, calculus helps describe and predict physical behaviour. In this video we work through the core ideas of calculus, from differentiation and integration through to differential equations and numerical methods, but with an engineering focus, linking the mathematics back to real-world physical behaviours.

## Transcript

**0:00** · Calculus is a fundamental tool in engineering. It helps us stabilize drones in flight. Predict how structures deform under load. Analyse transient behavior in electrical circuits. And model the dynamics of vibrating systems. In all of these cases, we're asking the same fundamental question - how does the system respond when something changes? Calculus is how we answer that question - it's the mathematical study of change. In this video we'll explore the key principles of calculus, and discover exactly how they apply to real-world engineering problems.

**0:28** · The easiest way to understand how one quantity is affected by changes to another is by plotting both on a graph. The slope of the graph - represented by a tangent line that just touches the curve - is a key piece of information. It tells us how sensitive one quantity is to another. And that sensitivity changes depending on where we are on the curve. The slope often has a real, physical meaning.

**1:00** · If the graph shows displacement on the horizontal axis and force on the vertical axis, the slope represents the stiffness of the object, like the stiffness of a spring for example. If the graph shows velocity versus time, the slope is acceleration. And if it shows voltage versus current, the slope is electrical resistance. To understand how to extract this slope information in a systematic way, let's look at a simple example: the function Y equals X-cubed. Say we want to calculate the slope of this curve at a particular point.

**1:33** · One way to approximate it is to pick another point slightly to the right, at X plus a small amount that we'll call Delta-X.

**1:46** · The straight line between these two points gives us an estimate of the slope of the curve at this position. It has a slope equal to the change in Y divided by the change in X. Now imagine moving the two points closer together - shrinking Delta-X towards zero. As the points get closer, the line connecting them becomes a better and better approximation of the tangent at the point. And as Delta-X tends towards zero, the line between the two points becomes the true tangent, giving us the exact slope at that point.

**2:18** · By expanding the slope equation and taking the limit as Delta-X tends towards zero, we obtain an equation that gives us the slope of our x^3 function at any point X. As expected, this slope function has a value of zero at X equals zero, where the X-cubed curve is flat, and it increases as we move to the left or the right, where the slope of the X-cubed curve becomes steeper.

**2:51** · What we've just done - figuring out the equation that gives us the slope of the function y=x^3 - is called finding the derivative of the function. The derivative is written as dy/dx - it represents the change in Y per change in X. It can also be written as F-prime-of-X, or Y-prime.

**3:13** · In this function, X is the independent variable - the input we can choose - and Y is the dependent variable, the output that depends on our choice of X. We can use any variable names here. The independent variable is often T, for example, in which case DY-over-DT represents how quickly the quantity Y changes with time.

**3:44** · When the independent variable is time, the dot notation is often used to represent derivatives.

**3:52** · The approach we just used - starting with a line between two points on the curve and taking the limit as Delta-X approaches zero - is a process called "differentiating from first principles".

**4:03** · It's the underlying basis of differential calculus. But in practice, engineers rarely do this from scratch. We just saw that the derivative of x^3 is 3x^2 This pattern isn't unique to that one function - it works for any function of the form "X to the power of N". The derivative is obtained by multiplying by the power and reducing that power by one. Instead of deriving everything from scratch, engineers use tables of standard derivatives for the functions we see again and again, like sine, cosine, exponential functions or square root functions.

**4:37** · Let's look at a few examples. The derivative of a constant value is zero, because it has no slope. And a straight line has a constant slope, so its derivative is a constant value. Sine and cosine functions appear all the time in engineering, especially in systems that vary cyclically with time, like alternating current circuits. This graph shows sine-of-X. At the peaks, where the function reaches a maximum, the slope is zero.

**5:15** · And where the curve crosses the horizontal axis, the slope is at its steepest, corresponding to either its minimum, or maximum value. The derivative of sine-of-X is cosine-of-X. Similarly, the derivative of cosine-of-X is "negative sine-of-X".

**5:36** · The negative is needed for the slope to have the correct sign - positive where cosine is rising, and negative where it's falling. Another important function is the exponential function.

**5:55** · What makes it remarkable is that, at every point, the slope is exactly equal to the value of the function itself - the larger the value, the faster it grows. Exponential behavior shows up whenever the rate of change of a quantity depends on how much of that quantity already exists, like the charge building up in a capacitor, or radioactive decay, where more atoms means more decay events. In most engineering applications, we're not dealing with a single, simple function, but a combination of more complicated functions.

**6:26** · Fortunately, a few straightforward rules save us from having to differentiate from first principles every time. The first is the linearity rule. When two functions are added together, the derivative of the whole function is just the sum of the derivatives of the two individual functions. This doesn't work when the functions are multiplied together though, because when both functions are changing, their rates of change interact.

**6:56** · In these cases, the product rule needs to be used - the derivative of the product of two functions U and V is the derivative of U multiplied by V, plus U multiplied by the derivative of V.

**7:10** · Similarly the quotient rule should be used when one function is divided by another. And finally there's the chain rule. To find the derivative when one function is nested inside another, you differentiate the outer function as if the inner part were just a single variable, and multiply it by the derivative of the inner function. Here's an example, where the inner function U is 3x, and the outer function V is sine-of-U.

**7:36** · The derivative of this function is equal to the derivative of V with respect to U - which is cosine of U - multiplied by the derivative of U. Having 3x inside the sine term instead of just X means that, as X increases, the input to the sine curve increases three times faster. This makes the slope of the curve three times steeper at every point, which is why you need to multiply by the derivative of U to get the correct slope.

**8:16** · With these four simple rules and the table of derivatives for common functions, you can differentiate a huge range of complicated functions relatively easily.

**8:33** · The derivative gives us a really useful tool for exploring the behavior of a function.

**8:38** · If we plot this function on a graph, for example, you'll notice that wherever the derivative is zero, the function is at a local minimum or maximum. This happens because the slope of the curve goes from being negative to being positive at a minimum, and from being positive to negative at a maximum. In both cases the slope must pass through zero at the turning point. This is a powerful application of calculus - if we want to find the maximum or minimum values of a function, we can just take its derivative and find where it's equal to zero.

**9:08** · These points where the slope of a curve becomes flat are called stationary points. To figure out if a stationary point is a maximum or a minimum, all we need to do is look at how the slope itself changes around that point.

**9:29** · And we can do that by taking the derivative of the derivative, which is called the second derivative.

**9:36** · The second derivative tells us about the curvature of the function. If it's positive, the derivative has a positive slope, so the curve is bending upwards, which means we're at a local minimum. And if it's negative, the derivative has a negative slope, so the curve bends downwards and we're at a local maximum. There's a third type of stationary point called an inflection point, where the curve doesn't turn back on itself, but its curvature reverses.

**10:04** · At a stationary inflection point, both the first and second derivatives are zero, and the second derivative changes sign, to reflect the curvature reversal. Now let's see why this matters in the real world. Imagine a function that represents the temperature along a nuclear fuel rod. We want to model how this temperature distribution changes over time. This can be done using the heat equation.

**10:29** · It tells us that the rate at which temperature changes over time depends on a material property, called thermal diffusivity, and how temperature is distributed along the rod, represented by the second derivative of temperature with respect to the position X. The second derivative appears in the equation, because heat will flow away from local hot spots, where the second derivative is negative, toward cooler regions where the second derivative is positive.

**11:00** · It's the second derivative that determines the direction of heat flow. Many physical processes follow similar laws, where quantities spread over time from regions of high to low concentration.

**11:18** · Fick's second law of diffusion, for example, is used to model the movement of atoms in a solid, or the dispersion of contaminants in a liquid. In all such cases, calculus provides the framework for modelling how these quantities change over time. You might have noticed that these equations use a slightly different notation for the derivative. So far we've only discussed derivatives of functions that depend on one variable, like time or position. But many real-world quantities depend on two variables, or more.

**11:50** · The curly D symbol tells us we're taking a partial derivative, which means we're looking at how temperature changes with respect to one variable, while holding the other constant. The partial derivative of temperature with respect to time describes how the temperature at any fixed point on the rod changes with time. And the partial derivative with respect to position describes how temperature varies along the length of the rod at a single instant in time.

**12:20** · Take a simple function that depends on variables X and T. To take the partial derivative with respect to X, we differentiate by considering T to be a constant. And to take the partial derivative with respect to T, we consider X to be a constant. Differentiation takes a function and gives you the rate of change as you move along it. In some cases, though, the rate of change is what we already know, and we want to figure out the function itself.

**12:53** · Imagine a function that tells you how some quantity changes with time - a power consumption curve for an electric motor, for example. It shows higher power consumption during start-up and lower consumption during steady operation. Power is the rate at which energy is consumed, measured in joules per second, so this curve effectively represents the derivative of the total energy consumption with respect to time. To figure out the total energy consumed over a set time period, we need to add up all of the small instantaneous changes.

**13:28** · This process - accumulating all these infinitesimal changes to find the total quantity - is called integration. It's the reverse of differentiation.

**13:43** · Graphically, integration corresponds to finding the area under a curve. To see why this is, imagine dividing the region under the curve into loads of thin vertical rectangles. Each rectangle has a width that corresponds to a small change in X, and a height equal to the value of the curve at that X, and so the rectangle approximates a tiny contribution to the total.

**14:08** · 1300 Joules per second consumed over 0.1 seconds is 130 Joules. To obtain the total accumulated quantity up to a certain point, you just add up all of the tiny contributions up to that point.

**14:25** · As you make the rectangles thinner and thinner, you get closer to the exact area under the curve.

**14:34** · Mathematically integration is represented using the integral symbol. This means "integrate the function F with respect to X". The result is a new function, the antiderivative, that gives you the total amount accumulated as a function of X. When limits are added to the integral symbol, they define the interval over which you're integrating, which is equivalent to calculating the total accumulated change from X equals A to X equals B. Because integration is the reverse of differentiation, we can use the same lookup tables to integrate a function.

**15:13** · To integrate X to the power of 4, for example, we add 1 to the power, giving us X to the power of 5.

**15:20** · We also need to divide by the new power, otherwise we would end up with "5 times X to the power of 4" when differentiating. One important thing to realize is that information is lost when differentiating, because any constant terms have a slope of zero. These two functions are parallel curves with identical slopes at every point, just shifted up and down, so they differentiate to the same thing, X to the power of 4.

**15:45** · For this reason, when integrating, an additional term - the constant of integration - needs to be added to account for any constant that might have been lost. If we know the value of the original function at a particular point, we can use that to find the value of C. And with the antiderivative now defined, we can calculate the integral between two limits by taking its value at the upper limit and subtracting its value at the lower limit.

**16:23** · You don't actually need to know the constant of integration when calculating an integral between two limits, because it cancels out when taking the difference between the upper and lower limits. Like differentiation, integration has certain rules that help when integrating more complicated functions. One of the most useful is called integration by parts, which helps integrate the product of two functions - it's the reverse of the product rule for differentiation. Say you want to integrate "X times cosine of X".

**16:54** · You split the function into two parts, U and V, and choose one part to differentiate and the other to integrate. By using the "integration by parts" formula to rewrite the integral, you end up with something that's much easier to solve. This method works really well if one part of the function is easy to differentiate and the other is easy to integrate.

**17:28** · Another important technique is integration by substitution. It's used when the integral can be written in a form that includes an outer function, an inner function, and the derivative of that inner function. A simplified form of the integral can be obtained by substituting the inner function for a new variable, U. This can easily be integrated with respect to U.

**17:44** · And substituting the expression for U back in gives the final answer in terms of the original variable, X. Integration by substitution is essentially just the reverse of the chain rule. In the real world, the behavior of an engineering system is rarely governed by a single neat function.

**18:18** · More often, it depends on how certain parameters change with respect to others, and so these systems tend to be governed by differential equations - equations that define the relationship between a quantity and its derivatives. Equations like these appear everywhere in the physical world. Take a cable suspended between two points under its own weight. The shape the cable settles into is governed by a differential equation, derived by considering the balance of the forces acting on it.

**18:50** · The equation depends on the first and second derivatives of Y, where X and Y represent the horizontal and vertical positions of the cable - as well as on the cable's weight per unit length, and the tension within it. Solving the differential equation gives you the very specific shape adopted by the cable, which is called a catenary. Another example is the deflected shape of a beam.

**19:22** · When a load is applied, the beam deforms in a way that satisfies a differential equation. The second derivative of the vertical deflection, Y, with respect to the distance along the beam, X, represents the curvature of the beam. At any point along the beam this curvature depends on the bending moment at that location - produced by the applied load - and on two parameters that describe the beam's stiffness - the Young's modulus E, a measure of the material's stiffness, and the second moment of area I, which reflects how the beam's cross-section resists bending.

**19:52** · Mechanical and civil engineers use this differential equation all the time to design and analyse structures.

**20:08** · Differential equations often appear in vibration problems. The vibrational behavior of mechanical systems is often represented by a simple model consisting of a mass connected to a spring and a damper. The model captures how real structures or components oscillate in response to disturbances.

**20:28** · The vertical position of the mass X with respect to time depends on the forces acting on the mass, and the balance of these forces is governed by a differential equation. Each term in the equation corresponds to a physical effect - the inertial force is proportional to acceleration, the damping force is proportional to velocity, and the spring restoring force is proportional to position. Electrical systems can also be described using differential equations. Take an RLC circuit, which contains a resistor, an inductor, and a capacitor connected in series.

**21:03** · Because the inductor and capacitor store energy, the current doesn't respond instantly when a voltage is applied. Instead, the charge Q builds up or discharges over time in a way that's governed by a differential equation. Each term on the left side of the equation represents the voltage drop across one of the components, and the term on the right side represents the applied voltage. As you can see, differential equations appear everywhere in engineering, and take many different forms.

**21:37** · To analyse them effectively, we need to understand the different types of equations and how they're classified. If the equation involves the first derivative of a function it's a first order differential equation. If it includes second derivatives, it's second order. Third order differential equations contain third derivatives, and so on. If the equation contains derivatives with respect to just one independent variable, it's called an ordinary differential equation.

**22:08** · If it has two or more - like the heat equation we saw earlier - it's a partial differential equation. An equation is non-linear if the dependent variable or its derivatives are raised to a power, multiplied by each other, or appear inside non-linear functions, like sine or exponential functions.

**22:34** · It's non-homogeneous if there's a term that doesn't include the variable or its derivatives, meaning the whole equation would be non-zero if the dependent variable was set to zero. And it's autonomous if the independent variable doesn't appear in the equation, and no terms depend on it. In systems defined by autonomous equations, the evolution of the system only depends on the current state of the system, not on the independent variable itself.

**23:07** · These categories aren't mutually exclusive - here's an example of a second-order, ordinary, non-linear, non-homogeneous, non-autonomous differential equation. The damped vibration equation we saw earlier is a second-order, ordinary, linear, homogeneous, autonomous differential equation. It's homogeneous because every term in the equation involves the displacement X or its derivatives.

**23:32** · Physically, this means the equation describes the system's natural response - how the mass oscillates and eventually comes to rest without any external force acting on it. If a time-dependent external force is applied to the mass, producing forced vibration, the system is no longer self-determined - it's driven by the applied force. The resulting equation is non-homogeneous, because it includes an external forcing term. It's also non-autonomous because the independent variable, time, now appears in the equation.

**24:08** · Solving a differential equation is the process of finding the unknown function that satisfies the equation, and meets any boundary or initial conditions. It's a huge topic, so for this video let's just touch on a few common solution methods.

**24:28** · Direct integration is used when a derivative of any order appears by itself on one side of the equation, and the other side depends only on the independent variable. This is the case for the beam equation, because the second order derivative is on the left side of the equation, and the terms on the right are either constants or known quantities that depend on X. In other words the equation only contains one derivative term, and the unknown variable Y doesn't appear separately.

**24:59** · To solve the equation all we need to do is integrate until we obtain Y. For the beam equation that means integrating twice. For this example E and I are constants, and the bending moment is equal to minus P times X. Each integration reduces the order by one and introduces a constant of integration. The constants can be found by applying the boundary conditions. This gives us the deflected shape of the beam. The "Separation of Variables" method is a bit more versatile.

**25:44** · It's usually applied to first-order equations that contain both the dependent and independent variables. The idea is to re-arrange the equation so that all terms involving the dependent variable, including its differential - DY in this case - are on one side, and all terms involving the independent variable and its differential DX, are on the other. Once separated, both sides can be integrated independently, and the equation can be rearranged or simplified to obtain the solution. Here's a quick example, where the derivative DY-over-DX is equal to X squared times Y. Separating the variables and integrating both sides gives an equation for Y.

**26:39** · There are loads of other techniques for solving differential equations - too many to cover here - like the integrating factor method, complementary and particular solutions, the Laplace transform approach, and more. Even so, many real world equations can't be solved - either the math becomes far too complex, or an analytical solution just doesn't exist.

**27:02** · This is often the case for non-linear equations. A well-known example is the Navier-Stokes equations, which describe the motion of fluids. This system of partial non-linear differential equations has no analytical solution. Part of the reason it's so difficult to solve is the non-linear part of the inertial term, where the fluid's velocity at a point depends on how the velocity varies spatially around that point.

**27:26** · For equations like this one that are difficult or impossible to solve, engineers use numerical methods - methods that find approximate solutions by iteratively calculating the value of a function in small steps. The entire field of computational fluid dynamics is based on applying approximate numerical methods and a lot of computing power to the Navier-Stokes equations, to simulate fluid flow.

**28:00** · One of the simplest numerical methods is Euler's method. Say you're working with a differential equation that describes how a cell population in a bioreactor grows over time. The rate at which the population grows depends on its current size, how near it is to the maximum population the environment can sustain, and on a growth rate constant.

**28:24** · If you can't solve the equation directly to find the population size as a function of time, you can estimate it using Euler's method instead. You start from an initial value, in this case a population size of 1 at time zero. By repeatedly calculating the slope of the curve from the differential equation, multiplying that slope by a chosen time step, and adding the result to the previous value, you can gradually trace out an approximate solution to the equation.

**29:06** · The smaller the step size you use, the closer this approximation becomes to the exact solution. More advanced numerical techniques like the Runge-Kutta method can get you even closer to the exact solution.

**29:24** · One really important engineering application of calculus is in control systems - systems that manage the behavior of a machine or device, using feedback and sensor data to achieve a desired outcome. Say you want to design a system that can maneuver and stabilize a quadcopter. First, you need to understand the physics that govern its motion. Let's focus on adjusting the pitch angle - which tilts the drone forwards and backwards.

**29:53** · This is done by changing the relative thrust of the front and rear motor pairs. If the rear motors spin slightly faster than the front ones, they generate more upward thrust, producing a torque that causes the drone to pitch forwards. The relationship between this torque and the resulting pitch angle is described by a differential equation. The second derivative of the pitch angle with respect to time, which is angular acceleration, depends on the applied torque and the drone's mass moment of inertia about the pitch axis. This equation provides the foundation for simulating the drone's motion.

**30:27** · By integrating it twice with respect to time, we can calculate how the pitch angle changes as the motor speeds, and so the torque, are adjusted.

**30:39** · Similar equations can be derived for the roll and yaw axes as well. These equations form part of the mathematical model of the drone - a model engineers use during the design phase to simulate its behavior and fine-tune the control system parameters. In flight, the on-board flight controller uses sensor feedback to track how the drone is moving, and makes adjustments through a feedback loop, implemented by an algorithm called a PID controller. Here again calculus plays a key role.

**31:11** · The controller continuously calculates the error between where the drone is and where it should be, and adjusts the motor speeds to reduce the error. The PID controller has three parts.

**31:26** · The proportional term reacts to the current error - a larger error produces a stronger correction.

**31:33** · The integral term takes the integral of the error over time, increasing the correction whenever an error persists, to eliminate steady drift. And the derivative term takes the derivative of the error with respect to time, responding to how quickly the error is changing to dampen oscillations and avoid overshoot. Without calculus and differential equations, it would be impossible to simulate a drone's behavior, or design a controller capable of keeping it stable in flight.

**31:59** · We've covered a lot of ground in this video, but if you want to take it a step further, I highly recommend you check out this video's sponsor, Brilliant, download their app, and work through their course on calculus. It's the perfect companion to this video, and will help you cement your understanding of the concepts we've been exploring, not by watching, but by doing. Brilliant is a learning app built around active problem solving.

**32:25** · Instead of taking in information passively, you dive into fun interactive lessons that challenge you to think about new concepts and test your understanding as you go. This hands-on approach is incredibly effective, because you're building intuition and understanding through practice.

**32:44** · Beyond calculus, Brilliant has a huge range of courses covering science, logic, programming, data analysis, and even how AI works - all designed to help you develop strong analytical and problem-solving skills. Each course is split into bite-sized, interactive lessons you can work through at your own pace, with visual explanations, guided problems, and instant feedback that will keep you engaged as you learn.

**33:15** · All engineers need to know how to problem-solve effectively, but it's not really something you can learn from a textbook or a video. It's a skill that's developed by tackling problems, making mistakes, and building intuition over time. And that's exactly what Brilliant is designed for. To get started for free, go to brilliant.org/efficientengineer, click the link in the description, or scan the QR code.

**33:39** · And if you decide to sign up for the annual Premium subscription for unlimited daily access to everything on Brilliant, the link will give you a 20% discount. And that's it for this look at calculus. Thanks for watching!