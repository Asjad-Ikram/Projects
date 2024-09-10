#Sudoku Solving Program

Puzzle=[[0, 6, 0, 0, 0, 0, 5, 0, 0],\
        [0, 0, 3, 2, 0, 0, 0, 4, 0],\
        [0, 0, 0, 0, 1, 0, 0, 7, 0],\
        [2, 0, 0, 0, 0, 0, 0, 0, 3],\
        [0, 0, 0, 0, 0, 0, 6, 0, 0],\
        [0, 0, 8, 0, 0, 0, 0, 0, 0],\
        [0, 3, 0, 0, 0, 8, 0, 0, 0],\
        [0, 0, 0, 5, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 4, 0, 0, 0, 2]]

def find_empty_space(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==0:
                return r,c
    return None,None


def is_guess_valid(puzzle, guess,row,col):
    
    #Checking  the rows
    if guess in puzzle[row]:
        return False
    
    #Checking the columns
    col_val=[]
    for i in range(9):
        col_val.append(puzzle[i][col])
        if guess in col_val:
            return False    
    
    #Checking 9x9 Box
    row_start=(row//3)*3
    col_start=(col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if guess == puzzle[r][c]:
                return False
            
    return True


#The Puzzle is solved using backtracking
def Sudoku_Solver(puzzle):

    row,col=find_empty_space(puzzle)
    
    #Checking to see if row or col is empty/0 (only one needs to be checked). In this case the table is filled and our work is done
    if row is None:
        return True    
    
    #checking a valid guess
    for guess in range(1,10):
        if is_guess_valid(puzzle, guess,row,col):
            puzzle[row][col]= guess

            if Sudoku_Solver(puzzle):
                return True

        Puzzle[row][col]=0

Sudoku_Solver(Puzzle)
print(Puzzle)