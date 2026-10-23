def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	x,y = len(vectors),len(vectors[0])
	mean = [sum(k)/y for k in vectors]

	ave = [[x-m for x in f]for f,m in zip(vectors,mean)]

	return [ 
		[
			sum(ave[i][k] * ave[j][k] for k in range(y))/(y-1) for i in range(x)
		] for j in range(x)
		]