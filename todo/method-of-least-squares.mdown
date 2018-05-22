Categories: maths
Tags: curve
      fitting
      least
      squares
      adaptive
      linear

## Method of Least Squares ##

- Basically a model of how well the "observed data" fits the model that has been defined.
- e.g. consider fitting some observed data $latex (x\_{i}, y\_{i}) $ against a linear model $latex f(x\_{i})=a+bx\_{i} $.

<!-- least-squares-graph.png -->
![Least Squares](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6WEo2aW12dmdTLVU "Least Squares")

- The "sum of squared error" is defined as:

      $latex E={\displaystyle \sum\_{i=1}^{n}\left[f(x\_{i})-y\_{i}\right]^{2}} $

- Note, we square the error to get a positive value.
- The smaller the $latex E $, the better the graph matches the data.
- The linear model that minimises $latex E $ is called the last square regression line.

## Robbins-Munro Stochastic Approximation (RMSA) ##

- **Optimisation**
  - Solution is the set of parameter values values that minimises a given performance index/objective function.
- **Stochastic Approximation**
  - Practical method of approximate optimisation.

### Adaptive Linear Element ###

<!-- adaptive-linear-element.png -->
![Adaptive Linear Element](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6VVpzbzZFZkJtTHM "Adaptive Linear Element")

### Input Signal Vector ###

      $latex x=\left[{\displaystyle \varepsilon_{1}},\varepsilon_{2}..,\varepsilon_{n}\right]^{T}\epsilon\,\Re^{n} $

- where:
  - $latex \\{\varepsilon\_{j}\\} $ - Real value scalar signals (inputs).
  - $latex x $ - Stochastic variable (Vector).

- Assume linear independence, i.e.:

      $latex \eta=m^{T}x+\varepsilon $

### Parameter/Weight Vector

      $latex m=\left[\mu_{1},\mu_{2},...,\mu_{n}\right]^{T}\epsilon\,\Re^{n} $

- where:
  - $latex \varepsilon $ - stochastic error, zero expectation value.

### Objective Function ###

- The objective function is defined as the scalar value of the average expected value of the quadratic error.

      $latex Objective\, Function=J=E\left\\{ (\eta-m^{T}x)^{2}\right\\} \qquad(i) $

- where $latex E\\{ . \\} $ is the expectation over the infinite set.
- i.e. when $latex X $ has possible values $latex x\_{1},x\_{2},.. $

      $latex Expectation=E(X)={\displaystyle \sum_{all\, distinct\, values\, of\, X}x\_{i}f(x)} $

- where $latex f(x) $ is the probability density function.

- Note, the population mean for the variable $latex X $ is $latex \mu $, i.e.

      $latex \mu=E(X) $

- For **discrete distributions**:

      $latex E(X)={\displaystyle \sum\_{j}x\_{j}f(x\_{j})} $

- For **continuous distributions**:

      $latex E(X)={\displaystyle \intop_{-\infty}^{\infty}xf(x)dx} $

- Therefore:

      $latex J=\int(\eta-m^{T}x)^{2}p(x)dx $

  - which provides a more descriptive form than $latex (i) $.

- Now we want to find $latex m^{*} $ for $latex m $ that minimises $latex J $.

- If $latex f $ is differentiable and has an extremum at point $latex X\_{0} $ then the partial derivatives $latex \delta f/\delta x,..,\delta f/\delta x\_{n} $ must be 0 at $latex X_{0} $.
  - i.e. a stationary point, therefore $latex \nabla f(X_{0})=0 $.

- i.e.

      $latex \nabla J(n)=\left[\frac{{\displaystyle \delta J}}{{\displaystyle \delta\mu\_{1}}},..,{\displaystyle \frac{\delta J}{\delta\mu\_{n}}}\right]^{T}=0 $

- **Note** for experimental data, the probability density function (pdf) $latex p(x) $ may not be known.
  - Instead use sample function of $latex J $, i.e.

        $latex J\_{1}(t)=\left[\eta(t)-m^{T}(t)x(t)\right]^{2} $

  - where:
      - $latex t=0,1,2.. $ - sample index.
      - $latex m(t) $ - approximation of $latex m $ at time $latex t $.

### RMSA ###

- RMSA used to find $latex m(t) $ by recursively searching for $latex J\_{1}(t) $ with respect to $latex m(t) $ where $latex J\_{1}(t) $ is an approximation of $latex J $.
- Starting with arbitrary individual values $latex m(0) $, the sequence $latex \\{ m(t) \\} $ converges to the neighbourhood of the optimal $latex m^{*} $.
- Recursion is defined as a series of gradient steps:

      $latex m^{T}(t+1)=m^{T}(t)-G\_{t}\left[\nabla m(t)J\_{1}(t)\right]\qquad(ii) $

- Note,

      $latex \nabla\_{x}f(x)=\nabla f(x)={\displaystyle \frac{\delta f}{\delta x\_{1}}}+{\displaystyle \frac{\delta f}{\delta x\_{2}}}+.. $

- $latex G\_{t} $
  - Gain Matrix
  - Must be a "positive definite".
  - In practice usually have $latex G_{t}=\alpha(t)\underline{I} $ where:
      - $latex \underline{I} $ - Identity matrix.
      - $latex \alpha(t) $ - Scalar, steepest descent when $latex \alpha(t) $ small.

- therefore $latex (ii) $ becomes:

      $latex m^{T}(t+1)=m^{T}(t)+\alpha(t)\left[\eta(t)-m^{T}(t)x(t)\right] $

- since:

      $latex J_{1}(t)=\left[\eta(t)-m^{T}(t)x(t)\right]^{2}=\eta(t)^{2}-2\eta(t)m^{T}(t)x(t)+\left[m^{T}(t)x(t)\right]^{2} $

  - where $latex \eta(t)^{2}=0 $.

- now:

      $latex \nabla J_{1}(t)=-2\eta(t)\underline{x}(t)+2(\underline{m}^{T}(t)x(t))\underline{x}(t) $

- therefore:

      $latex m^{T}(t+1)=m^{T}(t)-\alpha(t)\left[2\eta(t)x(t)-2x(t)x(t)m^{T}(t)\right] $

- which can be rearranged as:

      $latex m^{T}(t+1)=m^{T}(t)+\alpha(t)\left[\eta(t)-m^{T}(t)x(t)\right]x^{T}(t) $


        


