Categories: natural language
Tags: hash
      huffman
      coding
      bloom
      language
      spell
      list

### Reference ###

Development of a Spelling List, M.D. McIlroy, AT&T Bell Labs.

### Notes ###

#### On spell checking ####

- All leading and trailing punctuation is removed.
- Embedded punctuation is included.
- Hyphenated words are split to avoid cluttering the spelling list with innumerable ephemeral combinations.
- Derivable words were culled:
  - Capitalised words that were spelled like uncapitalised words.
  - Words with selected suffixes (e.g. *-s*, *-ment*, *-ical*) whose stems were also present and words with selected prefixes (*un-*, *dis-*, *non-*).
  - e.g. *Peters* was unnecessary and even *Peter=Pete+-er*.
- Spelling list of 24,000 words was quite effective.
- Spelling checker knows approximately 30 suffixes and 40 prefixes.
  - Words looked up by successively stripping suffixes, and within the suffix-stripping loop, by successively stripping prefixes until and exact match is found.
  - Prefixes may be found mindlessly, but suffixes are another matter.
  - Suffix Rules:
    - Suffix that begins with a vowel is not stripped when that would leave a monosyllable ending with vowel-consonant.
    - If, stripping such a suffix would leave a monosyllable with a final doubled consonant, one of the consonants may need to be stripped too.
      - e.g. Both the double and undoubled stems are tried, to insure finding derivations like *mapping->map* as well as *buzzed->buzz*.
      - Pertinent monosyllables for this rule are sets of letters containing exactly one vowel and non ending in *x* or *w*.
      - Thus *fad* and *ten* are pertinent monosyllables, *neat* and *mix* are not.
  - Prefix Rules:
    - They may be recognised in any order provided only that *under-*, when present, must be stripped in preference to *un-*.
    - Certain common prefixes, notably *in-* and *de-* excluded.
      - These prefixes are too unreliable, *in-* is confusable with *un-*, to say nothing of requiring special treatment when prefixed to words beginning with one of *l, m, p, r* as in *illicit, immeasurable, impossible, irrepresisible*.
    - Many words beginning with *de-* are not derived by prefixing at all, this prefix is not as productive as it might seem.

#### On Hashing ####

- Bloom filter succeeded in encoding 25,000 word list into 50,000 bytes.
- A differential huffman code, squeezed 30,000 words into 52,000 bytes.

#### Bloom Filter ####

- Spatters each entry randomly across a large bit table so thoroughly that each hash value cannot be reconstructed from the table.

##### Process #####

- Let N-bit table be initially clear.
- For each entry, compute k independent hash functions in the range 0 to N-1 and set corresponding bits of the table to 1.
- To probe table, ask whether all k designated bits are 1.
- Remainders modulo the k largest primes less than N constitute a convenient and effective set of hash functions.
- As the last few bits of the hash table do not pull full weight in the scheme, the table is effectively shorter than N bits.

##### Theory #####

- To achieve maximum information (i.e. minimal error rate for given number of entries), the bits of the table should take the values 0 and 1 with equal probability.
- The probability q of a bit being 0 is:

        $latex q=\left(1-{\displaystyle \frac{1}{N}}\right)^{km}\approx e^{-km/N} $

  - where m is the number of entries, q becomes $latex {\displaystyle \frac{1}{2}} $ when:

        $latex k={\displaystyle \frac{N}{m}}log(2) $

  - The probability of false acceptance in this instance is:

        $latex (1-q)^{k}=2^{-k} $

##### Notes #####

- For 25,000 word list hashed into 25,000 16 bit words (or 400,000 bits), the optimal number of hash functions was $latex k=11 $ and the probability of false acceptance was 1 in 20000.

#### Compressing Conventional Hash ####

- If each entry of a $latex v$ -member vocabulary is hashed into $latex b $ bits, and only the hash values are remembered, the probability of false acceptance with be the probability of accidentally hashing into a good value, namely $latex v/2^{b} $.
- A desirable vocabulary size for a spelling list is about 30,000 or roughly $latex 2^{15} $ words, a desirable error rate of about 1 in $latex 2^{12} $; thus an appropriate hash size is 27 bits.
- There are:

        $latex \left[\begin{array}{c} 2^{b}\\ v\end{array}\right] $

  - possible sets of $latex v $ distinct hash values, so

        $latex log\_{2}\left[\begin{array}{c} 2^{b}\\ v\end{array}\right]=v(b-log\_{2}(v/e)) $

  - bits are required to encode the set. In our case, $latex v=30000 $ and $latex b=27 $, which works out to 13.57 bits per entry.

