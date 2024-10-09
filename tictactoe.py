from random import randrange

def display_board(board):
    print('\n'.join(' | '.join(map(str, row)) + '\n' + '-' * 9 for row in board))

def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= (move := int(move)) <= 9:
            row, col = divmod(move - 1, 3)
            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                return
            print("Square taken. Choose another.")
        print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board, sign):
    return any(all(cell == sign for cell in row) for row in board) or \
           any(all(board[r][c] == sign for r in range(3)) for c in range(3)) or \
           all(board[i][i] == sign for i in range(3)) or \
           all(board[i][2 - i] == sign for i in range(3))

def draw_move(board):
    free_fields = [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['O', 'X']]
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    board = [[1 + j + i * 3 for j in range(3)] for i in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)
    
    while True:
        enter_move(board)
        display_board(board)
        if check_win(board, 'O'):
            print("You win!")
            break
        if all(isinstance(cell, str) for row in board for cell in row):
            print("It's a tie!")
            break
        draw_move(board)
        display_board(board)
        if check_win(board, 'X'):
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()
