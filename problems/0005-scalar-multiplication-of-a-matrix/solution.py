def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	if len(matrix) == 0:
		return []
	return [[matrix[j][i] * scalar for i in range(len(matrix[0]))] for j in range(len(matrix))]