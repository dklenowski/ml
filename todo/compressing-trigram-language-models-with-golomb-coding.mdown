Categories: natural language
Tags: golomb
      trigram
      gram

### Reference ###

Compressing Trigram Language Models With Golomb Coding. Ken Church, Ted Hart and Jianfeng Gao, Microsoft.

### Notes ###

#### Katz Backoff

- Due to the sparsity of text and the fact that we will not see n-grams in test that did not appear in training set, Katz proposed backing off from trigrams to bigrams (and from bigrams to unigrams) when we don't have enough training data.
- For trigram seen during training, backoff estimate for the probability:

        $latex P(w_{i}\mid w_{i-2}w_{i-1}) $

- is the discounted probability:

        $latex P_{d}(w_{i}\mid w_{i-2}w_{i-1}) $

  - i.e. discounted probabilities steal from the rich and give to the poor (lesser found n-grams).

- The backoff estimate for unseen trigrams is:

        $latex \alpha(w_{i-2}w_{i-1})\: P_{d}(w_{i}\mid w_{i-1}) $

- backoff alphas ($latex \alpha $) are a normalisation factor that accounts for the discounted mass, i.e.:

        $latex \alpha(w_{i-2}w_{i-1})=\frac{{\displaystyle 1-}{\displaystyle \sum_{{\displaystyle w_{i}:C(w_{i-2}w_{i-1}w_{i})}}P(w_{i}\mid w_{i-2}w_{i-1})}}{{\displaystyle 1-\sum_{{\displaystyle w_{i}:C(w_{i-2}w_{i-1}w_{i})}}P(w_{i}\mid w_{i-1})}} $

  - where $latex C(w\_{i-2}w\_{i-1}w\_{i})>0 $ indicates trigram was seen in training data.

#### Stolcke Pruning ####

- Looks for n-grams that would receive nearly the same estimates via Katz backoff if they were removed.
- Saves space by removing n-grams subject to a loss consideration:

  1. Select a threshold $latex \theta $.
  2. Compare performance loss due to pruning each trigram and bigram individually using pruning criteria.
  3. Remove all trigrams with performance loss less than $latex \theta $.
  4. REmove all bigrams with no child nodes (trigram nodes) and with the performance loss less than $latex \theta $.
  5. Re-compute backoff weights.


- Trigrams consists of 3 integers (offsets into the vocabulary): $latex w\_{1}w\_{2}w\_{3} $.
- These 3 integers mapped to single hash between $latex 0 $ and $latex P-1 $ using:

        $latex hash=(w_{3}V^{0}+w_{2}V^{1}+w_{3}V^{2})mod(P) $

  - where:
      - $latex V $ - Vocabulary size.


