import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Given data
Xs = np.array([0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5])
Ys = np.array([0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248])

# Calculate correlation coefficient
corr_coefficient, _ = pearsonr(Xs, Ys)

# Plot the data
plt.scatter(Xs, Ys)
plt.title('Orbital Period vs. Semi-major Axis')
plt.xlabel('Semi-major Axis (AU)')
plt.ylabel('Orbital Period (Earth years)')
plt.grid(True)
plt.show()

print(f"The correlation coefficient (rX,Y) is approximately: {corr_coefficient:.2f}")
