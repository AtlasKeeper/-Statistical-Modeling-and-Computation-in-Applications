import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
Xs = np.array([0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5])
Ys = np.array([0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(Xs, Ys)

# Calculate predicted Y values
predicted_Ys = slope * Xs + intercept

# Calculate residuals
residuals = Ys - predicted_Ys

# Plot residuals
plt.scatter(Xs, residuals)
plt.axhline(y=0, color='r', linestyle='-')  # Add a horizontal line at y=0 for reference
plt.title('Residuals for Linear Regression')
plt.xlabel('Semi-major Axis (AU)')
plt.ylabel('Residuals (Observed - Predicted)')
plt.grid(True)
plt.show()
