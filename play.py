from random import randint

def get_player_names():
    """
    Gets player names. Defaults to 'Player 1' and/or 'Player 2' if either has entered their names.

    Returns:
    tuple: The names of the players.
    """

    player1 = input("\nEnter player 1 name (leave empty for default): ") 
    player2 = input("Enter player 2 name (leave empty for default): ")

    player1 = "Player 1" if player1 == '' else player1
    player2 = "Player 2" if player2 == '' else player2

    return player1, player2


def draw_grid(game_data):
    """
    Draws the 3x3 tic-tac-toe game grid.
  
    Parameters:
    game_data (list): A list containing the game data.
    """

    print("\n\t" + game_data[6] + "|" + game_data[7] + "|" + game_data[8])
    print("\t-----")
    print("\t" + game_data[3] + "|" + game_data[4] + "|" + game_data[5])
    print("\t-----")
    print("\t" + game_data[0] + "|" + game_data[1] + "|" + game_data[2])


def should_continue(game_data):
    """
    Returns True if there's still and unoccupied grid in the game data list.

    Parameters:
    game_data (list): A list containing the game data.
    
    Returns:
    bool: True if there is at least one unoccupied grid in the game data list.
    """

    return ' ' in game_data


def get_player_input(game_data, mark, player_name):
    """
    Validates the input from the user and inserts a player mark to the game data list.
  
    Parameters:
    game_data (list): A list containing the game data.
    mark (str): A cross or naught based on the current player that is to be inserted into the game data list
    player_name: The name of the player who is taking a turn 
  
    Returns:
    list: The game data list with a new naught or cross inserted
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
    Return True if a player has won a game and False otherwise.
  
    Parameters:
    game_data (list): A list containing the game data.
  
    Returns:
    bool: True if a player has won the game and False otherwise.
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
    Prints the details of the game after gameplay.
  
    Parameters:
    win (bool): True of False based on whether either player won or not.
    name (str): The name of the player who has won the game.
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
