Categories: genetic algorithms
Tags: gene
      expression
      algorithm
      programming
      genetic
      
## Reference

- Gene Expression Programming: A New Adaptive Algorithm for Solving Problems. Candida Ferreira, Universidade dos Acores. Complex Systems, Vol 13, issue 2: 87-89, 2001.


## Introduction

- Similar Genetic Algorithms i.e. "uses populations of individuals, selects them according to fitness, and introduces genetic variation using one or more genetic operators."
- Difference to traditional:
  - Genetic Algorithms (GAs)
    - Individuals linear strings, fixed length (chromosomes).
  - Genetic Programming (GP)
    - Individuals nonlinear entities, different sizes and shapes (parse trees).
  - Gene Expression Programming (GEP)
    - Individuals initially fixed length strings (chromosomes), later expressed as nonlinear entities of different sizes (expression trees).
- Developmental Genetic Programming (DGP)
  - Form of Genetic Programming.
  - Binary strings used to encode mathematical expressions.
  - Illegal mathematical expressions common during evolution, computational effort to edit illegal expressions.
- GEP organises chromosomes to prevent translation into illegal structures.

### Life

- Thresholds of any life explosion:

#### Replicator Threshold

- Self copying system in which there is hereditary variation.
- Replicators survive by virtue of their own properties.

#### Phenotype Threshold

- Replicators survive by virtue of causal effects on something else - the phenotype.

## Implementation

              1. Create Chromosome of Initial Population
              
              2. Express Chromosomes
              
              3. Execute Each Program
              
              4. Evaluate Fitness
              
              5. Iterate or Terminate?        -->       End
                      |
                      | Iterate
                      \/
              6. Keep Best Program
              
              7. Select Programs
              
              8. Replication                ---+
                                               |
              9. Mutation                      |
                                               |
              10. IS Transposition             |
                                               |
              11. RIS Transposition            |      Reproduction
                                               |
              12. Gene Transposition           |
                                               |
              13. 1-Point Recombination        |
                                               |
              14. 2-Point Recombination        |
                                               |
              15. Gene Recombination        ---+
              
              16. Prepare New Programs of Next Generation
              

### 1. Create Chromosome of Initial Population

- Random generation of chromosomes of the initial population.

### 2. Express Chromosomes

### 3. Execute Each Program

### 4. Evaluate Fitness

- Individuals selected according to fitness to reproduce with modification, leaving progeny with new traits.

### 5. Iterate or Terminate?

### 6. Keep Best Program

## Genome

- genome/chromosome consists of linear fixed length symbolic string composed of >= 1 genes.
  - **Genes are of equal length.**
- Utilises Opening Reading Frames (ORFs) from biology.
  - **ORFs are variable length.**

### Open Reading Frames

- Coding sequence of gene.
- Begins with "start" codon, continues with amino acid codons and ends with a "termination" codon.
- In nature, Sequences also exist upstream from the start codon and downstream from the end codon.
- In GEP, start codon always first position in gene, but termination point does not always coincide with last position of gene.
  - i.e. non coding regions downstream from termination point.

#### Example

- Equation:

        $latex Q=\sqrt{(a+b)\times(c-d)} $

- Expression Tree (ET) (phenotype of GEP):

<!-- gep-cf-1.png -->
![](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6dTNTR0g1dG9pbkk "gep-cf-1.png")


- Genotype:
  - ORF starting at `Q` and terminating at `d`.
  - Author calls these ORFs K-expressions.
  - Note, when translating genotype, a leaf is complete when it is composed of variables or constants.

            01234567
            Q*+-abcd

### GEP Genes/Chromosomes

- GEP Genes composed of head and tail.
  - Head contains symbols that represent both functions (elements from the function set F) and terminals (elements from the terminal set T).
  - Tail contains only terminals.
  - i.e. 2 different alphabets occur at different regions within gene.

#### Example

- Gene composed of the following symbols:

        {Q,*,/,-,+,a,b}

- Example genotype:

        012345678901234567890
        +Q-/b*aaQbaabaabbaaab

- Expression Tree:

<!-- gep-cf-2.png -->
![](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6NUJmNFkwVFRJLTg "gep-cf-2.png")

  - ORF ends at position 10, gene ends at position 20.

