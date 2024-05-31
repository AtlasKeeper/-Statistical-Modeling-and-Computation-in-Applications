import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Original data
Xs = np.array([0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5])
Ys = np.array([0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248])

# Transformations
log_Xs = np.log(Xs)
log_Ys = np.log(Ys)

# Perform linear regression on the transformed data
log_Xs = log_Xs.reshape(-1, 1)
model = LinearRegression()
model.fit(log_Xs, log_Ys)

# Get the slope (kappa) and intercept (ln(omega))
kappa = model.coef_[0]
ln_omega = model.intercept_

# Round kappa to two significant figures
kappa_rounded = round(kappa, 2)

print(f"κ = {kappa_rounded}")
print(f"ln(ω) = {ln_omega}")

# Calculate omega from ln(omega)
omega = np.exp(ln_omega)
print(f"ω = {omega}")

# Plotting the original data and the nonlinear fit
X_fit = np.linspace(min(Xs), max(Xs), 100)
Y_fit = omega * X_fit**kappa_rounded

plt.scatter(Xs, Ys, color='blue', label='Data')
plt.plot(X_fit, Y_fit, color='red', label='Nonlinear Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Nonlinear Fit: Y = ωX^κ')
plt.legend()
plt.show()
