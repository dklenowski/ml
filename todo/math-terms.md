Categories: maths
Tags: population
      dynamic
      deterministic
      stochastic
      steady
      map


## Dynamical System

- Set of possible states and rule that determines present state in terms of past states.

## Deterministic

- Can determine present state from past states.

## Random/Stochastic Process/System

- Opposite of dynamic deterministic system.

## Steady State

- Approaches a finite limit.

## Map

- A function whose domain (input) and range (output) space are the same is called a map.
- e.g. let x be a point and f be a map, then orbit of x under f is the set of points

$latex \{x,f(x),f^{2}(x),....\}$

- The initial rate of orbit - starting point p is a fixed point of map if

$latex f(p)=p$

e.g.

$latex g(x)=2x(1-x)$

- from the real line to itself is called a map.
- The orbit of x=0.01 under g is

$latex \{0.01,0.0198,0.0038,...\}$

- The fixed points of g are x=0 and x=0.5

## Example Dynamical and Deterministic System

### Population bacteria.

    x - Population of bacteria.
    f(x) - Population of bacteria 1 hour later.
    t=0, x=10000
    t=1 f(x)=2x=20000
    t=2 f(x)=40000
    t=3 f(x)=80000

- In general:

$latex x_{n}=f(x_{n-1})=2x_{n-1}$

- where n is time and:

$latex x_{n}$ - Population at time t

- let:

$latex f^{2}(x)=f(f(x_{0}))$

- e.g.

$latex x_{0}$

$latex x_{1}=f(x_{1})=f(x_{0})$

$latex x_{2}=f(x_{2})=f(x_{1})=f(f(x_{0}))$

then in general:

$latex f^{k}(x)$ - Applying f to initial state k times