Categories: java
Tags: int
      hashcode

The code below generates a hashCode for 2 `int`'s (`i` and `j`). The implementation is based on `org.apache.commons.collections.map.MultiKeyMap#hash(Object key1, Object key2)` with a slight modification where `j` is multiplied by `31` to prevent duplicates for negative numbers.

``` java
  // modification to MultiKeyMap.java#hash in that j is multiplied by 31 which
  // prevents duplicated hashCodes for i=0,j=-1 and i=-1,j=0
  public int hashCode() {
    int h = 0;
    h ^= i;
    h ^= j*31;

    h += ~(h << 9);
    h ^=  (h >>> 14);
    h +=  (h << 4);
    h ^=  (h >>> 10);

    return h;
  }
```