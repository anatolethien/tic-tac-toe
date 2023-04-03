class TicTacToe:
    def __init__(self):
        self.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        self.player1 = input('Player 1: ')
        self.player2 = input('Player 2: ')

    def display_grid(self):
        rows = ['|'.join(row) for row in self.grid]
        print('\n-+-+-\n'.join(rows))

    def encode_grid(self) -> str:
        rows = [''.join(row) for row in self.grid]
        return ''.join(rows)

if __name__ == '__main__':
    ttc = TicTacToe()
    ttc.display_grid()
    print(ttc.encode_grid())
