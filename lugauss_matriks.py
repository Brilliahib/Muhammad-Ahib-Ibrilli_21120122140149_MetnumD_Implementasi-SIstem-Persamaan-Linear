import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        L[j, j] = 1

        for i in range(j+1):
            s1 = sum(U[k, j] * L[i, k] for k in range(i))
            U[i, j] = A[i, j] - s1

        for i in range(j, n):
            s2 = sum(U[k, j] * L[i, k] for k in range(j))
            L[i, j] = (A[i, j] - s2) / U[j, j]

    return L, U

# Contoh penggunaan
A = np.array([[2, -1, 1], [-1, 3, -1], [1, -1, 2]])

L, U = lu_decomposition(A)
print("L:")
print(L)
print("U:")
print(U)
