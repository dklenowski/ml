Categories: genetic algorithms
Tags: algorithms
      genetic


## Terms ##

### Strings ###

- Over the binary alphabet $latex V = \\{0, 1\\} $ a string $latex A $ is:

      $latex a=a\_{1}a\_{2}a\_{3}a\_{4} $

- Where $latex a_{i} $:
  - Is a binary feature/detector (i.e. a gene).
  - Is either 0 or 1.
- The $latex a_{i} $ value is called an *allele*.
- The population of strings $latex A_{j} $ where $latex j=1,2,..n $ contained in the population $latex A(t) $ at time (or generation) $latex t $.

### Schemata ###

- $latex H $ from the alphabet $latex V^{t} = \\{0, 1, *\\} $.
- Rules:
  1. For alphabet of cardinality $latex k $ there are $latex (k+1)^{l} $ schemata.
  2. Population of n members at most $latex n2^{l} $ schemata (each string is a representative of $latex 2^{l} $ schemata).

### Schema Order ###

- Order of schema $latex H $, $latex o(H) $.
- Number of fixed positions present in the template.
- e.g.

        H = 0 1 1 * 1 * *  $latex o(H)=4 $
        H = 0 * * * * * *  $latex o(H)=1 $

### Defining Length ###

- Of schema $latex H $, $latex \delta(H) $
- Distance between the first and last specific string position.
- e.g.

        H = 0 1 1 * 1 * *  $latex \delta(H)=5-1=4 $
        H = 0 * * * * * *  $latex \delta(H)=0 $

## Reproduction ##

- Given timestep $latex t $ and $latex m $ examples of a particular schema $latex H $ within a population $latex \underline{A}(t) $:

      $latex m=m(H,t) $

- Where $latex m(H,t) $ is the number of instance of $latex H $ at time $latex t $.
- During reproduction, the string is copied according to fitness.
  - i.e. the string $latex A_{i} $ is copied with probability:

          $latex p\_{i}=\frac{{\displaystyle f\_{i}}}{{\displaystyle \sum f_{j}}} $

- For a non overlapping population of size $latex n $ with replacement from population $latex \underline{A}(t) $:

          $latex m(H,\, t+1)={\displaystyle m(H,\, t)}{\displaystyle n}\frac{{\displaystyle f(H)}}{{\displaystyle \sum}{\displaystyle f_{i}}} $

- Where $latex f(h) $ is the observed average fitness of strings representing schema $latex H $ at time $latex t $.
- Note the the average fitness of the entire population is given by:

          $latex \bar{f}=\frac{{\displaystyle \sum f_{j}}}{{\displaystyle n}} $

- Therefore:

          $latex m(H,\, t+1)={\displaystyle m(H,\, t)}\frac{{\displaystyle f(H)}}{{\displaystyle \bar{f}}} $

- Notes:
  - Schemata with fitness values above the population average will receive an increase in the number of samples in the next generation.
  - Schemata with fitness values below the population average will receive a decrease in the number of samples in the next generation.
  - These updates are performed in parallel (across the entire string).

### Growth/Decay ###

- Assume the population schema remains above average by an amount $latex cf $ where $latex c $ is a constant.

      $latex m(H,\, t)=m(H,\, t)\frac{{\displaystyle \bar{f}+c\bar{f}}}{{\displaystyle \bar{f}}}=m(H,\, t)(1+c)$

- Starting at $latex t=0$, constant $latex c$

      $latex m(H,\, t)=m(H,\,0)(1+c)^{t}$

- Which is a geometric progression, exponential form.
  - Therefore reproduction allocates exponentially increasing (or decreasing) numbers of trials to above (or below) the average schemata.

## Crossover ##

- Information that is exchanged between strings.
- Creates new structures with minimal disruption to the allocation strategy of reproduction.
- Affects schemata.

### Process ###

- Random selection of mate.
- Random selection of crossover site.
- Exchange of substrings from beginning of string to crossover site inclusive with corresponding substring of chosen mate.

- e.g. String A chosen for mating and crossover.
  - Crossing Site = 3 (cross cut between positions 3 and 4).
  - Note, there are potentially 6 crossing sites for a string of length 7.


            A  = 0 1 1 1 0 0 0
            H1 = * 1 * * * * 0
            H2 = * * * 1 0 * *
                    |
                    crossing site

- Schemata $latex H_{1} $
  - Destroyed, `1` at position 2 and `0` at position 7.
- Schemata $latex H_{2} $
  - Will survive.
  - `1` at position 4 and `0` at position 5 will be carried intact to a single offspring.

### To Quantify ###

- Schema $latex H\_{1} $ with a defining length of $latex \delta(H\_{1})=5 $.
- If the crossover site selected at random among $latex l-1=7-1=6 $ sites then the schema $latex H_{1} $ destroyed with probability **[1]**:

      $latex p_{d}=\frac{{\displaystyle \delta(H\_{1})}}{{\displaystyle (l-1)}}={\displaystyle \frac{5}{6}} $

- And will survive with:

      $latex p-{s}=1-p_{d}={\displaystyle \frac{1}{6}} $

- Therefore survival under single crossover is:

      $latex p_{s}=1-\frac{{\displaystyle \delta(H)}}{{\displaystyle (l-1)}} $

