import numpy as np

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def scalar_multiply(matrix, scalar):
    return np.multiply(matrix, scalar)

def matrix_multiply(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        return "Error: Number of columns in matrix A must be equal to the number of rows in matrix B for multiplication."
    return np.matmul(matrix1, matrix2)

def matrix_inverse(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return "Error: Matrix is not square, inverse does not exist."
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "Error: Matrix is singular, inverse does not exist."

def matrix_determinant(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return "Error: Matrix is not square, determinant does not exist."
    return np.linalg.det(matrix)

def matrix_power(matrix, power):
    return np.linalg.matrix_power(matrix, power)

def main():
    matrix_a = None
    matrix_b = None
  
    print("Welcome to Juanita's Matrix Calculaor <333")
    

    while True:
        if matrix_a is None:
            rows_a = int(input("Enter the number of rows for matrix A: "))
            cols_a = int(input("Enter the number of columns for matrix A: "))
            matrix_a = np.array([[float(input(f"Enter value for matrix A at position ({i+1},{j+1}): ")) for j in range(cols_a)] for i in range(rows_a)])

        print("\nMatrix A:\n", matrix_a)

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Scalar Multiplication")
        print("4. Matrix Multiplication")
        print("5. Matrix Inverse")
        print("6. Matrix Determinant")
        print("7. Matrix Power")
        print("8. Reset Matrices")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 9:
            break
        elif choice in [1, 2, 4]:  # Addition, Subtraction, Matrix Multiplication
            if matrix_b is None:
                rows_b = int(input("Enter the number of rows for matrix B: "))
                cols_b = int(input("Enter the number of columns for matrix B: "))
                matrix_b = np.array([[float(input(f"Enter value for matrix B at position ({i+1},{j+1}): ")) for j in range(cols_b)] for i in range(rows_b)])

            if choice == 1:
                print("Addition:\n", add_matrices(matrix_a, matrix_b))
            elif choice == 2:
                print("Subtraction:\n", subtract_matrices(matrix_a, matrix_b))
            elif choice == 4:
                print("Matrix Multiplication:\n", matrix_multiply(matrix_a, matrix_b))
        elif choice == 3:
            scalar = float(input("Enter the scalar value: "))
            print("Scalar Multiplication:\n", scalar_multiply(matrix_a, scalar))
        elif choice == 5:
            print("Matrix A Inverse:\n", matrix_inverse(matrix_a))
        elif choice == 6:
            print("Matrix A Determinant:", matrix_determinant(matrix_a))
        elif choice == 7:
            power = int(input("Enter the power: "))
            print("Matrix A Raised to Power:\n", matrix_power(matrix_a, power))
        elif choice == 8:
            matrix_a = None
            matrix_b = None
        else:
            print("Invalid choice. Please try again.")

main()
