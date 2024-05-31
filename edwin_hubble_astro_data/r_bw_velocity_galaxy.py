import numpy as np

# Data provided
Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, 
               0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, 
               1.72, 2.03, 2.02, 2.02, 2.02])
Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 
               320.0, 373.0, 93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 
               608.0, 1040.0, 1100.0, 840.0, 801.0, 519.0])

# Calculate the sample mean
mean_X = np.mean(Xs)
mean_Y = np.mean(Ys)

# Calculate the sample covariance and variances
cov_XY = np.sum((Xs - mean_X) * (Ys - mean_Y)) / (len(Xs) - 1)
var_X = np.var(Xs, ddof=1)
var_Y = np.var(Ys, ddof=1)

# Calculate the correlation coefficient
corr_coefficient = cov_XY / np.sqrt(var_X * var_Y)

# Calculate the slope of the linear model (maximum possible value of β^1)
max_beta_1 = corr_coefficient * np.sqrt(var_Y) / np.sqrt(var_X)

print(f"The maximum possible value of beta^1 is: {max_beta_1:.3f}")
