import unittest
from io import StringIO
import sys
from unittest.mock import patch
import play

class MyTestCase(unittest.TestCase):
    def test_get_player_names(self):
        with patch('sys.stdin', StringIO("Jayson\nAnton")):
            temp_out = StringIO()
            sys.stdout = temp_out
            result = play.get_player_names()
            my_out = temp_out.getvalue()
        self.assertEqual(my_out,
        "\nEnter player 1 name (leave empty for default): Enter player 2 name (leave empty for default): ")
        self.assertEqual(result, ('Jayson', 'Anton'))

    def test_get_player_names_default(self):
        with patch('sys.stdin', StringIO("\nAnton")):
            temp_out = StringIO()
            sys.stdout = temp_out
            result = play.get_player_names()
            my_out = temp_out.getvalue()
        self.assertEqual(my_out,
        "\nEnter player 1 name (leave empty for default): Enter player 2 name (leave empty for default): ")
        self.assertEqual(result, ('Player 1', 'Anton'))

    def test_draw_grid(self):
        game_data = ['X', ' ', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
        temp_out = StringIO()
        sys.stdout = temp_out
        result = play.draw_grid(game_data)
        my_out = temp_out.getvalue()
        self.assertEqual(my_out, '\n\t | | \n\t-----\n\tO|X| \n\t-----\n\tX| | \n')

    def test_should_continue_true(self):
        game_data = ['X', ' ', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
        result = play.should_continue(game_data)
        self.assertTrue(result)

    def test_should_continue_false(self):
        game_data = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        result = play.should_continue(game_data)
        self.assertFalse(result)

    def test_get_player_input(self):
        game_data = ['X', ' ', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
        with patch('sys.stdin', StringIO("Left\n1\n9")):
            temp_out = StringIO()
            sys.stdout = temp_out
            result = play.get_player_input(game_data, 'O', "Anton")
            my_out = temp_out.getvalue()
        self.assertEqual(my_out, "(Anton) Enter number (1-9): (Anton) Please enter a number in range (1-9) inclusive." +
        "\n(Anton) Enter number (1-9): (Anton) Your chosen grid is occupied, choose another grid." +
        "\n(Anton) Enter number (1-9): ")
        self.assertEqual(result, ['X', ' ', ' ', 'O', 'X', ' ', ' ', ' ', 'O'])

    def test_player_has_won_false(self):
        game_data = ['X', 'O', 'X ', 'O', 'X', ' ', ' ', ' ', ' ']
        self.assertFalse(play.player_has_won(game_data))

    def test_player_has_won_true(self):
        game_data = ['X', 'O', 'X ', 'X', 'O', ' ', 'X', ' ', 'O']
        self.assertTrue(play.player_has_won(game_data))

if __name__=='__main__':
    unittest.main()