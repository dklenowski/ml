Categories: algorithms
Tags: algorithm
      markov
      markov model
      model


## Introduction

Markov model/chain consists of a set of states:

        $latex S=\left\{ s_{1},s_{2}...,s_{r}\right\} $

A process starts in one of these states and moves from 1 state to another (a step).
To calculate the movement from state i to state j we assign a probability:
$latex probability=p_{ij} $

This probability is called the transition probability
Does not depend on previous state.
$latex p_{ii} $ is the probability the process remains in the current state.

## Weather Example

Three types of weather: Rain (R), Nice (N) and Snow (S) with a transition matrix:

        $latex \underline{P}=\begin{array}{c} R\\ N\\ S\end{array}\left[\begin{array}{ccc} 0.5 & .025 & 0.25\\ 0.5 & 0 & 0.5\\ 0.25 & 0.25 & 0.5\end{array}\right] $

Where each probability represents a conditional probability

$latex p_{ij}=P(j\mid i)$

e.g. $latex p_{11} $ represents the probability it is raining tomorrow given it is raining today.

## Question

Given that the chain is in state i today what is the probability it will be in state j 2 days from now.

i.e. $latex p_{ij}^{(2)} $

More specifically, assume it is raining today find the probability it will be snowing in 2 days

e.g.

            today   today+1   today+2
        1)  rain    rain      snow  -> A
        2)  rain    nice      snow  -> B
        3)  snow    rain      snow  -> C

The probability is the disjoint union of A, B and C. i.e. the product of the
conditional probability is is rain tomorrow given it is rain today and the
conditional probability it is snow two days from now given it is rain tomorrow.
This can be written as:

$latex p_{13}^{(2)}=\overbrace{p_{11}p_{13}}^{A}+\overbrace{p_{12}p_{23}}^{B}+\overbrace{p_{13}p_{33}}^{C} $

In general if a Markov chain has r states:

To find the markov probability for the transition from state i to state j:

$latex p_{ij}^{(2)}={\displaystyle \sum_{k=1}^{r}p_{ik}p_{kj}} $

To find the markov probability for the transition from state i to state j using n steps:

$latex p_{ij}^{(n)}={\displaystyle \sum_{k=1}^{r}p_{ik}p_{kj}} $

where $latex p_{ik}p_{kj}\epsilon(n-1) $

## Calculation of the transition matrices

### Original transition matrix

        $latex today\rightarrow today+1=\underline{P_{1}}=\begin{array}{c} R\\ N\\ S\end{array}\left[\begin{array}{ccc} 0.5 & 0.25 & 0.25\\ 0.5 & 0 & 0.5\\ 0.25 & 0.25 & 0.5\end{array}\right] $

### Second transition matrix

Use the previous transition matrix to calculate the values of the new transition matrix.

        $latex \begin{aligned}today\rightarrow today+2 & =today+1\rightarrow today+2\\ & =P(RRR)^{(2)}\\ & =\underline{P_{2}}\\ & =\begin{array}{c} R\\ N\\ S\end{array}\left[\begin{array}{ccc} 0.438 & 0.188 & 0.375\\ 0.375 & 0.25 & 0.375\\ 0.375 & 0.188 & 0.438\end{array}\right]\end{aligned} $

where:

$latex \begin{aligned}p_{12}^{(2)} & =p_{11}p_{12}+p_{12}p_{22}+p_{13}p_{31}\\ & =0.5(0.25)+0.25(0)+0.25(0.25)\\ & =0.1875\end{aligned} $

### Third transition matrix

        $latex \begin{aligned}today\rightarrow today+3 & =today+2\rightarrow today+3\\ & =P(RRR)^{(3)}\\ & =\underline{P_{3}}\\ & =\begin{array}{c} R\\ N\\ S\end{array}\left[\begin{array}{ccc} & 0.269\\ \\\\\end{array}\right]\end{aligned} $

where:

        $latex \begin{aligned}p_{12}^{(3)} & =p_{11}p_{12}+p_{12}p_{22}+p_{13}p_{31}\\ & =0.438(0.188)+0.188(0.25)+0.375(0.375)\\ & =0.269\end{aligned} $