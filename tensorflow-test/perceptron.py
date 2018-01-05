#!/usr/bin/python

import time
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

ct = 1

# Threshold Activation function
def threshold(x):
    """
    Simpliest activation function.

    :param x:
    :return:
    """
    global ct
    print "running iteration %d" % ct
    ct += 1

    cond = tf.less(x, tf.zeros(tf.shape(x), dtype=x.dtype))
    print "cond=%s" % cond
    out = tf.where(cond, tf.zeros(tf.shape(x)), tf.ones(tf.shape(x)))
    return out

# Plotting Threshold Activation Function
h = np.linspace(-1, 1, 5)  # array -1 to 1 in 50 increments
print "h=%s" % h

out = threshold(h)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    y = sess.run(out)
    plt.xlabel('Activity of Neuron')
    plt.ylabel('Output of Neuron')
    plt.title('Threshold Activation Function')
    plt.plot(h, y)
    plt.show()
    print "h=%s" % h
    print "y=%s" % y

