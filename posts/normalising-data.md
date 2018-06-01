Categories: algorithm
Tags: normalise

## Normalising Data ##


### Simple Scaling ###

      $latex x'=\frac{{\displaystyle x-x_{min}}}{{\displaystyle x_{max}-x_{min}}} $

### Normalisation ###


      $latex x'=\frac{{\displaystyle x-\bar{x}}}{{\displaystyle s}} $

where: 

      $latex \bar{x}=\frac{{\displaystyle \sum x}}{{\displaystyle n}} $

and:

      $latex s=\sqrt{\frac{{\displaystyle \sum(x_{i}-x)^{2}}}{{\displaystyle n-1}}} $

### Squashing Functions ###

- Used in activation functions of NN's.

#### Logistic

        $latex \frac{1}{{\displaystyle 1+e^{-x}}} $

- Steep gradient.
- Symmetric about x=0,y=0.5.
- Usable range 0.1 < x < 0.9.


#### TanH ####

        $latex tanh(x) $

- Steep gradient.
- Symmetric about x=0,y=0.
- Usable range -0.95 < x < 0.95







