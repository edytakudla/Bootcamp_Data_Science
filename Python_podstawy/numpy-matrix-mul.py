import numpy as np

def matrix_multiplication(A, B):
    """
    >>> import numpy as np

    >>> A = np.array([[1, 0], [0, 1]])
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    [[4, 1], [2, 2]]

    >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
    >>> B = np.matrix([[4,1], [2,2], [5,1], [2,3]])
    >>> matrix_multiplication(A, B)
    [[9, 2], [7, 3], [21, 8], [28, 8]]
    """

    A = np.matrix(A)
    B = np.matrix(B)
    print((A * B).tolist())
    print((A @ B).tolist())

    return(A * B).tolist()


A = np.array([[1, 0], [0, 1]])
B = [[4, 1], [2, 2]]
matrix_multiplication(A, B)

A = [[1, 0, 1, 0], [0, 1, 1, 0], [3, 2, 1, 0], [4, 1, 2, 0]]
B = np.matrix([[4, 1], [2, 2], [5, 1], [2, 3]])
matrix_multiplication(A, B)


# liczby losowe z przedzialu 10 do 100
A = np.random.randint(low=10, high=100, size=(16,16)).astype(float)
print('Matrix:')
print(A)

B = A.transpose()
print('Transposed:')
print(B)

inner = B[6:10, 6:10]
print('Inner:')
print(inner)

total = inner.sum()
print(f'Sum: {total}')