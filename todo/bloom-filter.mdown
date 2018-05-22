Categories: algorithms
Tags: algorithm
      bloom
      hash

## References

[1] Hadoop In Action, Chuck Lam, Manning 2011.


## Introduction

- False Positive (error rate, `c`) rate approximated by:

      $latex c=(1-e^{(-kn/m)})\, k $
      
      k - number of hash functions used.
      m - number of bits for the bloom filter.
      n - number of elements added to bloom filter.

- `m` and `n` determined by system, therefore choose `k` to reduce false positive rate, i.e.

      $latex k=ln(2)({\displaystyle \frac{m}{n}})\thickapprox0.7({\displaystyle \frac{m}{n}}) $

- if `m` not known, but the error rate `c` is known, use:

      $latex m={\displaystyle \frac{-kn}{ln(1-c^{1/k})}} $


## Algorithm

### Notes

- Bloom filter represented by a bit array of size `m`.
- Have `k` independent hash functions, where each hash function takes an input and outputs an integer between `0` and `m-1`.
- When we add an element to the bloom filter, use the hash functions to generate `k` indexes into the bit array and set the `k` bits to 1.
- Note that a bit will be set to `1` regardless of its previous state.
- Has no *false negatives* (i.e. if `contains` returns true, Bloom Filter definitely does not contain the object).
- Possibility of *false positives*.

### Implementation

- All implementation notes based on the Hadoop implementation of Bloom Filters

        org.apache.hadoop.hbase.util

        BloomFilter <Interface>   -> ByteBloomFilter          <- Hash     <- JenkinsHash
                                            |                             <- MurmarHash
                                            \/
                                  -> DynamicByteBloomFilter


#### `add()`

- [ByteBloomFilter.java](http://svn.apache.org/repos/asf/hbase/trunk/src/main/java/org/apache/hadoop/hbase/util/ByteBloomFilter.java)

        @Override
        public void add(byte [] buf, int offset, int len) {
          /*
           * For faster hashing, use combinatorial generation
           * http://www.eecs.harvard.edu/~kirsch/pubs/bbbf/esa06.pdf
           */
          int hash1 = this.hash.hash(buf, offset, len, 0);
          int hash2 = this.hash.hash(buf, offset, len, hash1);
        
          for (int i = 0; i < this.hashCount; i++) {
            long hashLoc = Math.abs((hash1 + i * hash2) % (this.byteSize * 8));
            set(hashLoc);
          }
        
          ++this.keyCount;
        }

##### Notes

- Uses the same hash function to set all bits in bloom filter.

#### `contains()`

- [ByteBloomFilter.java](http://svn.apache.org/repos/asf/hbase/trunk/src/main/java/org/apache/hadoop/hbase/util/ByteBloomFilter.java)

        @Override
        public boolean contains(byte [] buf, int offset, int length,
            ByteBuffer theBloom) {
        
          if(theBloom.limit() != this.byteSize) {
            throw new IllegalArgumentException("Bloom does not match expected size");
          }
        
          int hash1 = this.hash.hash(buf, offset, length, 0);
          int hash2 = this.hash.hash(buf, offset, length, hash1);
        
          for (int i = 0; i < this.hashCount; i++) {
            long hashLoc = Math.abs((hash1 + i * hash2) % (this.byteSize * 8));
            if (!get(hashLoc, theBloom) ) {
              return false;
            }
          }
          return true;
        }