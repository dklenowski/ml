Categories: algorithms
Tags: algorithm
      bayes

### Bayes Theorem ###

- Assume event *E* has occurred:
  - A new distribution function needs to be created (i.e. $latex m(w_{j}\mid E) $) for $latex \Omega $ to reflect the fact that *E* has occurred.
  - i.e. there will be a new sample space with new probabilities after event *E* has occurred.

        $latex P(F\mid E)=\frac{{\displaystyle P(F\cap E)}}{{\displaystyle P(E)}} $

  - i.e. the probability of *F* occurring given *E* has already occurred.

#### Theorems ####

##### Independence

- 2 events *E* and *F* independent if $latex P(E)>0 $ and $latex P(F)>0 $ and if

        $latex P(E\mid F)=P(E) $

- and

        $latex P(F\mid E)=P(F) $

- 2 events *E* and *F* also independent if $latex P(E)>0 $ and $latex P(F)>0 $ and if

        $latex P(E\cap F)=P(E)P(F) $

##### Mutual Independence

- Set of events $latex \{A\_{1},A\_{2},..,A\_{n}\} $ are mutually independent if for any subset $latex \{A\_{i},A\_{j},..,A\_{m}\} $ we have:

        $latex P(A_{i}\cap A_{j}\cap..\cap A_{m})=P(A_{i})P(A_{j})..P(A_{m}) $

- Note, it is important to note that the statement:

        $latex P(A_{1}\cap A_{2}\cap..\cap A_{n})=P(A_{1})P(A_{2})..P(A_{n}) $

  - does not imply that the events $latex A\_{1},A\_{2},..,A\_{n} $ are not pairwise independent.


#### Derivation ####

- Given the outcome of the second stage of a two stage experiment, find the probability for an outcome of the first stage.

##### Independent Trials

- Sequence of random variables $latex X\_{1}, X\_{2} $ that are mutually independent and have the same distribution.
  - Called a sequence of independent trials or a independent trials process.

- Sample Space:

        $latex R=\left\{ r_{1},r_{2},..,r_{s}\right\} $

- Distribution Function:

        $latex m_{x}=\left(\begin{array}{cccc} r_{1} & r_{2} & .. & r_{s}\\ p_{1} & p_{2} & .. & p_{s}\end{array}\right) $

- Repeat experiment *n* times to describe the total experiment and choose as the sample space the space

        $latex \Omega=R\times R\times R\times..\times R $

  - which consists of all possible sequences:

          $latex w=\left(w\_{1},w\_{2},..,w\_{n}\right) $
  
    - where the value of each $latex w\_{j} $ is chosen by $latex R $.

- Assign a distribution function to the product distribution:

        $latex m(w)=m(w_{1})\cdot m(w_{2})\cdot..\cdot m(w_{n}) $

  - where:

          $latex m(w\_{j})=p\_{k} $
          $latex w\_{j}=r\_{k} $

- Let $latex X\_{j} $ denote the *j'th* coordinate of the outcome $latex \\{ r\_{1},r\_{2},..,r\_{s}\\} $
  - **Therefore** the random variables $latex X\_{1},..,X\_{n} $ forms an independent trials process.


##### Calculation of General Bayes Probabilities #####

- Given a set of events $latex H\_{1},H\_{2},..,H\_{m} $ (i.e. the hypothesis) that are pairwise disjoint, i.e. the sample space satisfies the following condition:

        $latex \Omega=H_{1}\cup H_{2}\cup..\cup H_{m} $

  - Note, **pairwise disjoint**
    - No two events have an element in common.
    - i.e. For *A* and *B*, every element of $latex A\cup B $ either lies in *A* and not in *B* or in *B* and not in *A*.

- And a set of prior probabilities for the hypothesis:

        $latex P(H_{1}),P(H_{2}),..,P(H_{m}) $

- We use event *E* to give information about which hypothesis is correct.
  - i.e. we know $latex P(E\mid H_{i}) $ for all *i*.
  - i.e. if we know the correct hypothesis, we know the probability for the evidence.

