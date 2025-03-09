'''
Backpropagation is the neural network training process of feeding 
error rates back through a neural network to make it more accurate.

Sources: 
https://www.geeksforgeeks.org/backpropagation-in-neural-network/
https://iamtrask.github.io/2015/07/12/basic-python-network/
http://neuralnetworksanddeeplearning.com/chap2.html
'''

import numpy as np

# Sigmoid Function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# Input Dataset
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])

# Output Dataset
y = np.array([[0,0,1,1]]).T

# Random Numbers for Calculation
np.random.seed(1)

# Initialize Weights Randomly with Mean 0 || First layer of weights, Synapse 0, connecting l0 to l1.
syn0 = 2*np.random.random((3,1)) - 1

for iter in range(10000):
    # Forward Propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # Error, how much did we miss?
    l1_error = y - l1

    # Multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # Update Weights
    syn0 += np.dot(l0.T,l1_delta)

print("Output After Training: ")
print(l1)
