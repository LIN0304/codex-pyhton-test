const board = Array(9).fill(null);
const cells = document.querySelectorAll('.cell');
const statusEl = document.getElementById('status');
let currentPlayer = 'X';

const WIN_PATTERNS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
];

function checkWinner(b) {
    for (const [a, c, d] of WIN_PATTERNS) {
        if (b[a] && b[a] === b[c] && b[a] === b[d]) {
            return b[a];
        }
    }
    return null;
}

function isDraw(b) {
    return b.every(v => v !== null) && !checkWinner(b);
}

function aiMove() {
    const empty = board.map((v, i) => v === null ? i : null).filter(i => i !== null);
    if (empty.length === 0) return;
    const choice = empty[Math.floor(Math.random() * empty.length)];
    board[choice] = 'O';
    cells[choice].textContent = 'O';
}

function updateStatus() {
    const winner = checkWinner(board);
    if (winner) {
        statusEl.textContent = `${winner} wins!`;
        cells.forEach(c => c.removeEventListener('click', handleClick));
    } else if (isDraw(board)) {
        statusEl.textContent = "It's a draw!";
    }
}

function handleClick(e) {
    const idx = parseInt(e.target.dataset.index, 10);
    if (board[idx] || checkWinner(board)) return;
    board[idx] = 'X';
    e.target.textContent = 'X';
    if (!checkWinner(board) && !isDraw(board)) {
        aiMove();
    }
    updateStatus();
}

cells.forEach(cell => cell.addEventListener('click', handleClick));