- Mutation at position 9 changing `b` into `+`, new genotype:

            012345678901234567890
            +Q-/b*aaQbaabaabbaaab

<!-- gep-cf-3.png -->
![](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6dUt2NVlYLVpTbDg "gep-cf-3.png")

#### Translation

- Assemblage complete when baseline composed of only terminals (variables/constants) formed.

## Gene Programming

- Given:
  - Length of head $latex h $.
  - Number of arguments $latex n $.

- The length of the tail ($latex t $) is:

      $latex t=h(n-1)+1 $

- e.g. for a gene with the symbols `{Q,*,/,-,+,a,b}`, $latex n=2 $ and $latex h=10 $.

      $latex t=10(1)+1=11 $

- therefore the length of the gene ($latex l $) is:

      $latex l=10+11=21 $

### Example

- Gene:

          0123456789 01234567890
          +Q-/b*aaQb aabaabbaaab 

- ORF:
  - ORF ends at position 10.
  - Gene ends at position 20.

<!-- gep-cf-4.png -->
![](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6OFdJemQwMm5jWTg "gep-cf-4.png")

### Mutation

- Mutation at position `9`, changing `b` into `+`.
- Gene:

          0123456789012 34567890
          +Q-/b*aaQ+aab aabbaaab

<!-- gep-cf-5.png -->
![](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6R1psMHYwUE9MQ2M "gep-cf-5.png")

- i.e. the termination point shifts 2 positions.

### Notes

- Despite fixed length gene's, each gene has potential to code for ETs of different sizes and shapes.
- Modifications made in genome, always result in valid ET.
- Linking function, number of genes and length of each gene are chosen a-prior for each problem.
  - e.g. start by using single gene chromosome, gradually increasing the length of the head.
  - If gene becomes large, increase the number of genes and choose a function to link them.


### Multigenic Chromosomes

- e.g. chromosome length 27

          0123456789012345678901234567890
          -b*babbab*Qb+abbba-*Qabbaba

- Translates to 3 ORFs
  - Position 0 marks the start of each gene.
  - End evident on construction of ORF.

<!-- gep-cf-6.png -->
![](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6LWplaDZlNkpodUk "gep-cf-6.png")

- i.e. GEP chromosomes code for >= 1 ORFs and depending on the task:
  - Sub-ET's may be selected individually according to their fitness (e.g. in problems with multiple outputs).
  - Or whole multi-subunit ET may be used.
- Linking functions for Sub-ET's:
  - Chosen a-priori.
  - In nature, akin to the assemblage of different protein subunits into a multi-subunit protein.
  - Any mathematical or boolean function with more than one argument.

#### Example

- A three-genic chromosome:
  - `N` - NOT (function of 1 argument).
  - `A` - AND (function of 2 arguments).
  - `O` - OR (function of 2 arguments).

- e.g. chromosome:

          IIAIca3aa2acuNNAOab2u3c31cAu12ua3112cac

- ET:

