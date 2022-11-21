from sudoku_generator import SudokuGenerator

sudoku = SudokuGenerator(9, 30)
sudoku.board[0][1] = 2
sudoku.print_board()
print(sudoku.valid_in_box(3, 0, 2))