Categories: natural language
Tags: word
      text
      compression



### Reference ###

Constructing Word-Based Text Compression Algorithms. R. Nigel Horspool and Gordon V. Cormack.

### Notes ###

- All algorithms in the text are based on "strict" alternate maximal strings of alphanumeric and non-alphanumeric characters.

- Major problem with word based compression algorithms.
  - The number of distinct words that the algorithm has to process is potentially unbounded.
  - Therefore no sense to implement an algorithm that requires a pre-determined finite alphabet.

- General mechanism for handling a new word involves using an escape code.
  - When compression algorithm hits a new word, outputs an escape code followed by some representation of the new word.

- Algorithms use 2 alphabets $latex \sum\_{A} $ , the alphabet of alphanumeric words and $latex \sum\_{B} $ , the alphabet of punctuation strings.

#### Word Based Adaptive Huffman Coding ####

      
      AFreq = frequencies of alphanumeric words
      PFreq = frequencies of punctuation strings
      
      AHuffman = huffman codes for alphanumeric words
      PHuffman = huffman codes for punctuation strings
      
      repeat
        read one alphanumeric word, AW
        if $latex AW\not\in\sum_{A} $ then
          output AHuffman[escape]
          output text of AW
          $latex \sum_{A}=\sum_{A}\cup\{AW\} $
          AFreq[AW] = 1
          AFreq[escape] += 1
        else
          output AHuffman[AW]
          AFreq[AW] += 1
        endif
        
        AHuffman = recomputated table of huffman codes from frequency table, AFreq
        
        read one non-alphanumeric word, PW
        if AW $latex PW\not\in\sum_{P} $ then
          // continuing similarly from above
          // ..
      until end of input is reached
      
      