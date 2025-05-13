def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row, solutions):
        if row == n:
            solutions.append(["." * i + "Q" + "." * (n - i - 1) for i in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1, solutions)
                board[row] = -1 

    solutions = []
    solve([-1] * n, 0, solutions)
    return solutions

# test case
result = solve_n_queens(4)
for solution in result:
    for row in solution:
        print(row)
    print()
