def solve_sudoku(board):
    def is_valid(board, r, c, num):
        
        for i in range(9):
            if board[r][i] == num:
                return False
       
        for i in range(9):
            if board[i][c] == num:
                return False
       
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:  
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            if backtrack(board):
                                return True
                            board[r][c] = 0  
                    return False
        return True  

    backtrack(board)

# test cases
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(sudoku_board)

for row in sudoku_board:
    print(row)
