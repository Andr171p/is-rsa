import math
from typing import List


class MagicSquare:
    def __init__(self, shape: int) -> None:
        self._shape = shape

    def _is_valid_shape(self) -> bool:
        if self._shape % 2 != 1 and self._shape < 3:
            raise ValueError("Размер магического квадарата должен быть нечётным числом >=3")
        return True

    def _create_zero_square(self) -> List[list[None]]:
        return [[None for _ in range(self._shape)] for _ in range(self._shape)]

    def create_magic_square(self) -> List[list]:
        assert self._is_valid_shape()
        magic_square: List[list] = self._create_zero_square()
        x, y = 0, self._shape // 2
        for num in range(1, self._shape ** 2 + 1):
            magic_square[x][y] = num
            new_x, new_y = (x - 1) % self._shape, (y + 1) % self._shape
            if magic_square[new_x][new_y]:
                x = (x + 1) % self._shape
            else:
                x, y = new_x, new_y
        return magic_square


class MagicEncryption:
    @staticmethod
    def _get_shape(text: str) -> int:
        text = text.replace(' ', '')
        length = len(text)
        if length % math.sqrt(length):
            shape = int(math.sqrt(length) + 1)
        else:
            shape = int(math.sqrt(length))
        return shape if shape >= 3 else shape + 1

    @classmethod
    def encrypt(cls, text: str) -> str:
        shape = cls._get_shape(text=text)
        magic_square = MagicSquare(shape=shape).create_magic_square()
        chars = list(text)
        positions = {}
        for i in range(len(magic_square)):
            for j in range(len(magic_square[i])):
                positions[magic_square[i][j]] = (i, j)
        for index, char in enumerate(chars):
            if index + 1 in positions:
                row, col = positions[index + 1]
                magic_square[row][col] = char
        return magic_square

    @classmethod
    def decrypt(cls, text: str) -> str:
        ...


print(MagicEncryption.encrypt(text='Магическая сила'))