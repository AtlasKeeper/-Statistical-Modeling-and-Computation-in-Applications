import numpy as np
import matplotlib.pyplot as plt

# Data provided
Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, 
               0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, 
               1.72, 2.03, 2.02, 2.02, 2.02])
Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 
               320.0, 373.0, 93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 
               608.0, 1040.0, 1100.0, 840.0, 801.0, 519.0])

# Number of data points
N = 24

# Calculate the sample mean
mean_X = np.mean(Xs)
mean_Y = np.mean(Ys)

# Calculate the sample standard deviation (ddof=1 for sample standard deviation)
std_X = np.std(Xs, ddof=1)
std_Y = np.std(Ys, ddof=1)

# Calculate the sample covariance
cov_XY = np.sum((Xs - mean_X) * (Ys - mean_Y)) / (N - 1)

# Calculate the sample correlation coefficient
corr_XY = cov_XY / (std_X * std_Y)

# Print the sample correlation coefficient
print(f"Sample Correlation Coefficient (r_XY) = {corr_XY:.3f}")

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(Xs, Ys, color='blue', label='Galaxies')
plt.title("Hubble's Data: Galaxy Velocity vs. Distance")
plt.xlabel("Distance (Mpc)")
plt.ylabel("Velocity (km/s)")
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.grid(True)
plt.legend()
plt.show()
