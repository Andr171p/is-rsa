from typing import List, Optional


class EvenMagicSquare:
    def __init__(self, shape: int) -> None:
        self._shape = shape
        if self._is_valid_shape():
            self._half_n = self._shape // 2
            self._mark = 1
            self._middle = self._shape // 2
            self._upper = self._shape ** 2 + 1
            self._half = self._shape ** 2 // 2

    def _is_valid_shape(self) -> bool:
        if self._shape % 2 or self._shape < 4:
            raise ValueError("Размер четного магического квадрата должен быть <4")
        return True

    def _create_empty_square(self) -> List[None]:
        return [None] * (self._shape ** 2 + 1)

    def _set_marks(self, square: List[Optional[int]]) -> List[Optional[int]]:
        for i in range(1, self._half_n + 1):
            for j in range(1, self._half_n + 1):
                square[self._middle - j + 1] = self._mark
                square[self._middle + j] = self._mark
                self._mark = -self._mark
            self._middle += self._shape
            self._mark = -self._mark
        return square

    def _fill_nums(self, square: List[Optional[int]]) -> List[Optional[int]]:
        for i in range(1, self._half + 1):
            l = i
            if square[i] < 0:
                l = self._upper - i

            square[l] = i
            square[self._upper - l] = self._upper - i
        return square

    def create_magic_square(self) -> List[List[int]]:
        square = self._create_empty_square()
        square = self._set_marks(square)
        square = self._fill_nums(square)
        square = square[1:]
        magic_square: List[List[int]] = []
        for i in range(self._shape):
            start_index = i * self._shape
            end_index = start_index + self._shape
            magic_square.append(square[start_index:end_index])
        return magic_square
