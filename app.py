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
        print('\n-+-+-\n'.join(['|'.join(row) for row in self.grid]))

    def encode_grid(self) -> str:
        return ''.join([''.join(row) for row in self.grid])

if __name__ == '__main__':
    ttc = TicTacToe()
    ttc.display_grid()
    print(ttc.encode_grid())
