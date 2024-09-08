import numpy as np  # type: ignore

def strassen_matrix_multiplication(A, B):
    # Base case when matrix size is 1x1
    if len(A) == 1:
        return A * B

    # Splitting the matrices into quadrants
    mid = len(A) // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Calculating the 7 products using Strassen's formulas
    M1 = strassen_matrix_multiplication(A11 + A22, B11 + B22)
    M2 = strassen_matrix_multiplication(A21 + A22, B11)
    M3 = strassen_matrix_multiplication(A11, B12 - B22)
    M4 = strassen_matrix_multiplication(A22, B21 - B11)
    M5 = strassen_matrix_multiplication(A11 + A12, B22)
    M6 = strassen_matrix_multiplication(A21 - A11, B11 + B12)
    M7 = strassen_matrix_multiplication(A12 - A22, B21 + B22)

    # Combining the 7 products to get the result
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combining the quadrants into a single matrix
    C = np.zeros((len(A), len(A)), dtype=A.dtype)
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

def main():
    # Input matrices from the user
    n = int(input("Enter the size of the matrices (n x n, must be a power of 2): "))
    
    print("Enter matrix A (row by row):")
    A = np.array([list(map(int, input().split())) for _ in range(n)])

    print("Enter matrix B (row by row):")
    B = np.array([list(map(int, input().split())) for _ in range(n)])
    
    # Perform Strassen's multiplication
    C = strassen_matrix_multiplication(A, B)

    # Display the result
    print("Result of Strassen Matrix Multiplication:")
    print(C)

if __name__ == "__main__":
    main()
