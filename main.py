from typing import List, Optional


class MagicSquare:
    def __init__(self, shape: int) -> None:
        self.shape = shape
        self._square: List[List[Optional[int]]] = [
            [None for _ in range(self.shape)]
            for _ in range(self.shape)
        ]

    def calculate_sums(self):
        ...

    def __repr__(self) -> str:
        rows = []
        for row in self._square:
            rows.append(f"{row}\n")
        return "".join(rows)


def calculate_row_sum(matrix: List[List[int]], index: int = 0) -> int:
    return sum(matrix[index])


def calculate_column_sum(matrix: List[List[int]], index: int = 0) -> int:
    return sum([row[index] for row in matrix])


def calculate_main_diag_sum(matrix: List[List[int]]) -> int:
    return sum([matrix[index][index] for index in range(len(matrix))])


def calculate_side_diag_sum(matrix: List[List[int]]) -> int:
    shape = len(matrix)
    summ = 0
    for num in range(shape):
        summ += matrix[0 + num][shape - num]
        print(f"index: {summ}")
    return summ


m = [
    [1, 2, 7],
    [2, 4, 3],
    [9, 5, 8]
]
print(calculate_row_sum(m, index=0))
print(calculate_column_sum(m, index=1))
print(calculate_main_diag_sum(m))
print(calculate_side_diag_sum(m))