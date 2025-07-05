"""
Jul 03, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Dynamic Programming
ChainedMatrices
"""
class ChainedMatrices:
    def __init__(self, p):
        self.p = p
        self.n = len(p) - 1 #calculate the len of the vector p

        # Creation of the square matrices
        self.m = [[0 for _ in range(self.n+1)] for _ in range(self.n + 1)] # Since we are not using the first position add one more
        self.s = [[0 for _ in range(self.n+1)] for _ in range(self.n + 1)] # Since we are not using the first position add one more

        # A variable to print a nicer solution
        self.solution = ""

    def solve(self):
        for i in range(self.n):
            self.m[i][i] = 0 # We fill the diagonal with zeros

        for l in range(2, self.n + 1):
            for i in range(1, self.n - l + 2):
                j = i + l - 1
                self.m[i][j] = float('inf') # We establish the minimum value against which we are going to compare.
                for k in range(i, j):
                    q = self.m[i][k] + self.m[k+1][j] + self.p[i-1] * self.p[k] * self.p[j] # execution of the step 2, calculus of the optimus solution value
                    if q < self.m[i][j]: # We decide which value we want to keep and store it instead
                        self.m[i][j] = q
                        self.s[i][j] = k
        return self.m, self.s

    def print_optimal_parens(self, s, i, j):
        if i == j:
            self.solution += "A" + str(i) # instead of printing the value, we store each chunk to print all together at the end
        else:
            self.solution += "("
            self.print_optimal_parens(s, i, s[i][j])
            self.print_optimal_parens(s, s[i][j] + 1, j)
            self.solution += ")"

    def print_solution(self, i, j):
        print("Mínimo de multiplicaciones: ", self.m[i][j])
        self.print_optimal_parens(self.s, i,j)
        print(c.solution)

if __name__ == '__main__':
    # Example vector
    p_example=[30, 35, 15, 5, 10, 20, 25]

    # Homework vector
    p_homework=[5, 10, 3, 12, 5, 50, 6]

    c = ChainedMatrices(p_homework)
    c.solve()
    c.print_solution(1,6)


    """
    p_example:  [ (A1*(A2*A3)) * ((A4*A5)*A6) ]
    p_homework: [ (A1*A2) * ( (A3*A4) * (A5*A6) ) ]
    """
