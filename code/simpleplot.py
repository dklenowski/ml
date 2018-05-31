import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Threshold Activation function
def threshold(x):
    cond = tf.less(x, tf.zeros(tf.shape(x), dtype=x.dtype))
    return tf.where(cond, tf.zeros(tf.shape(x)), tf.ones(tf.shape(x)))

# Plotting Threshold Activation Function
h = np.linspace(-1, 1, 100)  # array -1 to 1 in 100 increments
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


