import numpy as np

def input_matriks_balikan():
    n = int(input("Masukkan ukuran matriks (n x n): "))
    print("Masukkan elemen matriks koefisien A:")
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i,j] = float(input(f"Masukkan elemen A[{i+1},{j+1}]: "))
    return A

def matriks_balikan(A=None):
    if A is None:
        A = input_matriks_balikan()
    try:
        A_inv = np.linalg.inv(A)
        return A_inv
    except np.linalg.LinAlgError:
        print("Matriks tidak dapat diinverskan.")
        return None

if __name__ == "__main__":
    A_inverse = matriks_balikan()
    if A_inverse is not None:
        print("\nInverse matriks:")
        print(A_inverse)