- Assuming crossover is performed at random, with probability $latex p_{c} $ at a particular mating:

      $latex p_{s}\geqslant1-\frac{{\displaystyle \delta(H)}}{{\displaystyle (l-1)}} $

- which reduces to **[1]** when $latex p_{c} = 1 $.
  - Note, an inequality is used in the above equation because not all crossovers in the defining length break up schema $latex H $.

- **Therefore** the shorter the schema, the more likely it will survive.

## Combining Reproduction and Crossover ##

- For Reproduction:

      $latex m(H,\, t+1)={\displaystyle m(H,\, t)}\frac{{\displaystyle f(H)}}{{\displaystyle \bar{f}}} $

- The combined effect:

          Combined  =   Expected Number of            Survival Probability
          Effect        Schema for              *     under Crossover
                        Reproduction Alone

- i.e.

      $latex m(H,\, t+1)\geqslant{\displaystyle m(H,\, t)}\frac{{\displaystyle f(H)}}{{\displaystyle \bar{f}}}p_{s} $

- therefore:

      $latex m(H,\, t+1)\geqslant{\displaystyle m(H,\, t)}\frac{{\displaystyle f(H)}}{{\displaystyle \bar{f}}}\left[1-p_{c}\frac{{\displaystyle \delta(H)}}{{\displaystyle (l-1)}}\right] $

- **2 factors**:
  1. Schema above/below population average.
  2. Whether schema has short/long defining lengths.

- **Therefore** schemata with above average observed performance and short defining lengths will be sampled at exponentially increasing rates.

## Mutation ##

- $latex p_{m} $ is the probability of random alteration of a single position (mutation).

- A single allele survives with:

      $latex 1-p_{m} $

- The probability that $latex H $ survives:

      $latex (1-p_{m})^{o(H)} $
  
  - where: $latex p_{m} \ll 1 $

- For small values of $latex p_{m} $, schema survival can be approximated by:

      $latex 1-o(H)p_{m} $

## General Equation for Crossover, Reproduction and Mutation ##

      $latex m(H,\, t+1)\geqslant{\displaystyle m(H,\, t)}\frac{{\displaystyle f(H)}}{{\displaystyle \bar{f}}}\left[1-p_{c}\frac{{\displaystyle \delta(H)}}{{\displaystyle (l-1)}}\right]\left[1-o(H)p_{m}\right] $

      $latex m(H,\, t+1)\geqslant{\displaystyle m(H,\, t)}\frac{{\displaystyle f(H)}}{{\displaystyle \bar{f}}}\left[1-o(H)p_{m}-p_{c}{\displaystyle \frac{\delta(H)}{(l-1)}}+p_{c}{\displaystyle \frac{\delta(H)}{(l-1)}}o(H)p_{m}\right] $

- where the following is negligible:

      $latex p\_{c}{\displaystyle \frac{\delta(H)}{(l-1)}}o(H)p\_{m}\doteqdot0 $

- therefore:

      $latex m(H,\, t+1)\geqslant{\displaystyle m(H,\, t)}\frac{{\displaystyle f(H)}}{{\displaystyle \bar{f}}}\left[1-p\_{c}{\displaystyle \frac{\delta(H)}{(l-1)}}-o(H)p\_{m}\right] $


## Example Problem - 2-armed bandit/k-armed bandit


### Given ###

- Slot machine with 2 arms.
- First arm pays $latex \mu\_{1} $ variance $latex \sigma\_{1}^{2} $.
- Second arm pays $latex \mu\_{2} $ variance $latex \sigma\_{2}^{2} $. 
- Where $latex \mu\_{1}\geqslant\mu\_{2} $.

### Required To Find ###

- Which arm to play?

### Working ###

#### Option 1 ####

- Perform experiment and thereafter making a single irreversible decision depending on the outcome of the experiment.

##### Solve #####

- Perform $latex N $ trials among 2 arms.
- Allocate equal number of trials, $latex n $, to each of the 2 arms ($latex 2n<N $) during experimentation.
- Allocate remaining $latex N-2n $ trials to arm with best observed payoff.
- Then the expected loss (De Jong):

      $latex Expected\: Loss=L(N,\: n)=\left|\mu\_{1}-\mu\_{2}\right|\left[(N-n)q(n)+n(1-q(n))\right] $

- where $latex q(n) $ is the probability that the worst arm is the observed best arm after n trials.
The probability $latex q(n) $ approximated by the tail of the normal distribution:

      $latex q(n)\backsimeq{\displaystyle \frac{1}{\sqrt{2\pi}}}{\displaystyle \frac{{\displaystyle e^{{\displaystyle -x^{2}/2}}}}{x}} $

- where:

      $latex x=\frac{{\displaystyle \mu\_{1}-\mu\_{2}}}{\sqrt{{\displaystyle \sigma\_{1}^{2}+\sigma\_{2}^{2}}}}\sqrt{n} $

- Therefore there are 2 types of losses:
  1. Issuing $latex n $ trials to the wrong arm.
  2. Choosing arm with lower payoff even after performing experiment.

##### Solve using Genetic Algorithms #####

- Consider competing schema as competing arms.
- 2 schemata $latex A $ and $latex B $.
- Competing if at al positions $latex i=1,2,..l $ either:

      $latex a)\quad a\_{i}=b\_{i}=* $
      $latex b)\quad a\_{i}\neq\*b\_{i}\neq\*a\_{i}\neq b\_{i} $

- for at least $latex 1..i $.











