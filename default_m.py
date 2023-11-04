import numpy as np

n = 100

A = np.zeros((n, n))
for i in range(100):
    for j in range(100):
        A[i][j] = (-1) ** j

# Создание матрицы B
B = np.zeros((n, n))
for i in range(100):
    for j in range(100):
        B[i][j] = i + j

# Инициализация матрицы C
C = np.zeros((n, n))

# Инициализация счетчиков операций
oper_add = 0
oper_mult = 0

# Умножение матриц A и B и подсчет операций
for i in range(100):
    for j in range(100):
        for k in range(100):
            C[i][j] += A[i][k] * B[k][j]
            oper_add += 1  # Увеличиваем счетчик операций сложения
            oper_mult += 1  # Увеличиваем счетчик операций умножения

print("Результат:")
print(C)
print("Количество операций сложения:", oper_add)
print("Количество операций умножения:", oper_mult)
