import numpy as np
def solve_jacobi(A: list[list[float]], b: list[float], n: int) -> list[float]:
    N = len(b)
    x = [0.0] * N
    for _ in range(n):
        x = [
            (b[i] - sum(A[i][j] * x[j] for j in range(N) if j != i)) / A[i][i]
            for i in range(N)
        ]
    return [round(v, 4) for v in x]
    