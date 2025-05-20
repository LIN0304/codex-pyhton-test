import unittest
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
        board = ['O', None, None,
                 'O', None, None,
                 'O', None, None]
        self.assertEqual(tictactoe.check_winner(board), 'O')

    def test_check_winner_diagonals(self):
        board = ['X', None, None,
                 None, 'X', None,
                 None, None, 'X']
        self.assertEqual(tictactoe.check_winner(board), 'X')

    def test_is_draw(self):
        board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertTrue(tictactoe.is_draw(board))

if __name__ == '__main__':
    unittest.main()
