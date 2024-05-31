import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Data
Xs = np.array([0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5])
Ys = np.array([0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248])
N = 9

# Q-Q plot for X values
sm.qqplot(Xs, line='s')
plt.title("X distribution")
plt.show()

# Q-Q plot for Y values
sm.qqplot(Ys, line='s')
plt.title("Y distribution")
plt.show()

# Calculating and printing correlation coefficient
correlation_coefficient = np.corrcoef(Xs, Ys)[0, 1]
print(f"Correlation coefficient (r) between X and Y: {correlation_coefficient:.2f}")
