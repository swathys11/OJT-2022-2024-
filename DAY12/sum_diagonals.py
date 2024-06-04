import numpy as np 

#create 3x3 matrix
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
sum_diagonals1 = np.trace(matrix1)
print("Sum of matrix in 3x3: ",sum_diagonals1)

#create matrix 4x4
matrix2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
sum_diagonals2 = np.trace(matrix2)
print("Sum of diagonals of 4x4: ",sum_diagonals2)