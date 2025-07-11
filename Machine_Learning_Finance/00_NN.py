import numpy as np
import time

def activation_function(x):
    return 1 if x >= 0 else 0

def training_neuron(X, y, epochs=100,
                    learning_rate=0.1):
    n_caracteristics = X.shape[1]
    weights = np.zeros(n_caracteristics)
    bias = 0

    for ep in range(epochs):
        print(f"Epoch {ep}")
        weight_updates = False

        for i in range(X.shape[0]):
            z = np.dot(weights, X[i]) + bias
            y_predicted = activation_function(z)
            error = y[i] - y_predicted

            if error != 0:
                weights += learning_rate * error * X[i]
                bias += learning_rate * error
                weight_updates = True

            time.sleep(0.2)  # Simulate time delay for each update

        if not weight_updates:
            print("Convergence reached.")
            break

    return weights, bias

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 0, 0, 1])

def prediction(input_1, input_2, weights, bias):
    X_input = np.array([input_1, input_2])
    z = np.dot(weights, [input_1, input_2]) + bias
    return activation_function(z)

# Train the Neuron
weights_trained, bias_trained = training_neuron(X, y)

# Make Predictions
print("Predictions:")
input_1_val = int(input("Enter First input (0 or 1): "))
input_2_val = int(input("Enter Second input (0 or 1): "))1
pred = prediction(input_1_val, input_2_val, weights_trained, bias_trained)
print(f"Prediction for inputs ({input_1_val}, {input_2_val}): {pred}")