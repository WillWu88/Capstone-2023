## -Simultaneous Localization and Mapping
#theory #navigation 
[Source](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping)
Simultaneous localization and mapping(SLAM) refers to the computational problem of creating/updating a map of an unknown environment, while also keeping track of a moving object's(car, boat, drone) location within it. 

## Mathematical description of the Problem

The SLAM problem aims to utiliize a given series of controls and sensor observations over discrete time steps, in order to compute an estimate of the moving object's state and map its environment. 

Like many inference problems, a local optimum solution can be found for the inferences of two variables at the same time, by aternating which variable is updated in an expectation-maximization algorithm. 

## Algorithms

Statistical techniques used to approximate the equations used in SLAM include Kalman filters and particle filters. These are used in conjuction in order to give an estimation of the posterior probability distribution for the position of the robot and for the map parameters. 

New SLAM algorithms are an active research area, and often consist of different requirements and assumptions about the types of maps, sensors, and models(further covered below).

### Mapping

Topological maps, or maps that emphasize capturing the connectivity(topology) of the environment rather than a geometrically accurate map are used in SLAM algorithms in order to enforce global consistency. 

Grid maps use arrays to represent the topological world, making inferences about which cells are occupied. 

Modern self driving cars utilize highly detailed maps collected in advance to simplify the mapping problem.

### Sensing

SLAM will continuously use several different types of sensors, and the powers and limits of various sensor types have been a major driver of new algorithms.

Different types of sensors give rise to different SLAM algorithms which assumptions are most appropriate to the sensors. 

At one extreme, laser scans or visual features provide details of many points within an area. At the other extreme, tactile sensors are extremely sparse as they contain only information about points very close to the agent. 

Sensor models divide broadly into landmark-based and raw-data approaches. Landmarks are uniquely identifiable objects in the world which location can be estimated by a sensor. Whereas, in raw-data approaches the model wotks directly as a function of the location, making no assumptions that landmarks can be found. 

For some outdoor applications, the need for SLAM has been almost completely eliminated because of high precision differential GPS sensors. 