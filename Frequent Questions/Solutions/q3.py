def q3(matrix: list[list[int]]) -> int:
    total_sum = 0
    for idx in range(len(matrix)):
        total_sum += matrix[idx][idx]
    return total_sum


print(q3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
