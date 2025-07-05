"""
Jul 03, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Dynamic Programming
Cut the rope
"""
class CutTheRope:
    def __init__(self, prices, n):
        self.prices = prices
        self.max_price = 0
        self.r = [0] * (n + 1) # allocate zeros in the array
        self.s = [0] * (n + 1) # allocate zeros in the array
        self.n = n

    def solve(self):
        self.r[0] = 0 # start with zero
        self.s[0] = 0 # skip the first position

        for j in range(1, self.n + 1): # we add one to make range inclusive
            q = float('-inf') # initialize q with negative infinite to start from there
            for i in range(1, j + 1): # same here, we add one to make range inclusive
                max_value = self.prices[i - 1] + self.r[j - i] # As we use this value on validation and assigment, this calculus is in a separated line
                if q < max_value: # validate if there is a new maximum value
                    q = max_value # update q with the new maximum value
                    self.s[j] = i
            self.r[j] = q

        self.max_price = self.r[self.n] # store the max price to print as result

        return self.max_price # return the maximum prince

    def print_solution(self):
        solution = [] # an array to store the cuts, this is nicer than print them one under the other

        while self.n > 0: # while there is rope to cut
            solution.append(self.s[self.n]) # store the cut instead of print it
            self.n = self.n - self.s[self.n] # decrease the rope

        print("Precio máximo: ", self.max_price)
        print("Descomposición óptima:", solution)

if __name__ == '__main__':
    #p_example =  [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    #c = CutTheRope(p_example, 7)

    p_homework = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]
    c = CutTheRope(p_homework, 9)

    c.solve()
    c.print_solution()
