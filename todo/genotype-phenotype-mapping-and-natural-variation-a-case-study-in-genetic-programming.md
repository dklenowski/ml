Categories: genetic algorithms
Tags: algorithms
      genetic
      genotype
      phenotype

## Reference ##

- Genotype-Phenotype-Mapping and Neutral Variation - A case study in Genetic Programming.
  Wolfgang Banzhaf, Department of Computer Science, Dortmund University.


## Quotes ##

- Paraphrased, Kimura's theory states that evolution at the molecular level is mainly due to mutations at are nearly neutral with respect to natural selection.
- Mutation and a resulting random drift of genomes are thus considered main forces behind evolution.
- Kimura notes that this continuous variation of genetic material, with most of it being neither advantageous nor disadvantageous, is key in understanding natural genetic diversity.


- Genotype-Phenotype Mapping (GPM)



        Genotype                                                          Phenotype
        Search Space    ----> Genotype-Phenotype Mapping (GPM)   ---->    Solution Space
        Unconstrained                                                     Constrained

- i.e. particularly useful in constrained optimisation problems.


- GPM in Nature (a), Generic Model (b), and in Binary Genetic Programming (c):


                (a)                     (b)                                 (c)
        Nucleotide Sequence         Genotype                        Binary Number Sequence
                |                       | Transcription                       |
                \/                      \/                                    \/
        mRNA Copy                   Intermediate Carrier            Binary Copy
                |                       | Edition                             |
                \/                      \/                                    \/
        Processed mRNA              Edited intermediate carrier     Corrected Copy
                |                       |                                     |
                |                       | Translation                         \/
                |                       |                           Raw Translation
                |                       |                                     |
                \/                      \/                                    \/
        Amino Acid Sequence       Translation Product             Correct Expression
                |             Formation | Compilation                         |
                \/                      \/                                    \/
        2dim,3dim structure         Phenotype                         Executable
                |                       |                                     |
                \/                      \/                                    \/
         Activity In Reactions      Behaviour                         Activity for IO Pairs