- To find the **posterior probabilities**
  - i.e. we want to find the probabilities for the hypothesis given the evidence (i.e. $latex P(H_{i}\mid E) $).
    - i.e. how likely it is that *E* lies in *H* (so *H* is consistent with the observations).

  - Let $latex H\_{i} $ be a point in the hypothesis, we want to find:

          $latex P(H\_{i}\mid E)=\frac{{\displaystyle P(H\_{i}\cap E)}}{{\displaystyle P(E)}} $

  - where:

          $latex P(H\_{i}\cap E)=P(H\_{i})P(E\mid H\_{i}) $ since $latex P(H\_{i}\cap E)=P(E\cap H\_{i}) $

  - and:

          $latex P(E)=P(H\_{i}\cap E)+P(H_{2}\cap E)+..+P(H\_{m}\cap E) $
          $latex P(E)=P(H\_{1})P(E\mid H\_{i})+P(H\_{2})P(E\mid H\_{2})+..+P(H\_{m})P(E\mid H\_{m}) $

  - therefore:

          $latex P(H\_{i}\mid E)=\frac{{\displaystyle P(H\_{i})P(E\mid H\_{i})}}{{\displaystyle \sum_{k=1}^{m}P(H\_{k})P(E\mid H\_{k})}} $

  - which gives us bayes theorem (since one and only one hypothesis can occur):

          $latex P(H\mid E)={\displaystyle \frac{P(E\mid H)P(H)}{P(E)}} $

### Using Bayes ###

- An event of interest *A* occurs in conjunction with one and only one of the events $latex B\_{1},B\_{2},B\_{3},..,B\_{k} $ which form a partition of the sample space into disjoint subsets.
- e.g. when *k=3*

<!-- bayes-partition.png -->
![Bayes Partition Function](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6TGFfTzZhM0RoUWc "Bayes Partition Function")

- We know:
  - The probabilities $latex B\_{1},B\_{2},B\_{3},..,B\_{k} $
  - The conditional probabilities $latex P(A\mid B\_{1}),..,P(A\mid B\_{k}) $

- We can use bayes to find the conditional probability $latex P(B\_{1}\mid A) $.

        $latex P(B_{1}\mid A)=\frac{{\displaystyle P(A\mid B_{1})P(B_{1})}}{{\displaystyle P(A)}} $


### Bayes Examples ###

#### Urns ####

- 2 urns *I* and *II*.
  - Urn *I* has 2 black balls and 3 white balls (5 balls).
  - Urn *II* has 1 black ball and 1 white ball (2 balls).

                  urn  ball             w       p(w)
                       b      2/5       w1      1/5
                      /
                    I
                  /   \ 
             1/2 /     w      3/5       w2      3/10
                *      
             1/2 \     b      1/2       w3      1/4
                  \   /
                    II
                      \
                       w      1/2       w4      1/4
                    
- The probability that a *back ball* chosen given urn *I* is chosen:

        $latex P(B\mid I)=\frac{{\displaystyle 2}}{{\displaystyle 5}} $

- The probability urn *I* is chosen given a *black ball* was chosen:

        $latex \begin{array}{cc} P(I\mid B) & \lefteqn{\lefteqn{=\frac{P(B\mid I)P(I)}{P(B)}}}\\ & \lefteqn{=\frac{P(B\mid I)P(I)}{P(B\cap I)+P(B\cap II)}}\\ & \lefteqn{=\frac{\frac{2}{5}\frac{1}{2}}{\frac{1}{2}\frac{2}{5}+\frac{1}{2}\frac{1}{2}}}\end{array} $

#### Diseases

- A doctor has to decide whether a patient has disease $latex d\_{1}, d\_{2}, d\_{3} $.
  - Two tests are carried out where the result is either positive or negative.
- The following is the distribution of tests from 10000 people

                         No Of People With        Result of test
             Disease     Disease                  ++     +-      -+      --
          
             d1          3215                     2110   etc     etc     etc
             d2          2125                     396    etc     etc     etc
             d3          4600                     510    etc     etc     etc
          
          Total          10000

- with probabilities:

        $latex P(d_{1})=\frac{3215}{10000}=0.3215 $
        $latex P(d_{2})=\frac{2125}{10000}=0.2125 $
        $latex P(d_{3})=\frac{4600}{10000}=0.4600 $
        $latex P(++\mid d_{1})=\frac{2110}{3125}=0.6752 $
        $latex P(++\mid d_{2})=\frac{396}{2125}=0.1864 $
        $latex P(++\mid d_{3})=\frac{510}{4600}=0.1100 $

- The probability that patient has $latex d\_{1} $ given he had a positive test.

        $latex \begin{array}{lc} P(d_{1}\mid++) & \lefteqn{=\frac{P(++\mid d_{1})P(d_{1})}{P++)}}\\ & \lefteqn{=\frac{P(++\mid d_{1})P(d_{1})}{P(d_{1})P(++\mid d_{1})+P(d_{2})P(++\mid d_{2})+P(d_{3})P(++\mid d_{3})}}\end{array} $


