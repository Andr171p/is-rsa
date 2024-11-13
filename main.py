def create_magic_square(n):
    """ Функция для создания магического квадрата размера n x n, где n должно быть нечетным числом. """
    if n % 2 != 1 or n < 3:
        raise ValueError("Размер магического квадрата должен быть нечетным числом >= 3")

    magic_square = [[0 for _ in range(n)] for _ in range(n)]

    # Начальная позиция
    row, col = 0, n // 2

    for num in range(1, n**2 + 1):
        magic_square[row][col] = num

        new_row = (row - 1) % n
        new_col = (col + 1) % n

        if magic_square[new_row][new_col]:
            row = (row + 1) % n
        else:
            row, col = new_row, new_col

    return magic_square

# Пример использования
if __name__ == "__main__":
    n = 3  # Размер магического квадрата
    square = create_magic_square(n)

    for row in square:
        print(row)