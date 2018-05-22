Categories: natural language
Tags: zipf
      law

# Zipf’s Law

## References

- Edleno et all, Fast and Flexible Word Searching on Compressed Texts
- Zipf, G. 1949, Human Behaviour and the Principle of Least Effort, Addison Wesley

## Notes

- If we order $latex v $ words of a natural language text in decreasing order of probability, then the probability of the first word is $latex i^{\theta} $ of the $latex i $ -th word, for evey $latex i $.
- Therefore the probability of the $latex i $ -th word is:

$latex p_{i}={\displaystyle \frac{1}{i^{\theta}H}} $ where $latex H=H_{v}^{(\theta)}=\sum_{j=1}^{v}\frac{{\displaystyle 1}}{{\displaystyle j^{\theta}}} $

- The constant $latex \theta $ depends on the text:
  - Simplest cast $latex \theta=1 $, therefore $latex G=O(log(v)) $.
  - Natural language texts usually have a more biased vocabulary.
  - Generalised Zipf’s Law has $latex \theta>1 $.
  - e.g. between 1.5 and 2.0 depending on the text, therefore $latex H=O(1) $.

