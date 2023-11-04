import numpy as np

def split_matrix(matrix):
    """Разбивает матрицу на 4 подматрицы."""
    rows, cols = matrix.shape
    half = rows // 2
    return (
        matrix[:half, :half], matrix[:half, half:],
        matrix[half:, :half], matrix[half:, half:]
    )

def strassen_multiply(A, B):
    global oper_add
    global oper_mult

    if A.shape[0] <= 64:  # Размер матрицы, при котором используется обычное умножение
        C = np.dot(A, B)
        oper_mult += A.shape[0] * A.shape[1]
    else:
        # Разбиваем матрицы A и B на подматрицы
        A11, A12, A21, A22 = split_matrix(A)
        B11, B12, B21, B22 = split_matrix(B)

        # Вычисляем 7 промежуточных матриц и подсчитываем операции умножения
        M1 = strassen_multiply((A11 + A22), (B11 + B22))
        M2 = strassen_multiply((A21 + A22), B11)
        M3 = strassen_multiply(A11, (B12 - B22))
        M4 = strassen_multiply(A22, (B21 - B11))
        M5 = strassen_multiply((A11 + A12), B22)
        M6 = strassen_multiply((A21 - A11), (B11 + B12))
        M7 = strassen_multiply((A12 - A22), (B21 + B22))

        # Подсчет операций сложения и вычитания
        oper_add += 6 * (A.shape[0] // 2) * (A.shape[0] // 2)

        # Вычисляем элементы результирующей матрицы C
        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        # Объединяем 4 подматрицы в результирующую матрицу
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C

n = 100
# Создание матрицы A
A = np.zeros((n, n))
for i in range(100):
    for j in range(100):
        A[i][j] = (-1) ** j

# Создание матрицы B
B = np.zeros((n, n))
for i in range(100):
    for j in range(100):
        B[i][j] = i + j

# Инициализация счетчиков операций
oper_add = 0
oper_mult = 0

# Умножение матриц A и B с использованием алгоритма Штрассена
C = strassen_multiply(A, B)

print("Результат:")
print(C)
print("Количество операций сложения:", oper_add)
print("Количество операций умножения:", oper_mult)
