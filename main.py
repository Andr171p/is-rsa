def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Нечетный порядок не поддерживается")

    magic_square = [[0 for _ in range(n)] for _ in range(n)]

    i, j = 0, n // 2

    for num in range(1, n ** 2 + 1):
        magic_square[i][j] = num

        next_i, next_j = (i - 1) % n, (j + 1) % n

        # Если следующая клетка занята, переходим вниз
        if magic_square[next_i][next_j]:
            i += 1
        else:
            i, j = next_i, next_j

    return magic_square


# Пример использования
n = 3
magic_square = generate_magic_square(n)

for row in magic_square:
    print(' '.join(map(str, row)))