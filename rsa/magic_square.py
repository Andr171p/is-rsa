import math
from typing import List, Dict, Tuple, Optional


class MagicSquare:
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
        for row in magic_square:
            print(row)
        return magic_square


def get_shape(text: str) -> int:
    text = text.replace(' ', '')
    length = len(text)
    if length < 9:
        return 3
    sqrt_length = math.isqrt(length)
    if length % sqrt_length != 0 or sqrt_length % 2 == 0:
        shape = sqrt_length + 1 if sqrt_length % 2 == 0 else sqrt_length + 2
    else:
        shape = sqrt_length
    return shape


class MagicEncryption:
    @staticmethod
    def create_magic_square(text: str) -> List[List[Optional[int]]]:
        shape = get_shape(text=text)
        magic_square = MagicSquare(shape=shape)
        return magic_square.create_magic_square()

    @classmethod
    def encrypt(cls, text: str) -> str:
        magic_square = cls.create_magic_square(text=text)
        chars = list(text)
        positions: Dict[int, Tuple[int, int]] = {}
        for i, row in enumerate(magic_square):
            for j, item in enumerate(magic_square[i]):
                positions[magic_square[i][j]] = (i, j)
        for index, char in enumerate(chars):
            if index + 1 in positions:
                row, col = positions[index + 1]
                magic_square[row][col] = char
        encrypted_text = ''.join([
            ' ' if isinstance(item, int) else item
            for row in magic_square
            for item in row
        ])
        return encrypted_text

    @classmethod
    def decrypt(cls, text: str) -> str:
        magic_square = cls.create_magic_square(text=text)
        decrypted_chars: List[Optional[str]] = [None for _ in range(len(text))]
        positions: List[int] = []
        for i, row in enumerate(magic_square):
            for j, item in enumerate(magic_square[i]):
                positions.append(magic_square[i][j])
        for index, char in enumerate(text):
            decrypted_chars[positions[index] - 1] = char
        decrypted_text = ''.join(decrypted_chars)
        return decrypted_text


def main() -> None:
    text = input("Введите текст: ")
    magic_encryption = MagicEncryption()
    encrypted = magic_encryption.encrypt(text=text)
    print(f"Зашифрованный текст: {encrypted}")
    decrypted = magic_encryption.decrypt(text=encrypted)
    print(f"Разшифрованный текст: {decrypted}")


if __name__ == "__main__":
    main()
