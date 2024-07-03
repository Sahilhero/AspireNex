def print_board(board):
    """Prints the current Tic Tac Toe board."""
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[7]}|{board[8]}|{board[9]}")
    print()

def is_space_free(position, board):
    """Checks if a position on the board is free."""
    return board[position] == ' '

def insert_letter(letter, position, board):
    """Inserts a letter (X or O) into the board at the specified position."""
    if is_space_free(position, board):
        board[position] = letter
        print_board(board)
        if check_for_win(letter, board):
            print(f"{letter} wins!")
            return True
        elif check_draw(board):
            print("It's a draw!")
            return True
    else:
        print("Can't insert there!")
    return False

def check_for_win(mark, board):
    """Checks if a player with 'mark' has won."""
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)             # diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == mark:
            return True
    return False

def check_draw(board):
    """Checks if the game board is full (draw condition)."""
    return all(space != ' ' for space in board.values())

def player_move():
    """Handles the player's move."""
    position = int(input(f"Enter the position for '{player}': ").strip())
    while position not in range(1, 10) or not is_space_free(position, board):
        print("Invalid move. Please choose an empty position from 1 to 9.")
        position = int(input(f"Enter the position for '{player}': ").strip())
    insert_letter(player, position, board)

def comp_move():
    """Handles the computer's move using a basic minimax algorithm."""
    best_score = -float('inf')
    best_move = None
    for key in board.keys():
        if is_space_free(key, board):
            board[key] = computer
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    insert_letter(computer, best_move, board)

def minimax(board, depth, is_maximizing):
    """Minimax algorithm implementation for the computer's move."""
    if check_for_win(computer, board):
        return 1
    elif check_for_win(player, board):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for key in board.keys():
            if is_space_free(key, board):
                board[key] = computer
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for key in board.keys():
            if is_space_free(key, board):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                best_score = min(best_score, score)
        return best_score

def start_game():
    """Starts the Tic Tac Toe game loop."""
    global board, player, computer
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    print("Welcome to Tic Tac Toe!")
    player = input("Do you want to be X or O? ").strip().upper()
    while player not in ['X', 'O']:
        player = input("Invalid choice. Please choose X or O: ").strip().upper()

    computer = 'O' if player == 'X' else 'X'

    first_turn = input("Do you want to go first? (yes/no): ").strip().lower()
    while first_turn not in ['yes', 'no']:
        first_turn = input("Invalid choice. Please enter 'yes' or 'no': ").strip().lower()

    if first_turn == 'no':
        comp_move()

    while not check_for_win(player, board) and not check_for_win(computer, board) and not check_draw(board):
        player_move()
        if check_for_win(player, board) or check_draw(board):
            break
        comp_move()

    if check_for_win(player, board):
        print("Player wins!")
    elif check_for_win(computer, board):
        print("Computer wins!")
    else:
        print("It's a draw!")

    restart_game()

def restart_game():
    """Restarts the game if the player chooses to play again."""
    restart = input("Do you want to play again? (yes/no): ").strip().lower()
    if restart == 'yes':
        start_game()
    elif restart == 'no':
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        restart_game()

# Start the game
start_game()
