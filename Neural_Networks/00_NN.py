input = [1.0, 2.0, 3.0,2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2.0
bias2 = 3.0
bias3 = 0.5

output= [
        # Neuron 1:
        input[0] * weights1[0] +
        input[1] * weights1[1] +
        input[2] * weights1[2] +
        input[3] * weights1[3] + bias1,

        # Neuron 2:
        input[0] * weights2[0] +
        input[1] * weights2[1] +
        input[2] * weights2[2] +
        input[3] * weights2[3] + bias2,

        # Neuron 3:
        input[0] * weights3[0] +
        input[1] * weights3[1] +
        input[2] * weights3[2] +
        input[3] * weights3[3] + bias3]
          
          
          
print(output)