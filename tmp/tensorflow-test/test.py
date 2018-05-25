
import time
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

W = tf.Variable(tf.random_normal([4, 1], stddev=2, seed=0))

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    y = sess.run(W)
    print "y=%s" % y