<!-- gep-cf-7.png -->
![](http://drive.google.com/uc?export=view&id=0B4Ieh2JkdcY6UG9HcGxIbUk5RG8 "gep-cf-7.png")


### Translation

- i.e. transfer information from a gene to an ET.
  - simpler form than the expression of genetic information in nature.
- Note, in GEP, no need for transcription (i.e. the message in the gene is directly translated into an ET).
- 4 cases (for all cases whole organism encoded in a linear genome):
  1. Single Gene
      - "Organism" is the product of a single gene (i.e. the ET).
  2. Multi Subunit ET
      - Different sub-ETs linked together by particular function.
  3. Spatial Multi Subunit ET 
      - "Organism" emerges from spatial organisation of different sub-ETs
      - e.g. in planning and problems with multiple outputs.
  4. Domain Organised Multi Subunit ET
      - "Organism" emerges from interactions of sub-ETs with different domains.
      - e.g. neural networks.

## Fitness Function


- If range of selection excessively narrowed, populations evolve slowly and incapable finding correct solution.
  - If, the opposite is done, and range of selection is broadened, numerous solutions appear with maximum fitness that are far from good solutions.
- To overcome this, a broad limit for selection (e.g. a relative error of 20%) is chosen.
  - Allows evolutionary process to get started.
- Following equations can be used to generate the fitness using relative/absolute errors:

        $latex f_{i}={\displaystyle \sum_{j=1}^{{\displaystyle C_{t}}}}(M-\mid C_{ij}-T_{j}\mid)\qquad(i)\;(Absolute\; Error) $
        $latex f_{i}={\displaystyle \sum_{j=1}^{{\displaystyle C_{t}}}}(M-\mid{\displaystyle \frac{C_{ij}-T_{j}}{T_{j}}}\mid\cdot100)\qquad(ii)\;(Relative\; Error) $

  - where:
      - $latex M $ - Range of selection.
      - $latex C\_{ij} $ - Result of fitness case $latex j $ for chromosome $latex i $.
      - $latex T\_{j} $ - Target value for fitness case $latex j $.

- Note, for boolean concept learning/logic synthesis:
  - Fundamental to penalise individuals able to solve 50% of fitness cases correctly (i.e. a 50/50 chance to solve a boolean operation!).
  - Select individuals able to solve 50-75% of fitness cases.
  - An alternative fitness function should be used:

          $latex If\; n\geq\frac{1}{2}C\_{t}\; then\; f\_{t}=n;\; else\; f\_{t}=1 $

    - where:
        - $latex n $ - Number of fitness cases correctly evaluated.
        - $latex C\_{t} $ - Total number of fitness cases.


## Selection

- For complex problems, roulette-wheel selection with elitism (Goldberg).

## Reproduction with Modification

### Replication

- According to fitness and luck (roulette) chromosomes copied into next generation.
- Does not really contribute anything to genetic diversity.

### Mutation

- Can occur anywhere within the chromosome (structural organisation must remain intact).
  - Head, can change to function or terminal.
  - Tail, terminals can only chance to terminals.
- Typically mutation rate ($latex p\_{m} $) equivalent to 2 point mutations per chromosome.
- In nature, neutral mutations can occur (mutations in introns, mutations that result in same amino acid due to redundancy of genetic code).
- In ET, mutations usually have an effect.


### Transposition

- Fragments of genome, can be activated and jump to another place in the chromosome.
- GEP, 3 kinds of transposable elements:
  1. Insertion Sequence (IS) Elements
      - Short fragment.
      - Function/terminal in first position.
      - Transpose to head of genes, except root.
  2. Root Insertion Sequence (RIS) Elements
      - Short fragment.
      - Function in first position.
      - Transpose to root of genes.
  3. Entire Genes
      - Transpose to beginning of chromosome.

#### IS Elements

- Randomly selected throughout chromosome.
- Copy made, inserted in any position in head of gene, except start.
- IS Transposition Rate ($latex p\_{is} $) is 0.1.
- Set of 3 IS elements of different length used.
- Chosen at random (by transposition operator):
  - Chromosome
  - Start of IS element
  - Target Site
  - Length of transposon
- Notes:
  - Sequence upstream of transposition site unchanged.
  - Sequence downstream loses length of IS element.
  - Can drastically reshape ET, more upstream, more profound the change.
  - High hit rate at lowest levels of ETs

##### Example

- 3-genic chromosome (length 20)

              |                           | | 
        012345678901234567890 012345678901234567890
        *-+*a-+a*bbabbaababab Q**+abQbb*aabbaAAAbba

- Transposition:
  - Chromosome: Gene 2
  - Start: 12
  - End: 14
  - Target Site: bond 6 in gene 1

- Result:

              |
        012345678901234567890 012345678901234567890
        *-+*a-bba+babbaababab Q**+abQbb*aabbaAAAbba

- Note, left shift occurs only in the current gene, other genes remain unaffected.

#### RIS Elements

- Chosen among sequence of heads.
  - Point chosen in head and scanned until function found.
  - Function becomes start of RIS element.
- RIS Transposition Rate ($latex p\_{is} $) is 0.1.
- Set of 3 RIS elements of different length used.
- Chosen at random (by transposition operator):
  - Chromosome
  - Start of RIS element
  - Target Site
  - Length of transposon
- Notes:

##### Example

- 2-genic chromosome (length 20)
                                  
                                  | |
        012345678901234567890 012345678901234567890
        -ba*+-+-Q/abababbbaaa Q*b/+bbabbaaaaaaaabbb


- RIS Transposition:
  - Chromosome: Gene 2
  - Start: 4
  - End: 6
  - Target Site: root in gene 2

- Result:
                              |
        012345678901234567890 012345678901234567890
        -ba*+-+-Q/abababbbaaa ++bQ*b/+bbaaaaaaaabbb

- Note, as before, left shift occurs only in the current gene.

##### Notes

- RIS transposition causes radical changes to chromosome.
  - i.e. excellent for causing genetic variation.

#### Gene Transposition

- Entire gene functions as transposon to beginning of chromosome.
- Transposon (gene) deleted in place of origin (so length of chromosome maintained).
- Chromosome for expression randomly chosen and 1 of its genes (except for first) chosen to transpose.

##### Example

- 3-genic chromosome (length 24):

                 |       |
        012345678012345678012345678
        *a-*abbab-QQ/aaabbQ+abababb

- Gene Transposition:
  - Chromosome: Gene 2
  - Target Site: Gene 1

- Result:

        |
        012345678012345678012345678
        -QQ/aaabb*a-*abbabQ+abababb


##### Notes

- Duplication genes plays important role in biology and evolution.


### Recombination

- Unable to create new genes, only rearrange existing genes.
- When only recombination used as source of genetic variation, complex problems only solved with very large initial populations.
- i.e. GEP relies not only on shuffling genes, but in the constant creation of new genetic material.


#### One-point Recombination

- Chromosomes crossover a randomly chose point to form 2 daughter chromosomes.
- One-point recombination rate ($latex p\_{1r} $) depends on rates of other operators.
  - Global crossover rate (sum of all 3 kinds recombination) typically *0.7*.

##### Example

- Parent chromosomes:

          |
        012345678012345678
        -b+Qbbabb/aQbbbaab
        /-a/ababb-ba-abaaa

- Recombination:
  - Crossover Point (random): Bond 3, gene 1

- Result (offspring):

          |
        012345678012345678
        -b+/ababb-ba-abaaa
        /-aQbbabb/aQbbbaab

##### Notes

- Most of the time, offspring exhibit different properties.
- Important source genetic variation.
- After mutation, one of operators most seen in GEP.

#### Two-Point Recombination

- Chromosomes paired.
- Two points of recombination randomly chosen.

##### Example

- Parent chromosomes:

              |       | 
        01234567890 01234567890
        +*a*bbcccac *baQ*acabab
        *cbb+cccbcc ++**bacbaab 


- Recombination:
  - First Crossover Point (random): Bond 7, Gene 1
  - Second Crossover Point (random): Bond 3, Gene 2

- Result (offspring):


              |       | 
        01234567890 01234567890
        +*a*bbccbcc ++*Q*acabab
        *cbb+ccccac *ba*bacbaab
        

##### Notes

- First gene, split downstream, not affecting ORF.
- Second gene, split upstream, profoundly changing ORF.
- Two-point recombination greater transforming power than one-point recombination.
- Good for complex problems, esp. when multigenic chromosomes composed of several genes used.

#### Gene Recombination

- Entire gene exchange during crossover.
- Exchanged genes randomly chosen, occupy same position in parent chromosome.

##### Example

- Parent chromosomes:

                |        |
        012345678012345678012345678
        /aa-abaaa/a*bbaaab/Q*+aaaab
        /-*/abbabQ+aQbabaa-Q/Qbaaba

- Recombination:
  - Crossover Point (random): Gene 2

- Result (offspring):
        
                |        |
        012345678012345678012345678
        /aa-abaaaQ+aQbabaa/Q*+aaaab
        /-*/abbab/a*bbaaab-Q/Qbaaba

### Implementation Notes 

- Advisable to start with short, single-gene chromosomes and then gradually increase *h*.
- GEP can efficiently evolve solutions using large values of *h* (i.e. complex sub ETs).
- GEP can cope well with excess of genes.
- Sometimes impossible to find perfect solution using gene shuffling only.
  - Even using generalised shuffling (e.g. gene recombination with gene transposition) can also result in oscillatory dynamics.








