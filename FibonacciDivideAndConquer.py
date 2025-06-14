"""
Jun 07, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Fibonacci sequence using Quick exponentiation formula to power the matrix

      |  (x^2)^(n/2)  For even exponent
x^n = |
      |  x * (x^2)^((n-1)/2) For odd exponent

In this case our base is a matrix
"""
def matrix_power( matrix, n ):
    if n < 0:
        raise Exception("Inverse matrix is not supported")

    # Identity matrix
    if n == 0:
        return [[1,0], [0,1]]

    # The same matrix
    if n == 1:
        return matrix

    # Initialize matrix positions
    x, y, z, w = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

    # Here we power the matrix to the power of 2 as the quick exponentiation formula
    m2 = [[x*x + y*z, x*y + y*w],  [z*x + w*z,z*y + w*w]]

    # Even and Odd cases from the quick exponentiation formula
    if n % 2 == 0:
        # Even: (m^2)^(n/2) just call itself with square matrix and exponent divided by 2
        return matrix_power(m2, n // 2)
    else :
        # Odd: matrix * (matrix^2)^((n-1)/2) here we multiply the matrix by the result of the function itself and send exponent n-1/2
        # m2 to the power of (n-1)/2
        mp = matrix_power(m2, (n - 1) // 2)
        # then multiply the result by the matrix in the input argument
        x_1, y_1, z_1, w_1 = mp[0][0], mp[0][1], mp[1][0], mp[1][1]
        return [[x*x_1 + y*z_1, x*y_1 + y*w_1],  [z*x_1 + w*z_1,z*y_1 + w*w_1]]

def fibo(n):
    # Fibonacci matrix
    matrix = [[1,1],[1,0]]

    # f(n) is on the [0][1] or [1][0] position and that is the desired numer
    return n if n < 2 else (matrix_power(matrix, n))[0][1]

if __name__ == "__main__":
    print( fibo(10) )