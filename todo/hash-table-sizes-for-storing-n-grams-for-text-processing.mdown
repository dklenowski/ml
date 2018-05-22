Categories: natural language
Tags: hash
      table
      hashcode

### Reference ###

Hash Table Sizes for Storing N-Grams for Text Processing. Zhong Gu and Daniel Berleant,, Technical Report 10-00a Oct 2000, Software Research Lab, Iowa State University.

### Notes ###

- Hash tables for 5 grams (5 characters).
- Convert each 5-gram to an equivalent 5 byte integer $latex i $ from $latex 0-(2^{40}-1) $.
- Each 5-gram consists of:

        $latex a_{0},a_{1},a_{2},a_{3},a_{4} $

  - where $latex num(a\_{n}) $ is the 1 byte integer equivalent of the character $latex a\_{n} $.

- The following formula is used to generate $latex i $.

        $latex i=num(a_{0})+256*num(a_{1})+256^{2}*num(a_{2})+256^{3}*num(a_{3})+256^{4}*num(a_{4}) $

- The resultant hashcode is generated using:

        $latex h(i)=i\%t $

  - where $latex t $ is the tablesize and is a prime number.

### Conclusions ###

- Provides a recommendation for tablesize's.
  - Sizes greater than $latex 2^{26} $.

