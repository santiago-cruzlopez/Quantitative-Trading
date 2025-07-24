import numpy as np

inputs = [1.0, 2.0, 3.0,2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2.0
bias2 = 3.0
bias3 = 0.5

output1= [
        # Neuron 1:
        inputs[0] * weights1[0] +
        inputs[1] * weights1[1] +
        inputs[2] * weights1[2] +
        inputs[3] * weights1[3] + bias1,

        # Neuron 2:
        inputs[0] * weights2[0] +
        inputs[1] * weights2[1] +
        inputs[2] * weights2[2] +
        inputs[3] * weights2[3] + bias2,

        # Neuron 3:
        inputs[0] * weights3[0] +
        inputs[1] * weights3[1] +
        inputs[2] * weights3[2] +
        inputs[3] * weights3[3] + bias3]
          

print(output1)

# Using Loops for multiple neurons
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]
layers_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_ouput = 0.0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_ouput += n_input * weight
    neuron_ouput += neuron_bias
    layers_outputs.append(neuron_ouput)

print(layers_outputs)


# Using numpy for One Neuron
output2 = np.dot(weights1, inputs) + bias1
print(output2)

a = [1, 2, 3]
b = [2, 3, 4]

dot_product = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
print(dot_product)