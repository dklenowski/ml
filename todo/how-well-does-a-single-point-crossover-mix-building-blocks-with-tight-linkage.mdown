Categories: genetic algorithms
Tags: algorithms
      genetic
      genotype
      phenotype
      
## Reference ##

How Well Does a single point Crossover mix building blocks with tight linkage.
Kumara Sastry and David E Goldberg,
Illinois Genetic Algorithms Laboratory (IlliGAL) Report 2002013, May 2002


## Notes ##

> "Holland made two key observations in his monograph (Holland, 1975): (1) BBs 
> with tighter linkage (shorter defining length) have a selective advantage over 
> those with loose linkage (longer defining length), and (@) operators to adapt 
> linkage and to choose allele combinations might be necessary for GA success."


> "On a parallel note, it is now know that many operators such as elitism, 
> niching, mating, restriction, inversion and reordering, proposed to adapt
> linkage and to enhance GA performance do not achieve there goal."

> "Failures with such operators suggest that the critical step in designing 
> better crossover operators is to first analyse fixed crossover operators 
> such as uniform, one-point and n-point crossovers. Such analysis should tell
> us if fixed crossover operators are powerful enough to solve problems of 
> bounded difficulty quickly, reliably and accurately."

> "Another class of models is motivated from quantitative genetics.
> Central to these modes is Geiringer's theorem and linkage (Robbin's) equilibrium or
> crossover induced bias such as positional bias, distributional bias, 
> recombinative bias and schema bias and relaxation time, which measures the rate 
> at which recombination operators converge to linkage equilibrium. 
> However, similar to schema disruption models, these models also do not address the mixing issue."


To calculate the mixing time, $latex t_{x} $ for allele wise exchange:

        $latex t_{x}=\frac{{\displaystyle 1}}{{\displaystyle np_{c}p^{l}}} $

where:
      $latex n $ - population size.
      $latex p $ - geometric mean of proportion of the target allele.
      $latex p_{c} $ - crossover probability.
      $latex l $ - string length.

Key points for above equation:

> "When mixing time is less than the selection time, then good BB exchange is ensured."
> "On the other hand, if mixing time is greater than selection time, then a GA will converge prematurely."
> "When the selection time is greater than the drift time, then GA drifts and converges to alleles with little or no selection pressure."
> "When selection pressure is high, BB's in different partitions might compete. Such a competition between non-competing alleles is called cross competition."

> "Theierens and Goldberg (1993) extended the allele-wise mixing model to incorporate BB wise mixing."

        $latex t_{x}=c{\displaystyle \frac{2^{\mu k}}{np_{c}}\frac{2^{m}}{m^{5/2}}} $

where:
      $latex m $ building blocks of size $latex k $.
      $latex c $ - constant.
      $latex \mu $ - constant.

> "Comparing this with selection yields a population sizing model to satisfy mixing:"

        $latex n\, ln\, n>c{\displaystyle \frac{2^{\mu k}}{np_{c}}\frac{2^{m}}{m^{5/2}}}ln\, s $

Key points for the above equation:

> "The sweet-spot shrinks rapidly as the problem size increases."
> "BBs have to be tightly linked in the problem coding structure."
> "As the problems become more difficult, population sizes must grow 
> exponentially to ensure that a simple GA using fixed crossover operators converges to a good solution."

> "Even though this study uses deceptive trap functions to validate the model, the results should
> apply to additively decomposable stationary fitness functions of bounded order." 

### Mixing models for m Building Blocks ###

2 key behaviours for single point crossover:

#### Ladder Climbing

> "All building block configurations at a certain mixing level have to be discovered
> before a higher mixing level can be reached. e.g. `b#b###` is at mixing level 2,
> while `b#bb##` is at mixing level 3.

#### Length Reduction ####

> "Proportion of individuals having good BB at their two ends is higher than those at other position."
> "Proportion gradually reduces along the position and reaches a minimum at the centre."

Mixing Probability (constant wrt to mixing level)

        $latex p_{mix}(m)={\displaystyle \frac{2}{3}}{\displaystyle \frac{(m-1)[(m-2)k+3]}{m(mk-1)}} $

where: 
        $latex m $ building blocks of size $latex k $.


Time taken to move to the next mixing level

        $latex n_{x}=\frac{1}{2}c_{mx}m $

where:
        $latex n_{x} $ is the number of individuals required to climb one step of the ladder (constant wrt mixing level).
        $latex \alpha<1/m $
        $latex c\_{mx}=-ln\alpha $
        
Key point for above equation:

> "The number of mixing events required to climb one step of the ladder is 
> proportional to the number of building blocks."

Mixing Time

        $latex t_{x}\approx c_{x,m}{\displaystyle \frac{m}{np_{c}}} $

where:
        $latex t\_{x} $ is the mixing time.
        $latex c\_{x,m}=\frac{2}{3}c_{mx} $

Mixing time to go from mixing level 1 to mixing level $latex m $.

        $latex t_{x,tot}=mt_{x}=c_{x,m}{\displaystyle \frac{m^{2}}{np_{c}}} $

Key point for above equation:

> "Total mixing time grows quadratically with the number of building blocks 
> and is inversely proportional to the population size and the crossover probability."

        $latex n>c_{x}{\displaystyle \frac{I}{p_{c}}}2^{k}m\sqrt{{\displaystyle \frac{m}{k}}} $

where:
        $latex n $ - population size.
        $latex I $ - selection intensity (function of tornament size).
        $latex p_{c} $ - crossover probability.
        $latex k $ - building block (BB) size.
        $latex m $ - number of BB's




      
        






