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

