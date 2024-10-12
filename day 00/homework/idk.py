def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([row[col] == player for row in board]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all[board[i][2 - i] == player for i in range(3)]