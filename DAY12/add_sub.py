import numpy as np

matrix1 = np.array([[1,2,3],[24,5,6]])
matrix2 = np.array([[7,8,9],[10,8,15]])
matrix_add = np.add(matrix1,matrix2)
matrix_sub = np.subtract(matrix1,matrix2)
print("Addition of matrixes: ", matrix_add)
print("Subtraction of matrixes: ", matrix_sub)