Categories: genetic algorithms
Tags: codon
      genotype
      phenotype

## Reference ##

A Case For Codons in Evolutionary Algorithms, Joshua Gilbert, Maggie Eppstein,
Department of Computer Science, Universityof Vermont, Burlington, VT. 

## Notes ##

### Genotype ###

- Data with which the genetic operators are applied.

### Phenotype ###

- Data that is evaluated in the fitness function.


### Biological Systems ###

- In DNA, 4 letter alphabet at the genotype level (a, g, c, t) representing 4 nucleotide bases (adenine, guanine, cytosine, and thymine).
- String DNA bases translated to protein or string of amino acids using a codon triplet translation scheme.
  - i.e. sequence 3 bases within coding portions of genes translated to 1 amino acid (or terminates amino acid sequence).
- Mutation and Recombination occur at genotype level on DNA strings, whereas translated sequences of amino acids are proteins that comprise the basis of the phenotype upon which selection acts.
- 4^3 = 64 possible codon values, 20 amino acids (plus stop codon) = 21, therefore redundant coding scheme.

## Universal Codon Translation Table ##

- Non-random.
- Most redundancy occurs in 3rd codon position.
- There are biochemical constraints that have strongly influenced why live as we know it has evolved with a base alphabet of 4, a codon size of 3 and this particular redundant codon mapping to the 21 possible phenotypic outcomes.


## Overview ##



        4   2   2   4   5   6   8   1   2   4       genotype
          \                             /
              codon translation table
          16  21  1   5   16    3   5   6
                        |
                    Objective Function
                        | 
                    Fitness
        
        Codon Translation Table
        1
        2
        3
        4
        5
        ..
        21


## Universal Codon Translation Table ##


                          2nd Codon Position
                    
                          T       C       A       G
                    T    Phe     Ser     Tyr     Cys     T
                    T    Phe     Ser     Tyr     Cys     C
                    T    Leu     Ser     Stop    Stop    A
                    T    Leu     Ser     Stop    Trp     G
                    C    LEu     Pro     His     Arg     T
                    C    Leu     Pro     His     Arg     C
        1st         C    Leu     Pro     Gln     Arg     A
        Codon       C    Leu     Pro     Gln     Arg     G      3rd Codon Position
        Position    A    Ile     Thr     Asn     Se      T
                    A    Ile     Thr     Asn     Ser     C
                    A    Ile     Thr     Lys     Arg     A
                    A    Met     Thr     Lys     Arg     G
                    G    Val     Ala     Asp     Gly     T
                    G    Val     Ala     Asp     Gly     C
                    G    Val     Ala     Glu     Gly     A
                    G    Val     Ala     Glu     Gly     G

## Creation of Codon Translation Tables ##

- The universal codon translation table above has a similarity index of 0.92 and an adjacency index of 8.10.


### Similarity Index ###

- How similar codon triplets are within **semantic groups**.
- **semantic group**
  - Set of codon values that translate to the same phenotypic value.

- Similarity index $latex Sim_{t} $ for a codon mapping table $latex t $ with $latex m $ groups is:

        $latex Sim_{t}=\frac{{\displaystyle \sum_{g=1..m}\left[{\displaystyle \sum_{i=1..n_{g}-1}}{\displaystyle \sum_{j=i+1..n_{g}}}{\displaystyle \sum_{k=1..3}}C_{k}^{i}\equiv C_{k}^{j}\right]}}{{\displaystyle \sum_{g=1..m}S_{g}}} $

where:

        $latex C_{k}^{i}\equiv C_{k}^{j}\:\left\{ \begin{array}{c} 1\: C_{k}^{i}=C_{k}^{j}\\ 0\: otherwise\end{array}\right. $

and:

        $latex S_{g} $ - Sum of maximum possible allelels between 2 pairs of codons.
        $latex g $ - Group of codons.
        $latex n_{g} $ - Number of members in group.
        

- Similarity indexes range from 1.0 (each codon in group is similar as possible) to 0.0 (all pairs of codons in each codon group share common alleles).

### Adjacency Index ###

> Phenotypic value is considered adjacent to another phenotypic value if it 
> can be reached by a single base mutation in the genotype.
> The adjacency index of a codon table t with m groups is defined as the sum, 
> over all groups g, of the number of unique phenotypic values (not including 
> the phenotype for the group itself) that can be reached by any single allele 
> change in any codon value in the group.

> Higher adjacency indices imply more phenotypic values are adjacent
> (i.e. they define the average number of modes in the multi-modal mutation 
> step size distribution, not counting the mode at 0).


## Conclusions ##

> Optimal choice of how to organise codon translation table for a cyclical 
> fitness landscape appears to depend on whether it is more important 
> to minimise the variability of the solution quality over time (low similarity, high adjacency)
> or the evolution of the best solution quality over time (high similarity, low adjacency).

> High similarity and low adjacency are the characteristics that have evolved in the biological codon table.

