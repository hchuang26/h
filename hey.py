import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def player_move(board, player):
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player
            break
        else:
            print("Invalid move. Try again.")

def computer_move(board, computer):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            print(f"Computer {computer} chooses row {row} and column {col}.")
            board[row][col] = computer
            break

def main():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]

        user_choice = input("Do you want to go first? (y/n): ")
        if user_choice.lower() == "y":
            human_player = "X"
            computer_player = "O"
        else:
            human_player = "O"
            computer_player = "X"

        current_player = random.choice(players)

        while True:
            if current_player == human_player:
                player_move(board, current_player)
            else:
                computer_move(board, current_player)

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = players[1 - players.index(current_player)]

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
