from typing import List, Optional


class OddMagicSquare:
    def __init__(self, shape: int) -> None:
        self._shape = shape

    def _is_valid_shape(self) -> bool:
        if self._shape % 2 != 1 and self._shape < 3:
            raise ValueError("Размер магического квадарата должен быть нечётным числом >=3")
        return True

    def _create_empty_square(self) -> List[List[Optional[int]]]:
        return [[None for _ in range(self._shape)] for _ in range(self._shape)]

    def create_magic_square(self) -> List[List[int]]:
        assert self._is_valid_shape()
        magic_square: List[List[Optional[int]]] = self._create_empty_square()
        x, y = 0, self._shape // 2
        for num in range(1, self._shape ** 2 + 1):
            magic_square[x][y] = num
            new_x, new_y = (x - 1) % self._shape, (y + 1) % self._shape
            if magic_square[new_x][new_y]:
                x = (x + 1) % self._shape
            else:
                x, y = new_x, new_y
        return magic_square