Categories: java
Tags: int
      pack

Note you need to use a mask for the `right` `int` because when an `int` is converted to a `long` it is converted two's complement (i.e. inversion of bits and adding of 1).

```java
    public static final long mask = -1L >>> 32;

    public static long pack(int left, int right) {
      long l = ((long)left << 32) | ((long)right & mask);
      return l;
    }
  
    public static int left(long l) {
      int i = (int)(l >> 32);
      return i;
    }
  
    public static int right(long l) {
      int i = (int)(l & mask);
      return i;
    }
```


