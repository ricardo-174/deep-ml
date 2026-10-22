import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	tra = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	disc = tra * tra - 4 * det
	x1 = (tra + math.sqrt(disc))/2
	x2 = (tra - math.sqrt(disc))/2
	return [x1,x2]