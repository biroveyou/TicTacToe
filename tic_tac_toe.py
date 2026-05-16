# netAcad PE1 - Final Project

from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   ", board[i][0], "   |   ", board[i][1], "   |   ", board[i][2], "   |", sep="")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_move = int(input("Enter your move: "))
            if 10 > user_move > 0:
                user_move = moves[user_move - 1]
                if user_move in make_list_of_free_fields(board):
                    board[user_move[0]][user_move[1]] = "O"
                    display_board(board)
                    break
                else:
                    print("Already occupied movement")
            else:
                print("Please enter a number between 1 and 9")

        except:
            print("Please enter a integer number for your move")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []

    for r in range(len(board)):
        for c in range(len(board)):
            if not (board[r][c] == "X" or board[r][c] == "O"):
                free_fields.append((r, c))

    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    win = False
    for r in range(len(board)):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            win = True

    for c in range(len(board)):
        if board[0][c] == sign and board[1][c] == sign and board[2][c] == sign:
            win = True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        win = True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        win = True

    if win and sign == "O":
        print("You won the game!")
    if win and sign == "X":
        print("The computer won the game!")
    return win

def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        computer_move = randrange(1, 10)
        computer_move = moves[computer_move - 1]
        if computer_move in make_list_of_free_fields(board):
            board[computer_move[0]][computer_move[1]] = "X"
            print("Compute move:")
            display_board(board)
            break


game_board = [[1, 2, 3],
              [4, "X", 6],
              [7, 8, 9]]

moves = ((0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2))

def main():
    display_board(game_board)
    for i in range(9):
        enter_move(game_board)
        if victory_for(game_board, "O"):
            break
        draw_move(game_board)
        if victory_for(game_board, "X"):
            break
        if i == 3:
            print("Tie")
            break

main()