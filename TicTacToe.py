class TicTacToe:
    def __init__(self):
        self.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        self.round = 0
        self.player = 'O'

    def __str__(self) -> str:
        return '\n-+-+-\n'.join(['|'.join(row) for row in self.grid])

    def encode_grid(self) -> str:
        return ''.join([''.join(row) for row in self.grid])

    def has_winner(self) -> bool:
        return any([
            self.grid[0][0] == self.grid[0][1] == self.grid[0][2] != ' ',
            self.grid[1][0] == self.grid[1][1] == self.grid[1][2] != ' ',
            self.grid[2][0] == self.grid[2][1] == self.grid[2][2] != ' ',
            self.grid[0][0] == self.grid[1][0] == self.grid[2][0] != ' ',
            self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != ' ',
            self.grid[0][2] == self.grid[1][2] == self.grid[2][2] != ' ',
            self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ',
            self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' '
        ])

    def which_player(self):
        self.player = 'O' if self.round % 2 == 1 else 'X'

    def round_info(self) -> str:
        return f'Round {self.round} - Player {self.player}'
    
    def user_input(self) -> tuple[int, int]:
        valid = {1, 2, 3}
        x = 0
        y = 0
        while not x in valid and not y in valid:
            x = int(input('x: '))
            y = int(input('y: '))
        return x, y

    def play(self):
        while self.round <= 9 and not self.has_winner():
            self.round += 1
            self.player = self.which_player()
            print(self.round_info())
            x, y = self.user_input()
            self.move(x, y)
            print(self)
        print(f'Player {self.player} wins!')

    def move(self, x: int, y: int):
        if self.grid[x - 1][y - 1] == ' ':
            self.grid[x - 1][y - 1] = self.player
