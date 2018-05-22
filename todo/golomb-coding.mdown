Categories: compression
Tags: algorithms
      golomb

### Reference ###

IEEE Transactions on information Theory, Run Length Encoding, 1966.

### Notes

- Alternative to huffman coding, but can be used to code an infinite list.

### Theory ###

- In general let $latex k $ be the smallest positive integer such that $latex 2\_{k} \geqq 2m $.
- Code dictionary contains exactly $latex m $ words of every word length $latex \geqq k $ as well as $latex 2^{k-1}-m $ words of length $latex k-1 $.
  - Note, when $latex m $ is a power of 2 the collection of words of length $latex k-1 $ is empty.

- In general if:

      $latex m=\frac{{\displaystyle -log(2)}}{{\displaystyle log(p)}} $

  - is not an integer, the best dictionary will oscillate between $latex [m] $ words of a given length and $latex [m]+1 $ words of another length (where $latex [m] $ is the greatest integer $latex \geqq m $).
    - Note, for large $latex m $, little penality for picking the nearest integer when designing the code.



### e.g. m=16 ###

- Since $latex m=16 $ is a power of 2.

      $latex 2^{k}\geqslant2m $

  - Therefore $latex m=5 $.

- To decode a number as $latex x $.

      $latex x=16A+R $
  
  - where:

      $latex R=Last\:5\: bits\: where\:0\leqslant R\leqslant15 $
      $latex A=Number\: of\:ones\: proceeding\: the\: first\:0 $

- To encode the number $latex N $.

  - Divide $latex N $ by 16 to get $latex N=16A+R $ and write $latex A $ 1's followed by the 5-bit representation of $latex R $.

- e.g.

        Number  Code        Binary        Result
        0       00000       00000         16*0+0=0
        1       00001       00001         16*0+1=1
        2       00010       00010         16*0+2=2
        3       00011       00011         16*0+3=3
        4       00100       00100         16*0+4=4
        5       00101       00101         16*0+5=5
        6       00110       00110         16*0+6=6
        7       00111       00111         16*0+7=7
        8       01000       01000         16*0+8=8
        9       01001       01001         16*0+9=9
        10      01010       01010         16*0+10=10
        11      01011       01011         16*0+11=11
        12      01100       01100         16*0+12=12
        13      01101       01101         16*0+13=13
        14      01110       01110         16*0+14=14
        15      01111       01111         16*0+15=15
                            
        16      1 00000     00000         16*1+0=16
        17      1 00001     00001         16*1+1=17
        18      1 00010     00010         16*1+2=18
        19      1 00011     00011         16*1+3=19
        20      1 00100     00100         16*1+4=20
        21      1 00101     00101         16*1+5=21
        22      1 00110     00110         16*1+6=22
        23      1 00111     00111         16*1+7=23
        24      1 01000     01000         16*1+8=24
        25      1 01001     01001         16*1+9=25
        26      1 01010     01010         16*1+10=26
        27      1 01011     01011         16*1+11=27
        28      1 01100     01100         16*1+12=28
        29      1 01101     01101         16*1+13=29
        30      1 01110     01110         16*1+14=30
        31      1 01111     01111         16*1+15=31
        
        32      11 00000    00000         16*2+0=32
        33      11 00001    00001         16*2+1=33
        34      11 00010    00010         16*2+2=34
        35      11 00011    00011         16*2+3=35
        36      11 00100    00100         16*2+4=36
        37      11 00101    00101         16*2+5=37
        38      11 00110    00110         16*2+6=38
        39      11 00111    00111         16*2+7=39
        40      11 01000    01000         16*2+8=40
        41      11 01001    01001         16*2+9=41
        42      11 01010    01010         16*2+10=42
        43      11 01011    01011         16*2+11=43
        44      11 01100    01100         16*2+12=44
        45      11 01101    01101         16*2+13=45
        46      11 01110    01110         16*2+14=46
        47      11 01111    01111         16*2+15=47


### e.g. m=14

- Since $latex m $ is a NOT power of 2.

      $latex m=14 $ therefore $latex k=5 $ and $latex 2^{k-1}-m=2 $

- therefore 2 codewords of length 4, followed by 14 codewords of lengths 5, 6, 7 etc

- To decode a number as $latex x $:

  - For $latex A $ 1's followed by 3 0's.

      $latex x=14A+R^{`} $

      - where:

          $latex R^{`}=Last\:4\: bits\: where\:0\leqslant R\leqslant15 $
          $latex A=Number\: of\:ones\: proceeding\: the\: first\:0 $

  - For $latex A $ 1's and the next 3 bits are not all 0's
  
      $latex x=14A+R-2 $
  
      - where:
  
          $latex R=Last\:5\: bits\: where\:0\leqslant R\leqslant31 $
          $latex A=Number\: of\:ones\: proceeding\: the\: first\:0 $

- i.e.

        Number  Code        Binary        Result
        0       0000        0             14*0+0=0
        1       0001        1             14*0+1=1
                                          
        2       00100       00100         14*0+4-2=2
        3       00101       00101         14*0+5-2=3
        4       00110       00110         14*0+6-2=4
        5       00111       00111         14*0+7-2=5
        6       01000       01000         14*0+8-2=6
        7       01001       01001         14*0+9-2=7
        8       01010       01010         14*0+10-2=8
        9       01011       01011         14*0+11-2=9
        10      01100       01100         14*0+12-2=10
        11      01101       01101         14*0+13-2=11
        12      01110       01110         14*0+14-2=12
        13      01111       01111         14*0+15-2=13
        14      1 0000      0000          14*1+0=14        A 1's followed by 3 or more 0's
        15      1 0001      0001          14*1+1=15        A 1's followed by 3 or more 0's
                                          
        16      1 00100     00100         14*1+4-2=16
        17      1 00101     00101         14*1+5-2=17
        18      1 00110     00110         14*1+6-2=18
        19      1 00111     00111         14*1+7-2=19
        20      1 01000     01000         14*1+8-2=20
        21      1 01000     01000         14*1+9-2=21
        22      1 01001     01001         14*1+10-2=22
        23      1 01010     01010         14*1+11-2=23
        24      1 01011     01011         14*1+12-2=24
        25      1 01100     01100         14*1+13-2=25
        26      1 01101     01101         14*1+14-2=26
        27      1 01111     01111         14*1+15-2=27
        28      11 0000     0000          14*2+0=28         A 1's followed by 3 or more 0's
        29      11 0001     0001          14*2+1=29         A 1's followed by 3 or more 0's
                                                            
        30      11 00100    00100         14*2+4-2=30
        31      11 00101    00101         14*2+5-2=31
        32      11 00110    00110         14*2+6-2=32
        33      11 00111    00111         14*2+7-2=33
        34      11 01000    01000         14*2+8-2=34
        35      11 01001    01001         14*2+9-2=35
        36      11 01010    01010         14*2+10-2=36
        37      11 01011    01011         14*2+11-2=37
        38      11 01100    01100         14*2+12-2=38
        39      11 01101    01101         14*2+13-2=39
        40      11 01110    01110         14*2+14-2=40
        41      11 01111    01111         14*2+15-2=41
        42      111 0000    0000          14*3+0=42         A 1's followed by 3 or more 0's
        43      111 0001    0001          14*3+1=43         A 1's followed by 3 or more 0's
                              
        44      111 00100   00100         14*3+4-2=44
        45      111 00101   00101         14*3+5-2=45
        46      111 00110   00110         14*3+6-2=46
        47      111 00111   00111         14*3+7-2=47
        
        
        