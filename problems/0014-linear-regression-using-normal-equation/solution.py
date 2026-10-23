import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	x = np.array(X,dtype = float)
	y = np.array(y,dtype = float)
	w = np.linalg.inv(x.T @ x) @ x.T @ y 
	return [round(float(v), 4) for v in w]