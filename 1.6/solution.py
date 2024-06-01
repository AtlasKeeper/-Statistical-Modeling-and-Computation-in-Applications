import numpy as np
import pandas as pd

def gradient_descent(X, y, step_size, precision):
    n, m = X.shape
    beta = np.zeros(m)  # Initialize coefficients to zeros
    max_iterations = 1000  # Set a maximum number of iterations

    for _ in range(max_iterations):
        gradient = -2 * X.T @ (y - X @ beta) / n
        beta_new = beta - step_size * gradient

        # Check for convergence
        if np.linalg.norm(beta_new - beta) < precision:
            break

        beta = beta_new

    return beta

# Load synthetic data from syn_X.csv and syn_Y.csv
X = pd.read_csv("unzipped/syn_X.csv").values
y = pd.read_csv("unzipped/syn_Y.csv").values.flatten()

# Set hyperparameters
step_size = 0.01  # Try different values
precision = 1e-6

# Run gradient descent
optimal_beta = gradient_descent(X, y, step_size, precision)
print("Optimal coefficients (beta):", optimal_beta)
