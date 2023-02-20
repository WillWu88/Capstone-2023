- Introduces the concept of observability and show that if a system is observable, it is possible to recover the state from measurements of the inputs and outputs to the system

### 7.1 Observability

- It will be shown that computation of the states can be carried out by a dynamical system called an observer.

#### Definition of Observability

- An observer uses the process measurement y, possibly corrupted by noise n and the input u to estimate the current state of the process.

- *Observability*: A linear system is observable if for any $T > 0$ it is possible to determine the state of the system x(T) through measurements of y(t) and u(t) on the interval (0,T).

- If a system is observable, then there are no "hidden" dynamics inside it; we can understand everything that is going on through observation (over time) of the inputs and outputs.

- *Sensor Fusion* is the process of reconciling signals from many sensors with mathematical models.

#### Testing for Observability

- We wish to understand when it is possible to determine the state from observatons of the output.

- The output itself gives the projection of the state on vectors that are rows of the matrix C.

- It turns out that we need not consider any derivatives higher than n-1

- The calculation can easily be extended to systems with inputs.

- The state is then given by a linear combination of inputs and outputs and their higher derivatives.
	- The observability criterion is unchanged.

- Theorem 7.1: (*Observability rank condition*) A linear system of the form is observable if and only if the observability matrix $W_o$ is full rank.

- Example 7.1 Compartment model pg 215

#### Observable Canonical Form

- As in the case of reachability, it turns out that if a system is observable then there always exists a transformation T that converts the system into observable canonical form.

### 7.2 State Estimation

- We will look for observers that can be represented as a linear dynamical system that takes the inputs and outputs of a system we are observing and produces an estimate of the system's state.

#### The Observer

- We can attempt to determine the state simply by simulating the qeuations with the correct input.

- When both the observer and estimator are going to 0 we must require that the system be stable, and essentially our estimator converges.
	- Not useful in a control design context since we want to have our estimator converge quicky to a nonzero state s that we can make use of it in our controller.

- The observer design problem is the dual of the state feedback design problem.

- Theorem 7.2 (Observer design by eigenvalue assinment).
	- *Consider the system given by* $dx/dt = Ax + Bu$ $y=Cx$ *with one input and one output. Let* $lamba(s) = s^{n} + a_{1}s^{n-1}+ ... +a_{n-1}s + a_{n}$ *be the characeristic polynomial for A. If the system is observable, then the dynamical system* $dx_{hat}/dt = Ax_{hat} + Bu + L(y-C*x_{hat}$ *is an observer for the system, with L chosen as ..* see page 220 for matricies.

- $dx_{hat}/dt = Ax_{hat} + Bu + L(y-C*x_{hat}$ is called an observer for (the states of) the system because it will generate an approimation of the states of the  system from its inputs and outputs.
	- The form of an observer is a much more useful form than the one given by pure differentiation in equation.

- Example 7.2 Compartment model page 220

- The observer gain L is a matrix that tells how the error e is weighted and distributed among the states.
	- The observer thus combines measurements with a dynamical model of the system.

#### Computing the Observer Gain 

- For simple low-order problems it is convenient to introduce the elements of the observer gain L as unknown parameters and solve for the values required to give the desired characteristic polynomial.

- Book example 7.3 Vehicle steering pg 221

### 7.3 Control Using Estimated State

- Theorem 7.3 (Eigenvalue assignment by output feedback)
	- *This polynomcial can be assigned arbitrary roots if the system is reachable and observable*

- The controller has a strong intitive appeal: it can be thought of as being composed of two parts, one state feedback and one observer.

- The feedback gain K can be computed as if all state variables can be measured , and it depends only on A and B.

- The property that the eigenvalue assignment for output feedback can be seperated into an eigenvalue assignment for a state feedback and an observer is called the *seperation principle*

- *Internal model principle*: the controller contains a codel of the process being controlled.

- Book example 7.4 Vehicle Steering pg 226

### 7.4 Kalman Filtering

