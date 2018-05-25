#!/usr/bin/python

import time
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Hyper parameters
eta = 0.4  # learning rate parameter
epsilon = 1e-03 # minimum accepted error
max_epochs = 100 # Maximum Epochs

# Training Data  Y = AB + BC, sum of two linear functions.
T, F = 1., 0.
X_in = [
    [T, T, T, T],
    [T, T, F, T],
    [T, F, T, T],
    [T, F, F, T],
    [F, T, T, T],
    [F, T, F, T],
    [F, F, T, T],
    [F, F, F, T],
]
Y = [
    [T],
    [T],
    [F],
    [F],
    [T],
    [F],
    [F],
    [F]
]


# Threshold Activation function
def threshold(x):
    cond = tf.less(x, tf.zeros(tf.shape(x), dtype=x.dtype))
    out = tf.where(cond, tf.zeros(tf.shape(x)), tf.ones(tf.shape(x)))
    return out

W = tf.Variable(tf.random_normal([4, 1], stddev=2, seed=0)) # 4 x 1

h = tf.matmul(X_in, W)
Y_hat = threshold(h)
error = Y - Y_hat
mean_error = tf.reduce_mean(tf.square(error))
dW = eta * tf.matmul(X_in, error, transpose_a=True)
train = tf.assign(W, W+dW)

init = tf.global_variables_initializer()
err = 1
epoch = 0
with tf.Session() as sess:
    sess.run(init)
    while err > epsilon and epoch < max_epochs:
        epoch += 1
        err, _ = sess.run([mean_error, train])
        print "train=%s" % train.eval()
        print "dw=%s" % dW.eval()
        print "out=%s" % Y_hat.eval()
        print('epoch: {0}  mean error: {1}'.format(epoch, err))

    print('Training complete')

