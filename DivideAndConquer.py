"""
Jun 07, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Quick exponentiation using the formula

      |  (x^2)^(n/2)  For even exponent
x^n = |
      |  x * (x^2)^((n-1)/2) For odd exponent
"""
def divide_and_conquer(base, n):
    # Base-case: any number to the zero power is one
    if n == 0: return 1

    # From the formula x^2
    base2 = base * base

    # Even and Odd cases
    if n % 2 == 0 :
        # Even: (x^2)^(n/2) just call itself with square base and exponent divided by 2
        return divide_and_conquer(base2, n//2)
    else :
        # Odd: x * (x^2)^((n-1)/2) here we multiply the base by the result of the function itself and send exponent n-1/2
        return base * divide_and_conquer(base2, (n-1)//2)

if __name__ == '__main__':
    print( divide_and_conquer(10,2) )