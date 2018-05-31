Categories: algorithms
Tags: algorithm
      markov
      markov model
      model


## Introduction

- When using large sparse data sets, zero conditional probabilities can reduce the effectiveness of the markov transition matrix.
- To overcome this, its straightforward to replace the zero conditional probabilities with a "fudge" probability, eliminating the underflow.
- The following "fudge" probability appears to work OK:

$latex p_{f}=\left(\displaystyle\frac{1}{vf}\right)a $

- Where:

v = number of "fudge" probabilities that we need to generate (i.e. a positive integer).
f = The sum of all frequencies.
a = A scaling factor for "fudge" probabilities

- The reduction for each non-zero conditional probability then becomes:

$latex s={\displaystyle \frac{a}{f_{i}f{\displaystyle \sum_{{\displaystyle i,i\epsilon n}}\frac{1}{f_{i}}}}}={\displaystyle \frac{1}{f_{i}}\left(\frac{a}{f{\displaystyle \sum_{{\displaystyle i,i\epsilon n}}\frac{{\displaystyle 1}}{f_{i}}}}\right)} $

## Working

### Given

- n - number of samples
- $latex f_{i} $ - frequency of sample i
- $latex f $ - total frequency and $latex f={\displaystyle \sum_{{\displaystyle i,i\epsilon n}}f_{i}} $
- v - number of "fudge" probabilities we need to generate.
- a - scaling factor for "fudge" probabilities (allows dynamic recalculation of the fudge probability
- $latex p_{f} $ - fudge probability where $latex p_{f}=\left({\displaystyle \frac{1}{vf}}\right)a $

### Required to find

- We need to find how much we have to reduce our non-zero conditional probabilities by.
- The probability equation for a row in the transition matrix becomes (i):

$latex \sum P(f_{i})=\underbrace{{\displaystyle \sum_{{\displaystyle i,i\epsilon n}}}\left({\displaystyle \frac{f_{i}}{f}-\frac{x}{f_{i}}}\right)} _a+\underbrace{{\displaystyle \sum_{{\displaystyle i,i\epsilon n}}}{\displaystyle \frac{a}{vf}}} _b=1 $

- where:
  - a - Original probability calculation with a scaling factor $latex \frac{{\displaystyle x}}{{\displaystyle f_{i}}} $ to accomodate the "fudge" probabilities (is dependent on our original frequency as per our requirements.
  - b - the new "fudge" probabilities which are used to reduce underflow.

### Working

Assume n = 1, (i) becomes:

$latex \left({\displaystyle \frac{f_{o}}{f}-\frac{x}{f_{0}}}\right)+\left({\displaystyle \frac{f_{1}}{f}-\frac{x}{f_{1}}}\right)+{\displaystyle \sum_{{\displaystyle j,j\epsilon v}}\frac{a}{vf}=1} $

$latex \left({\displaystyle \frac{f_{0}+f_{1}}{f}}\right)-x\left({\displaystyle \frac{1}{f_{0}}+\frac{1}{f_{1}}}\right)+{\displaystyle \sum_{{\displaystyle j,j\epsilon v}}\frac{a}{vf}=1} $

We know that:

$latex \sum f_{i}=f $

$latex {\displaystyle \sum}{\displaystyle \frac{a}{vf}}={\displaystyle \frac{va}{vf}}={\displaystyle \frac{a}{f}} $

Therefore:

$latex -x{\displaystyle \sum}{\displaystyle \frac{1}{f_{i}}}+{\displaystyle \frac{a}{f}}=0 $

$latex x={\displaystyle \frac{a}{f{\displaystyle \sum}{\displaystyle \frac{1}{f_{i}}}}} $

In General:

$latex x={\displaystyle \frac{a}{f{\displaystyle \sum_{{\displaystyle i,i\epsilon n}}}{\displaystyle \frac{1}{f_{i}}}}} $

$latex scalingFactor=s={\displaystyle \frac{a}{f_{i}f{\displaystyle \sum_{{\displaystyle i,i\epsilon n}}}{\displaystyle \frac{1}{f_{i}}}}} $

Now, we need to check that (i) holds, so assume n=1

$latex \sum P=\left({\displaystyle \frac{f_{0}}{f}}-{\displaystyle \frac{a}{f_{0}f\sum{\displaystyle \frac{1}{f_{i}}}}}\right)+\left({\displaystyle \frac{f_{1}}{f}}-{\displaystyle \frac{a}{f_{1}f\sum{\displaystyle \frac{1}{f_{i}}}}}\right)+\sum{\displaystyle \frac{a}{vf}}=1 $

This reduces to (ii):

$latex {\displaystyle \left(\frac{f_{0}+f_{1}}{f}\right)}+{\displaystyle \left(\frac{af_{1}+af_{0}}{f_{o}f_{1}f\sum{\displaystyle \frac{1}{f_{i}}}}\right)}+{\displaystyle \frac{a}{f}}=1 $

We know that:

$latex {\displaystyle \left(\frac{f_{0}+f_{1}}{f}\right)}=1 $

Therefore (ii) becomes:

$latex {\displaystyle \frac{a(f_{1}+f_{0})}{f_{o}f_{1}f\left({\displaystyle \frac{1}{f_{0}}+\frac{1}{f_{1}}}\right)}}={\displaystyle \frac{a}{f}} $

$latex f_{0}f_{1}\left({\displaystyle \frac{1}{f_{0}}+\frac{1}{f_{1}}}\right)=f $

$latex f_{0}f_{1}\left({\displaystyle \frac{f_{1}+f_{0}}{f_{0}f_{1}}}\right)=f $

$latex f=f $