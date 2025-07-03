"""
Jun 28,2025
Francisco Javier Alcalá Olivares
--------------------------------------
Sudoku solver using backtracking
"""
class Sudoku:
    # Extract the 9 quadrants from the grid to validate against them
    def extract_quadrants(self,grid):
        quadrants = []
        # We multiply by 3 to increase the value on each iteration
        # that way we reduce the numer of iterations here
        """
              Q0          Q2
            |X X X |   |X X X |
            |X X X |   |X X X |
            |X X X |...|X X X |
            .
            .
            .
            |X X X |   |X X X |
            |X X X |   |X X X |
            |X X X |...|X X X |
               Q6         Q8
        """
        for i in range(3):
            for j in range(3):
                quadrants.append(
                    [
                        grid[i*3][j*3]  ,grid[i*3][j*3+1]  ,grid[i*3][j*3+2],
                        grid[i*3+1][j*3],grid[i*3+1][j*3+1],grid[i*3+1][j*3+2],
                        grid[i*3+2][j*3],grid[i*3+2][j*3+1],grid[i*3+2][j*3+2]
                    ]
                )

        return quadrants

    # Here we verify if a number appears in a column,same "cell" coordinate,
    # but we iterate over each "row" if the number appears return True,it already exits
    def in_column(self,grid,cell,number):
        for i in range(9):
            if grid[i][cell] == number:
                return True
        return False

    # Here we just calculate the number of a quadrant based on the coordinate
    # Using the same approach of multiply to avoid unnecessary iterations
    # In case of a invalid coordinate return -1
    def get_quadrant_index(self,x,y):
        for i in range(3):
            if x in [i*3,i*3+1,i*3+2]:
                if  y in [0,1,2]:#Q0-Q2
                    return i*3
                if y in [3,4,5]:#Q3-Q5
                    return i*3+1
                if y in [6,7,8]:#Q6-Q8
                    return i*3+2
        return -1

    # Here we return the first empty cell or None if every cell has a value
    def empty_cell(self,grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i,j
        return None,None

    # this is our Feasibility function
    # number is not in row,it is not in quadrant,and it is not in column
    def is_valid(self,grid,x,y,number):
        quadrants = self.extract_quadrants(grid)
        return number not in grid[x] and number not in quadrants[self.get_quadrant_index(x,y)] and not self.in_column(grid,y,number)

    # Our recursive function to solve cell by cell
    def solve(self,grid):
        # get an empty cell to resolve
        x,y = self.empty_cell(grid)

        # If there are no more empty cells we finished,return True
        if x is None and y is None:
            return True

        # For each number from 1 to 9 check for the feasibility of putting that number there
        for i in range(1,10):
            if self.is_valid(grid,x,y,i):
                grid[x][y] = i

                # Then try to solve the next empty cell,if we success that was the right position
                if self.solve(grid):
                    return True
                else: # In case we couldn't solve we need to reset the cell to its empty value
                    grid[x][y] = 0

        # If none of the nine numbers were feasible for that position
        # return false,we are pruning here
        return False

    # Just printing the solution
    def print_grid(self,grid):
        for i in range(9):
            print(grid[i])

if __name__ == '__main__':
    game1 = [
        [5,0,0,9,1,3,7,2,0],
        [3,0,0,0,8,0,5,0,9],
        [0,9,0,2,5,0,0,8,0],
        [6,8,0,4,7,0,2,3,0],
        [0,0,9,5,0,0,4,6,0],
        [7,0,4,0,0,0,0,0,5],
        [0,2,0,0,0,0,0,0,0],
        [4,0,0,8,9,1,6,0,0],
        [8,5,0,7,2,0,0,0,3]
    ]

    game2 = [
        [6,9,0,0,0,0,7,0,0],
        [0,0,0,0,9,6,0,0,0],
        [0,8,0,7,5,3,0,9,0],
        [0,2,0,3,7,4,5,6,1],
        [3,6,7,0,0,5,0,2,0],
        [0,0,0,9,6,0,3,7,8],
        [0,0,6,0,3,1,0,8,4],
        [0,4,5,8,0,7,6,0,0],
        [0,0,0,0,0,0,0,5,7]
    ]

    s = Sudoku()

    print("=========================== Game 1 ===========================")

    s.solve(game1)
    s.print_grid(game1)

    print("=========================== Game 2 ===========================")

    s.solve(game2)
    s.print_grid(game2)