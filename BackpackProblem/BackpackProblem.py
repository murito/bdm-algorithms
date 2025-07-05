"""
Jul 03, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Dynamic Programming
Backpack problem + backtracking to find taken objects
"""
class BackpackProblem:
    def __init__(self, values, weights, backpack):
        self.v = values
        self.w = weights
        self.n = len(values)
        self.W = backpack
        self.V = [[0 for _ in range(self.W + 1)] for _ in range(self.n + 1)]

    def solve(self):
        for i in range(1, self.n + 1): # we always add one to make the range inclusive
            for x in range(0, self.W + 1): # we always add one to make the range inclusive
                j = x - self.w[i - 1] # backpack weight minus current weight
                if j < 0: # Check for the previous row in the current column
                    self.V[i][x] = max(self.V[i - 1][x], 0)
                else: # check for the previous row-column against previous row previous 2 columns plus current value, take the max value
                    self.V[i][x] = max(self.V[i - 1][x], (self.V[i - 1][j] + self.v[i - 1]) )

    # Backtrack the matrix
    def taken_items(self):
        column = self.W
        items_taken = []
        for i in range(self.n, 0, -1):
            if self.V[i][column] != self.V[i - 1][column]: # If the value in the previous row same column is different, current value was part of the solution
                items_taken.append(i) # add the index as part f the solution
                column -= self.w[i - 1] # decrease the space in the backpack with the weight we just mark as part of the solution

        # build a new matrix to nicely print the result
        result = [[0 for _ in range(len(items_taken))] for _ in range(3)]
        for i, idx in enumerate(items_taken):
            result[0][i] = idx           # Index of the taken item
            result[1][i] = self.v[idx-1] # Value of the taken item
            result[2][i] = self.w[idx-1] # Weight of the taken item

        return result

    def print_solution(self):
        r = self.taken_items()
        print("Items tomados:                 ", r[0])
        print("Suma de pesos:                 ", r[2], " = ", sum(r[2]))
        print("Suma de valores:               ", r[1], " = ", sum(r[1]))
        print("Tamaño de la mochila:          ", self.W)
        print("Valor óptimo dentro la mochila:", self.V[self.n][self.W])

if __name__ == '__main__':
    values_example = [3,2,4,4]
    weights_example = [4,3,2,3]
    backpack_example = 6

    values_homework =  [79,32,47,18,26,85,33,40,45,59]
    weights_homework = [85,26,48,21,22,95,43,45,55,52]
    backpack_homework = 140

    b = BackpackProblem(values_homework, weights_homework , backpack_homework )
    b.solve()
    b.print_solution()
    b.taken_items()