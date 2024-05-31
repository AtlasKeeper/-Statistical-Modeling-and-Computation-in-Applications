import numpy as np
import matplotlib.pyplot as plt

# Data provided
Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, 
               0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, 
               1.72, 2.03, 2.02, 2.02, 2.02])
Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 
               320.0, 373.0, 93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 
               608.0, 1040.0, 1100.0, 840.0, 801.0, 519.0])

N = 24

# Calculate the sample mean
mean_X = np.mean(Xs)
mean_Y = np.mean(Ys)

# Print the sample mean to three significant figures
print(f"X̄ = {mean_X:.3f} Mpc")
print(f"Ȳ = {mean_Y:.3f} km/s")

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(Xs, Ys, color='blue', label='Galaxies')
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.title("Hubble's Data: Galaxy Velocity vs. Distance")
plt.xlabel("Distance (Mpc)")
plt.ylabel("Velocity (km/s)")
plt.legend()
plt.grid(True)
plt.show()

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(Xs, Ys)[0, 1]

# Print the correlation coefficient
print(f"Correlation Coefficient: {correlation_coefficient:.3f}")
