import unittest
import unittest.mock
from src import tictactoe

class TestTicTacToe(unittest.TestCase):
    def test_make_move(self):
        board = [None] * 9
        self.assertTrue(tictactoe.make_move(board, 0, 'X'))
        self.assertFalse(tictactoe.make_move(board, 0, 'O'))

    def test_check_winner_rows(self):
        board = ['X', 'X', 'X'] + [None] * 6
        self.assertEqual(tictactoe.check_winner(board), 'X')

    def test_check_winner_columns(self):
        board = [
            'O', None, None,
            'O', None, None,
            'O', None, None,
        ]
        self.assertEqual(tictactoe.check_winner(board), 'O')

    def test_check_winner_diagonals(self):
        board = [
            'X', None, None,
            None, 'X', None,
            None, None, 'X',
        ]
        self.assertEqual(tictactoe.check_winner(board), 'X')

    def test_is_draw(self):
        board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertTrue(tictactoe.is_draw(board))

    def test_ai_move_places_O_in_empty_square(self):
        board = ['X', None, None, None, None, None, None, None, None]
        with unittest.mock.patch('random.choice', return_value=1):
            tictactoe.ai_move(board)
        self.assertEqual(board.count('O'), 1)
        self.assertEqual(board[1], 'O')

if __name__ == '__main__':
    unittest.main()
