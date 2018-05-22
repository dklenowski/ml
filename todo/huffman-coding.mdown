Categories: compression
Tags: algorithms
      huffman

## Huffman Coding ##

### Reference ###

A Concise Introduction to Data Compression. Salomon, D. 2008, Springer.

### Introduction ###

- Similar to Shannon Fano method.
- Produces best variable length codes when the probabilities of the symbols are negative powers of 2.
- Is a minimum length code in the sense that no other code has a shorter average length.
- Huffman codes are at most 0.1 bits longer (per symbol) than an ideal entropy encoder such as an arithmetic code.
- In general for *n* symbols:
  - $latex 2^{n-1} $ different huffman code trees.
  - $latex (n-2)!*(n-2) $ different huffman codes.


### Encoding Algorithm ###

Pseudocode:

        Build list of alphabet symbols in descending order of there probabilities
        Shift 2 lowest prority alphabet symbols and form a tree
        While list is not empty
          Shift lowest priority symbol
          Create new root node and use shifted symbol as leaf
        Arbitrarily assign 0/1 bits to left/right branches in tree and generate huffman table

### Encoding Example ###

#### Generate alphabet

        a1    0.4
        a2    0.2
        a3    0.2
        a4    0.1
        a5    0.1
        
#### Form tree with 2 lowest priority alphabet symbols

          a45    0.2 
          / \
         /   \
        a5   a4
        .1   .1

#### While list is not empty

##### Shift lowest priority symbol and create new root node and use shifted symbol as leaf

<pre>
     a345   0.4
    / \
   /   \
  / \   \
 /   \   \
a5   a4  a3
.1   .1  .2

     a2345    0.6
      / \
     /   \
    / \   \
   /   \   \
  / \   \   \
 /   \   \   \
a5   a4  a3   a2 
.1  .1   .2   .2

        a12345    1.0
        / \
       /   \
      / \   \
     /   \   \
    / \   \   \
   /   \   \   \
  / \   \   \   \
 /   \   \   \   \
a5   a4  a3   a2  a1
.1  .1   .2   .2  .4
</pre>

#### Assign 0/1 to left and right branches and generate table

- Using *Left 0, Right, 1*

            a1      1
            a2      01
            a3      001
            a4      0001
            a5      0000

- Using the above symbols, the average size of code is defined as:

            P(a1)*<a1 bits>+P(a2)*<a2 bits>+P(a3)*<a3 bits>+P(a4)*<a4 bits>+P(a5)*<a5 bits>

- which is:

            (0.4*1)+(0.2*2)+(0.2*3)+(0.1*4)+(0.1*4)=2.2 bits/symbol

- with a variance of:

            0.4(1-2.2)^2+0.2(2-2.2)^2+0.2(3-2.2)^2+0.1(4-2.2)^2+0.1(4-2.2)^2=1.36

- Note, we want trees with a smaller variance for network communication (as larger variances can encode to generate bits at a rate that varies with time, therefore requiring a buffer on the receiver end).

#### Notes ####

- The reference text flips the way a branch is added to the tree for *a345*, this does not improve the result (i.e has the same code size and variance).
- i.e.

<pre>
  a45    0.2 
  / \
 /   \
a5   a4
.1   .1

    a345    0.4
    / \ 
   /   \
  /   / \
 /   /   \
a3   a5   a4
.2   .1   .1

      a2345     0.6
      / \
     /   \
    / \   \
   /   \   \
  /   / \   \
 /   /   \   \
a3   a5   a4  a2
.2   .1   .1  .2

        a12345    1.0
        / \
       /   \
      / \   \
     /   \   \
    / \   \   \
   /   \   \   \
  /   / \   \   \
 /   /   \   \   \
a3   a5   a4  a2  a1
.2   .1   .1  .2  .4
</pre>

- With a symbol table:

          a1      0
          a2      10
          a3      111
          a4      1100
          a5      1101

- The text also uses the following rule to reduce the variance:
  - "When there are more than 2 smallest probability nodes, select the ones that are lowest and highest in the tree and combine them".
  - But this did not match on the tree that was created (as branches were added to both the left and right, apparently randomly!).

### Caveats ###

- Huffman coding cannot compress text with equal probabilities (e.g. random text).
- Huffman coding cannot be applied to a 2 symbol alphabet.

### Decoding Algorithm ###

Pseudocode:

        Assume tree was generated with left 0 and right 1
        Move to root of tree
        Read bit of input (in compressed file)
          If 0, follow bottom edge of tree
          If 1, follow top edge of tree
          If leaf, symbol found
            Emit code
            Move to root of tree
        Until end of input

#### Decoding Tables ####

- Used to improve decoding performance.
- Trade-off between chunk size and decoding speed.
  - Large chunks speed up decoding but require large tables.
  - A large alphabet requires a large set of tables.
  - Large tables have to be setup before decoding can start, and may preempt any performance gains in decoding speed.
- Process involves creating partial decoding tables for a huffman code.
- Process:
  - Break huffman code into *k* bit chunks.
  - Setup the first table:
    - Generate $latex 2^{k} $ bit patterns 0 through $latex 2^{k}-1 $.
    - Decode each pattern and record corresponding decoded string.
    - Record any pattern that has a remainder (the remainder is used as an index to a table that can be used to completely decode the chunk).
  - Subsequent tables can be generated as needed and use remainders from previous tables as prefixes.
    - i.e. once decoder decides that table 1 corresponds to prefix *p*, it generates $latex 2^{k} $ patterns *p|00...0* through *p|11...1*.
    - Number of partial decoding tables equals the number of interior nodes plus the root.
    - Partial decoding tables begin with code prefixes.
  - Decode each pattern, where remainders exist, generate Subsequent tables using the same procedure discussed above.

##### Example #####

- Huffman Table:

        a1    0
        a2    1 0
        a3    11 1
        a4    110 1
        a5    110 0

- Huffman Tree:

<pre>
        / \
       /   \
      / \   \
     /   \   \
    / \   \   \
   /   \   \   \
  /   / \   \   \
 /   /   \   \   \
a3   a5   a4  a2  a1
</pre>


- Encoded String:

        0|0|10|1101|111|0|1100
        a1|a1|a2|a4|a3|a1|a5

- Using *k=3*

        001|011|011|110|110|0

- Partial Decoding Tables:

                  T0                    T1=1                      T2=11                     T3=110      
          Bits  Decode  Rem      Bits   Decode  Rem       Bits    Decode  Rem       Bits     Decode  Rem
          000   a1a1a1  0        1|000  a2a1a1  0         11|000  a5a1    0         110|000  a5a1a1  0  
          001   a1a1    1        1|001  a2a1    1         11|001  a5      1         110|001  a5a1    1  
          010   a1a2    0        1|010  a2a2    0         11|010  a4a1    0         110|010  a5a2    0  
          011   a1      2        1|011  a2      2         11|011  a4      1         110|011  a5      2  
          100   a2a1    0        1|100  a5      0         11|100  a3a1a1  0         110|100  a4a1a1  0  
          101   a2      1        1|101  a4      0         11|101  a3a1    1         110|101  a4a1    1  
          110   -       3        1|110  a3a1    0         11|110  a3a2    0         110|110  a4a2    0  
          111   a3      0        1|111  a3      1         11|111  a3      2         110|111  a4      2  
      

- Decoding:

          001       a1a1    0 remainder
          011       a2      2 remainder (table 2)
          11011     a4      1 remainder (table 1)
          1110      a3a1    0 remainder
          110       -       3 remainder
          1100      a5      n/a 







          
          
          
          


