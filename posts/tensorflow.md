Categories: tensorflow
Tags: basics
	  tensorflow
	  python

# Tensorflow

All the notes on this page are based on Tensorflow 1.4.

# Imports

    import tensorflow as tf
    import numpy as np


# Running

## One Off

    y = tf.where(...)
    sess = tf.Session()
    outs = sess.run(y)
    sess.close()
    
    print "out=%s" % outs

## Iterative

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        y = sess.run(out)



# Useful primitives

## `where`

### Example

    x = np.linspace(-1, 1, 5)
    cond = tf.less(x, tf.zeros(tf.shape(x), dtype=x.dtype))
    y = tf.where(cond, tf.zeros(tf.shape(x)), tf.ones(tf.shape(x)))


`x` is a row of 5 elements.
`cond` generates a row of `bool`'s where each element contains:

    cond[i] = 0 iff x[i] < 0
            = 1 iff x[i] > 0

`y` contains a row of `int`'s where each element contains:

    y[i] = 0 iff cond[i] = True
         = 1 iff cond[i] = False

