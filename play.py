from random import randint

def get_player_names():
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """
    player1 = input("\nEnter player 1 name (leave empty for default): ") 
    player2 = input("Enter player 2 name (leave empty for default): ")

    player1 = "Player 1" if player1 == '' else player1
    player2 = "Player 2" if player2 == '' else player2

    return player1, player2


def draw_grid(game_data):
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """
    print("\n\t" + game_data[6] + "|" + game_data[7] + "|" + game_data[8])
    print("\t-----")
    print("\t" + game_data[3] + "|" + game_data[4] + "|" + game_data[5])
    print("\t-----")
    print("\t" + game_data[0] + "|" + game_data[1] + "|" + game_data[2])


def should_continue(game_data):
    return ' ' in game_data


def get_player_input(game_data, mark, player_name):
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """

    while (True):
        try:

            mark_position = int(input(f"({player_name}) Enter number (1-9): "))
            if (game_data[mark_position - 1] == ' '):
                break
            print(f"({player_name}) Your chosen grid is occupied, choose another grid.")

        except ValueError:
            print(f"({player_name}) Please enter a number in range (1-9) inclusive.")
        except IndexError:
            print(f"({player_name}) Please enter a number in range (1-9) inclusive.")

    game_data[mark_position - 1] = mark

    return game_data


def player_has_won(game_data):
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """
    if (game_data[0] == game_data[1] == game_data[2] and (game_data[0] != ' ')):
        return True
    elif (game_data[3] == game_data[4] == game_data[5] and (game_data[3] != ' ')):
        return True
    elif (game_data[6] == game_data[7] == game_data[8] and (game_data[6] != ' ')):
        return True
    elif (game_data[0] == game_data[3] == game_data[6] and (game_data[0] != ' ')):
        return True
    elif (game_data[1] == game_data[4] == game_data[7] and (game_data[1] != ' ')):
        return True
    elif (game_data[2] == game_data[5] == game_data[8] and (game_data[2] != ' ')):
        return True
    elif (game_data[0] == game_data[4] == game_data[8] and (game_data[0] != ' ')):
        return True
    elif (game_data[2] == game_data[4] == game_data[6] and (game_data[2] != ' ')):
        return True
    return False


def print_game_details(win, name):
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """

    if (win):
        print(f"\n{name} has won the game!")
    else:
        print("\nNone of you won the game!")

    print("Thank you for playing...")


def start_game():
    """Starts the tic-tac-toe game."""

    game_data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player_tracker = randint(0, 1)
    win = False

    (name1, name2) = get_player_names()

    while (should_continue(game_data) and not win):
        draw_grid(game_data)
        mark = 'X' if (player_tracker % 2 == 0) else 'O'
        name = name1 if mark == 'X' else name2
        game_data = get_player_input(game_data, mark, name)
        win = player_has_won(game_data)
        player_tracker += 1

    draw_grid(game_data)
    print_game_details(win, name)


if __name__=="__main__":
    start_game()
