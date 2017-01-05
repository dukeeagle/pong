import tensorflow as tf
import cv2
import pong
import numpy as np
import random
from collections deque #data structure

#5-layer convolutional neural network that feeds from image data - learns from deep reinforcement
#defining hyperparameters
ACTIONS = 3 #up, down, or stay
#learning rate
GAMMA = 0.99
#update gradient to reach this area
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05
#how many frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000
#batch size (how many times we train)
BATCH SIZE = 100

#create tf graph
def createGraph():

    #first convolutional layer and bias vector
    #tf.zeros creates empty tensor full of zeros with a given shape
    W_conv1 = tf.Variable(tf.zeros([8, 8, 4, 32]))
    b_conv1 = tf.Variable(tf.zeros([32])) #32 bits

    #second layer
    W_conv2 = tf.Variable(tf.zeros([4, 4, 32, 64]))
    b_conv2 = tf.Variable(tf.zeros([64])) #64 bits

    #third layer
    W_conv3 = tf.Variable(tf.zeros([3, 3, 64, 64]))
    b_conv3 = tf.Variable(tf.zeros([64])) #64 bits

    #fourth layer
    W_fc4 = tf.Variable(tf.zeros([3136, 784]))
    b_fc4 = tf.Variable(tf.zeros([784]))

    #last layer
    W_fc5 = tf.Variable(tf.zeros([784, ACTIONS]))
    b_fc5 = tf.Variable(tf.zeros([ACTIONS]))

    #input for pixel data
    s = tf.placeholder("float", [None, 84, 84, 84])

    #compute RELU activation function on 2d convolutions given 4d inputs and filter tensors (in other words, perform calculations on each layer)

    conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides[1, 4, 4, 1], padding = "VALID") + b_conv1)
    conv3 = tf.nn.relu(tf.nn.conv2d(s, W_conv3, strides[1, 2, 2, 1], padding = "VALID") + b_conv2)
    conv2 = tf.nn.relu(tf.nn.conv2d(s, W_conv2, strides[1, 1, 1, 1], padding = "VALID") + b_conv3)

    conv3_flat =
