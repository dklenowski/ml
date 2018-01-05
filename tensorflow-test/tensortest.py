import tensorflow as tf
import numpy as np


h = np.linspace(-1, 1, 10)
print "h=%s" % h
print "dtype=%s" % h.dtype
print "shape=%s" % tf.shape(h)


x = np.linspace(-1, 1, 5)
cond = tf.less(x, tf.zeros(tf.shape(x), dtype=x.dtype))
y = tf.where(cond, tf.zeros(tf.shape(x)), tf.ones(tf.shape(x)))


sess = tf.Session()
outs = sess.run(y)
sess.close()

print "x=%s" % x
print "y=%s" % outs
