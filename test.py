from sudoku_generator import *

sudoku = SudokuGenerator(9, 30)
sudoku.board[0][1] = 2

# print(sudoku.valid_in_box(3, 0, 2))
# sudoku.fill_diagonal()
# sudoku.print_board()
# print(sudoku.is_valid(3, 3, 2))

sudoku_board = generate_sudoku(9, 30)
for row in sudoku_board:
    for col in row:
        print(col, end=' ')
    print()