- When the values are listed in order, the mean first difference, $latex a $, is given by:

        $latex a={\displaystyle \frac{2^{b}}{v}} $

  - so differences should be typically represented in about $latex b-log_{2}(v) $ bits, in our case 12.

- By storing differences, we may expect to compress the list of hash values nearly to information-theoretic limit.

- Regard the ordered sequence of hash values as having been chosen by a Poisson process with rate $latex v/2^{b} $.
  - Differences exponentially distributed with mean $latex a=2^{b}/2 $.
  - With $latex a=2^{27}/30000 $ as before, an infinite huffman code has an expected codeword length of 13.60 bits.

- To look up a hash code
  - Sum the differences from the beginning until the value sought is reached or passed (which can be time consuming).
  - Partitioning the table into M bins, searching improved by a factor of M (but requires small additional space).
  - For this case, extra space for pointers to 512 bins brings effective mean codeword length to 14.01 bits.

#### Infinite Huffman Codes ####

- Infinite set of messages with independent probabilities 1/2, 1/4, 1/8, .. has entropy of 2 bytes and a perfect huffman code 0, 10, 110, 1110, ..
  - This geometric series, has a self similar code, i.e.
    - Any tail is shifted and 1 padded replicate of the whole.
- In general a set of probabilities:

        $latex P_{i}=(1-r)r^{i}\qquad=0,1,2.. $

  - where $latex r^{m}={\displaystyle \frac{1}{2}} $ for some integer *m* will be self similar in blocks of length *m*, removing an initial block scales the block by a factor of 2.

- Code self similar in blocks of *m* with each block 1 bit longer than the block before (i.e. golomb codes).
- In general for *r*, m must be taken to be the least integer s.t. $latex r^{m} \leq {\displaystyle \frac{1}{2}} $ 

#### Example ####

- Let the first codeword of length *k* end in 0 and let succeeding codewords of that length count in binary.
- If value of the first codeword is *2x*, then by self similarity the *m*th codeword must be $latex 2^{k}+2x $.
  - And the *k*th bit of this *k*+1 bit codeword must have value $latex 2x+m $.

- e.g. *k=4* and *x=3*

          0 110     
          0 111     
          1 000     
          1 001     
          1 010     
                    
        1 0 110     Overlap's with 0 110
        1 0 111     
        1 1 000     
        1 1 001     
        1 1 010     

  - Code self similar by blocks of length *m=5* 
  - *k*-bit codes count from *2x=6* up to *2x+m=11*

- For given *m*, length of the codewords in the first full block of equal length codewords is the least integer *k* that satisfies:

        $latex 2(2x+m)=2^{k}+2x $

  - For some nonnegative integer *x*, therefore:

            $latex k=log_{2}(m) $
            $latex x=2^{k-1}-m=2^{log_{2}(m)}-m $

  - We know the mean *a*, therefore we can compute:

            $latex r=a/(1+a) $
            $latex m=-log(2)/log(r) $

- When $latex x \neq 0 $, the first *x* codewords of entire code have length *k-1* and values *0* through *x-1*
  - i.e.

               000    -|
               001     | x=3
               010    -|
                      
              0110    -|
              0111     |
              1000     | m=5
              1001     |
              1010    -|
                      
            1 0110    

##### Decoding #####

        w=k-1 bits of cipher text
        if w < x
          first word of cipher text is w, as is clear text
        else
          u=w
          while u < 2x+m
            s += 1
            extend u by 1 bit
          
          w=cipher text
          clear text=x+u+(s-1)m 

##### Notes #####

- Expected codeword length:

        $latex {\displaystyle \sum_{i=0}^{\infty}P_{i}L_{i}=k-1+\frac{r^{x}}{1-r^{m}}} $

  - where $latex L\_{i} $ is the length of the *i*th codeword.
  - Since $latex r^{m}={\displaystyle \frac{1}{2}} $, mean length of a codeword is:

    $latex k-1+2r^{x}\qquad which\; varies\; between\; k\; and\; k+1\; as\; x\; varies\; between\; m\; and\; 0$

