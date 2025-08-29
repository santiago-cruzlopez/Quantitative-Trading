# Perceptron Learning Algorithm Implementation
# This code implements a single-layer perceptron to learn the AND logic gate.

import numpy as np
import time

def activation_function(x):
    return 1 if x >= 0 else 0

def train_perceptron(X, y, epochs=100, learning_rate=0.1):
    """
    Train a single-layer perceptron using the perceptron learning rule.
    
    Args:
    - X: Input features (2D NumPy array, rows=samples, columns=features).
    - y: Target labels (1D NumPy array).
    - epochs: Maximum training iterations.
    - learning_rate: Step size for weight updates.
    
    Returns:
    - weights: Trained weights.
    - bias: Trained bias.
    """

    n_caracteristics = X.shape[1]
    weights = np.zeros(n_caracteristics)
    bias = 0

    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}")
        weight_updates = False

        for i in range(X.shape[0]):
            z = np.dot(weights, X[i]) + bias
            y_pred = activation_function(z)
            error = y[i] - y_pred

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

def predict(input_1, input_2, weights, bias):
    """Predict output for two inputs using trained weights and bias."""
    X_input = np.array([input_1, input_2])
    z = np.dot(weights, X_input) + bias
    return activation_function(z)

# Train the perceptron
weights_trained, bias_trained = train_perceptron(X, y)

# Print trained parameters
print(f"Trained weights: {weights_trained}")
print(f"Trained bias: {bias_trained}")

# Predict for all possible inputs
print("\nPredictions for all possible inputs:")
for sample in X:
    pred = predict(sample[0], sample[1], weights_trained, bias_trained)
    print(f"Inputs {sample}: Prediction {pred}")

# User input with validation
print("\nInteractive Prediction:")
while True:
    try:
        input_1_val = int(input("Enter first input (0 or 1): "))
        input_2_val = int(input("Enter second input (0 or 1): "))
        if input_1_val not in [0, 1] or input_2_val not in [0, 1]:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter 0 or 1.")

pred = predict(input_1_val, input_2_val, weights_trained, bias_trained)
print(f"Prediction for inputs ({input_1_val}, {input_2_val}): {pred}")