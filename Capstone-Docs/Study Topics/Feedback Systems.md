#theory #control 

During our project, we also reviewed control systems with reference to [Feedback Systems Textbook](Documents/Feedback_Systems_Textbook.pdf). Notes on each chapter are linked below in our table of contents which follows the feedback systems table of contents.

## Table of Contents
Chapter 1: [[Feedback Loops]]
Chapter 2: [[System Dynamics and Modeling]]
Chapter 3: [[System Modeling Examples]]
Chapter 10: [[PID Control]]

## Introduction

The term feedback refers to the influence of two or more dynamical systems have on each other when they strongly coupled. The first system impacts on the the second system and vice-versa, which created a circular argument. This can have a counterintuitive consequence, in order to understand them it is necessary to resort to formal methods ([1](Documents/Feedback_Systems_Textbook.pdf) ). A closed loop system refers to systems interconnected in a cycle. In an open loop system the interconnection is broken.

Feedback can be exploited in designing systems. Generally, they are used to make systems resilient toward external influences, create linear behavior out of nonlinear components, or more generally, allows the system to be insensitive both to external disturbances and to variations in its individual elements. Those are the goals we have for our Pi Car project: we will be using the data that our sensors collect on the external disturbances such as the slip of its tires, and its internal variations such as its speed and acceleration in order to build a control system.

## Control system

Control engineering rely on dynamics modelling, information, software and operations research. A control system combines feedback loop sensing, computation and actuation of a dynamical system in order to create good disturbance attenuation, fast responsiveness to changed in operation point, etc. These properties are established through modeling and analysis techniques, such as system identification, to capture the essential dynamiccs of our system. This permits us to explore and predict as many possible behaviors with the consequences of uncertainty, noise and component failure that can impact our system.

## PID control

A PID controller is used to solve a wide range of control problems. This algorithm consists of three coefficients: proportional, integral and derivative which are dtermined to get an optimal response. The proportional control uses the proportionality between the characteristics of the controller to the control error for small errors. The proportional band of the controller is linear when the error is in the interval: $e_{min} \le e \le e_{max}$. The controller gain $k_p$ can be determined as:
$$
u = k_p(r-y) = k_pe
$$
The proportional control has the drawback of creating an oscillation which could make the system unstable. For the system to maintain a desired value, the integral control is implemented.
