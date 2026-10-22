def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'row':
        return [sum(row) / len(row) for row in matrix]
    if mode == 'column':
        return [sum(col) / len(col) for col in zip(*matrix)]
    raise ValueError("mode must be 'row' or 'column'")
