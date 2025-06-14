"""
Jun 07, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Linear solution to Fibonacci sequence
using the matrix form

    | 1  1 | ^ n = | fn-1 fn   |
    | 1  0 |       | fn   fn+1 |
"""

def matrix_power( matrix, pow ):
    if pow < 0:
        raise Exception("Inverse matrix is not supported")

    # Identity matrix
    if pow == 0:
        return [[1,0], [0,1]]

    # The same matrix
    if pow == 1:
        return matrix

    # Initialize matrix positions
    x, y, z, w = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

    # Initialize result matrix
    m = matrix

    # Initialize result matrix positions
    x_1, y_1, z_1, w_1 = m[0][0], m[0][1], m[1][0], m[1][1]

    # Subtract one from pow due the operation within the for is matrix * matrix by itself
    for n in range(pow - 1):
        # Multiply and add rows and columns as linear algebra dictates
        m = [[x*x_1 + y*z_1, x*y_1 + y*w_1],  [z*x_1 + w*z_1,z*y_1 + w*w_1]]
        # then reconstruct the variables with the new matrix
        x_1, y_1, z_1, w_1 = m[0][0], m[0][1], m[1][0], m[1][1]

    return m

def fibo(n):
    # Fibonacci matrix
    matrix = [[1,1],[1,0]]

    # f(n) is on the [0][1] or [1][0] position and that is the desired numer
    return n if n < 2 else (matrix_power(matrix, n))[0][1]

if __name__ == '__main__':
    print( fibo(10) )