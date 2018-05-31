Categories: natural language
Tags: localmax
      algorithm


### Reference ###

Using LocalMaxs Algorithm for the Extraction of Contiguous and Non-contiguous Multiword Lexical Units. Joaquim Ferreira da Seliva et al, Universidade Nove de Lisboa.

### Notes ###

- MWU - Multi Word Unit
- Algorithm:

        $latex \exists x \in \Omega_{n-1}, \exists y \in \Omega_{n+1} $
        W is a MWU if
          (length(W) = 2 and g(W) > y) or
          (length(W) > 2 and x <= g(W) and g(W) > y)

#### Symmetrical Conditional Probability (SCP) ####

- For bigram [x, y] "glue" value of bigram [x, y] measured by SCP[x, y]:

        $latex SCP([x,y])=p(x \mid y)\:p(y \mid x) $
        $latex SCP([x,y])=\frac{{\displaystyle p(x,y)^{2}}}{{\displaystyle p(x)p(y)}} \qquad(i) $

  - where:
      - $latex p(x,y) $, $latex p(x) $ and $latex p(y) $ are respectively the probabilities of occurances of the bigram [x,y] and the unigrams [x] and [y] in the corpus.
      - $latex p(x \mid y) $ is the conditional probability of x in the first position given y appears in the second position in the same bigram.


#### Fair Dispersion Point Normalisation ####

- Considering denominator in $latex (i) $ can think about n-gram as a "pseudo-bigram" having a left part [x] and a right part [y].
- Transforms any n-gram of any size in a "pseudo-bigram" and embodies all possibilities to have 2 adjacent groups of words from the whole original n-gram.
- Fair Dispersion Point defined as:

        $latex Avp=\frac{1}{n-1}{\displaystyle \sum_{i=1}^{i=n-1}p(w_{1},...,w_{i})\: p(w_{i+1},...,w_{n})\qquad(ii)} $

- Replacing $latex (ii) $ as the denominator of $latex (i) $, we have a normalised SCP:

        $latex SCP_{f}([w_{1},...,w_{n}])=\frac{{\displaystyle p(w_{1},...,w_{n})^{2}}}{Avp} $

#### Normalised Expectation Measure ####

- Existing between n words as the average expectation of the occurrence of 1 word in a given position knowing the occurrence of the other n-1 words also constrained by their position.
- i.e. evaluate cost, of a possible loss of one word in a n-gram.
- The more cohesive a word group is, that is the less it accepts the loss of one of its components, the higher its normalised expectation will be.
- Based on Conditional Probability, i.e.

        $latex p(X=x\mid Y=y)={\displaystyle \frac{p(X=x,Y=y)}{p(Y=y)}} $

##### Fair Point of Expectation #####

- An n-gram:

        $latex w_{1}w_{2}..w_{n} $

- Can be represented by:

        $latex [w_{1}\; p_{12}w_{2}\; p_{13}w_{3}\;...\; p_{1n}w_{n}] $

    - where $latex p\_{1n} $ for $latex i=2,..,n $ represents the signed distance that separates word $latex w\_{i} $ from $latex w\_{1} $.
    - Note, the above expression is equivalent to:

            $latex [w_{1}\; p_{12}w_{2}\; p_{23}w_{3}\;...\; p_{2n}w_{n}] $
      
      - where $latex p\_{2i}=p\_{1i}-p\_{12} $ for $latex i=3,..,n $ and $latex p\_{2n} $ represents the signed distance that separates word $latex w\_{i} $ from $latex w\_{2} $.

- Define the fair point of expectation (FPE) which is the arithmetic mean of the n join probabilities of the n (n-1)-grams contained in an n-gram.

        $latex FPE(\,[w_{1}\; p_{12}w_{2}\;...\; p_{1n}w_{n}]\,)=\frac{1}{n}(p(\,[w_{2}\; p_{23}w_{3}\; p_{2n}w_{n}]\,)+{\displaystyle \sum_{i=2}^{n}p(\,[w_{1}\; p_{1i}w_{i}\;...\; p_{1n}w_{n}]\,)}  $

  - where:
      - $latex p(\,[w\_{2}\; p\_{23}w\_{3}\; p\_{2n}w\_{n}]\,) $ for $latex i=3,..,n $ is the probability of the (n-1)-gram.
      - $latex p(\,[w\_{1}\; p\_{1i}w\_{i}\;..\; p\_{1n}w\_{n}]\,) $ is the probability of the occurrence of 1 (n-1)-gram containing the first word but missing a $latex p\_{1i}w\_{i} $ word.

- The resulting measure called the normalised expectation and proposed as a fair conditional probability:

        $latex NE(\,[w_{1}\; p_{12}w_{2}\;...\; p_{1n}w_{n}]\,)={\displaystyle \frac{p(\,[w_{1}\; p_{1i}w_{i}\;...\; p_{1n}w_{n}]\,)}{FPE(\,[w_{1}\; p_{12}w_{2}\;...\; p_{1n}w_{n}]\,)}} $

##### Mutual Expectation Measure #####

- Between 2 n-grams with the same normalised expectation, that is with the same value measuring the possible lss of 1 word in an n-gram, the most frequent n-gram is more likely to be a MWU.
- Define a Mutual Expectation which is a weighted normalised expectation

        $latex ME(\,[w_{1}\; p_{12}w_{2}\;...\; p_{1n}w_{n}]\,)=f(\,[w_{1}\; p_{12}w_{2}\;...\; p_{1n}w_{n}]\,)\; NE(\,[w_{1}\; p_{12}w_{2}\;...\; p_{1n}w_{n}]\,) $

  - where:
      - $latex f(\,[w\_{1}\; p\_{12}w\_{2}\;..\; p\_{1n}w\_{n}]\,) $ is the frequency of the particular n-gram.

### Results ###

- $latex SCP\_{f} $ achieved good precision (around 70%) on english texts for extracting MWU.
- $latex SCP\_{f} $ appears to work better on 2-gram (81%) rather than 3-gram (73%).
- $latex ME(.) $ works well (90%) for non-contiguous MWU (with exactly 1 gap).
  - Note, the more contiguous gaps in a MWU, the less the unit is meaningful, and the more likely it is be be an incorrect MWU.




        



