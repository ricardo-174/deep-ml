import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	a,t,s = np.array(A),np.array(T),np.array(S)
	if abs(np.linalg.det(t)) < 1e-9 or abs(np.linalg.det(s)) < 1e-9:
		return -1
	return (np.linalg.inv(t) @ a @ s).tolist()