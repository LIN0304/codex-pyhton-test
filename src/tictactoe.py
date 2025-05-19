from __future__ import annotations

import random
from typing import List, Optional

Board = List[Optional[str]]  # Each cell can be 'X', 'O', or None

WIN_PATTERNS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def check_winner(board: Board) -> Optional[str]:
    """Return 'X' or 'O' if one of them has won, otherwise None."""
    for a, b, c in WIN_PATTERNS:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board: Board) -> bool:
    """Return True if the board is full and there is no winner."""
    return all(cell is not None for cell in board) and check_winner(board) is None

def make_move(board: Board, position: int, player: str) -> bool:
    """Place player's mark at position (0-8). Return True if successful."""
    if 0 <= position <= 8 and board[position] is None:
        board[position] = player
        return True
    return False

def ai_move(board: Board) -> None:
    """Perform AI move for player 'O'. Uses simple random selection."""
    empty_positions = [i for i, cell in enumerate(board) if cell is None]
    if empty_positions:
        board[random.choice(empty_positions)] = 'O'


def board_to_str(board: Board) -> str:
    """Return a formatted string representing the board."""
    def cell_value(i: int) -> str:
        return board[i] if board[i] is not None else str(i + 1)

    rows = [
        " | ".join(cell_value(i) for i in range(row * 3, (row + 1) * 3))
        for row in range(3)
    ]
    return "\n---------\n".join(rows)


def main() -> None:
    """Play a game of Tic-Tac-Toe against a simple AI."""
    board: Board = [None] * 9
    current_player = 'X'  # human
    while True:
        print(board_to_str(board))
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        if current_player == 'X':
            move = input("Choose your move (1-9): ")
            if not move.isdigit() or not make_move(board, int(move) - 1, 'X'):
                print("Invalid move, try again.")
                continue
        else:
            ai_move(board)
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
