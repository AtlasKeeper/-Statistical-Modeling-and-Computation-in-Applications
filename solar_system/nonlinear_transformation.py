import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Original data
Xs = np.array([0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5])
Ys = np.array([0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248])

# Transformations
transformations = {
    "None, X'=X and Y'=Y": (Xs, Ys),
    "X'=X and Y'=ln(Y)": (Xs, np.log(Ys)),
    "X'=ln(X) and Y'=Y": (np.log(Xs), Ys),
    "X'=ln(X) and Y'=ln(Y)": (np.log(Xs), np.log(Ys)),
    "X'=X and Y'=Y^2": (Xs, Ys**2)
}

# Perform linear regression and calculate R^2 for each transformation
best_r2 = -np.inf
best_transformation = None
for name, (X_trans, Y_trans) in transformations.items():
    X_trans = X_trans.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X_trans, Y_trans)
    Y_pred = model.predict(X_trans)
    r2 = r2_score(Y_trans, Y_pred)
    print(f"{name}: R^2 = {r2:.4f}")
    
    if r2 > best_r2:
        best_r2 = r2
        best_transformation = name

print(f"\nBest transformation: {best_transformation} with R^2 = {best_r2:.4f}")

# Plot the best fit
X_trans, Y_trans = transformations[best_transformation]
X_trans = X_trans.reshape(-1, 1)
model = LinearRegression()
model.fit(X_trans, Y_trans)
Y_pred = model.predict(X_trans)

plt.scatter(X_trans, Y_trans, color='blue', label='Data')
plt.plot(X_trans, Y_pred, color='red', label='Best Fit Line')
plt.xlabel('Transformed X')
plt.ylabel('Transformed Y')
plt.title(f'Best Transformation: {best_transformation}')
plt.legend()
plt.show()
