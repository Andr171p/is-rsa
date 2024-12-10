n = int(input())

# Создаем массив
matrix = [0] * (n * n + 1)

# Генерируем магический квадрат
half_n = n // 2
mark = 1
middle = n // 2
upper = n * n + 1
half = n * n // 2

# Ставим метки в первой половине массива
for k in range(1, half_n + 1):
    for j in range(1, half_n + 1):
        matrix[middle - j + 1] = mark
        matrix[middle + j] = mark
        mark = -mark

    # Переходим к следующей строке
    middle += n
    mark = -mark

# Расставляем числа
for i in range(1, half + 1):
    # Будущая координата числа i
    l = i
    if matrix[i] < 0:
        l = upper - i

    matrix[l] = i
    matrix[upper - l] = upper - i
print(matrix)