def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    if len(a) == 0 or len(b) == 0:
        return []
    return [[sum(a[i][j] * b[j][k] for j in range(len(a[0]))) for k in range(len(b[0])) ] for i in range(len(a))]