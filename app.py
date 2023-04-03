class TicTacToe:
    def __init__(self):
        self.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        # self.player1 = input('Player 1: ')
        # self.player2 = input('Player 2: ')
    def __str__(self):
        return '\n-+-+-\n'.join(['|'.join(row) for row in self.grid])

    def encode_grid(self) -> str:
        """Returns a string representation of the grid."""
        return ''.join([''.join(row) for row in self.grid])
    
    def is_winning_position(self) -> bool:
        grid = self.encode_grid()
        return any([
            grid[0] == grid[1] == grid[2] != ' ',
            grid[3] == grid[4] == grid[5] != ' ',
            grid[6] == grid[7] == grid[8] != ' ',
            grid[0] == grid[3] == grid[6] != ' ',
            grid[1] == grid[4] == grid[7] != ' ',
            grid[2] == grid[5] == grid[8] != ' ',
            grid[0] == grid[4] == grid[8] != ' ',
            grid[2] == grid[4] == grid[6] != ' '
        ])
    
    def play(self, player: str, x: int, y: int):
        if self.grid[x-1][y-1] == ' ':
            self.grid[x-1][y-1] = player

if __name__ == '__main__':
    ttc = TicTacToe()
    ttc.play('O', 1, 1)
    ttc.play('X', 1, 2)
    ttc.play('O', 2, 2)
    ttc.play('X', 2, 1)
    ttc.play('O', 3, 3)
    # ttc.display_grid()
    print(ttc)
    print(ttc.is_winning_position())
