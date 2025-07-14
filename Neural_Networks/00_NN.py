input = [1.0, 2.0, 3.0,2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output= (input[0] * weights[0] +
          input[1] * weights[1] +
          input[2] * weights[2] +
          input[3] * weights[3] +
          bias)

print(output)